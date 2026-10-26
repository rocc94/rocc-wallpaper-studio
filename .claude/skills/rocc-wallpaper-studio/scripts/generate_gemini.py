#!/usr/bin/env python3
"""Generate exactly one image from a compiled brief using your GEMINI_API_KEY."""
import argparse,base64,json,os,struct,urllib.request,urllib.error
from pathlib import Path

MODEL='gemini-nano-banana-2.1'
ENDPOINT='https://generativelanguage.googleapis.com/v1beta/interactions'

def image_from_response(data):
    blocks=[b for s in data.get('steps',[]) if s.get('type')=='model_output' for b in s.get('content',[])]
    image=next((b for b in blocks if b.get('type')=='image' and b.get('mime_type')=='image/png'),None)
    if not image: raise ValueError('No PNG returned; no automatic retry was made.')
    raw=base64.b64decode(image['data'],validate=True)
    if len(raw)>15_000_000 or raw[:8]!=b'\x89PNG\r\n\x1a\n' or len(raw)<24: raise ValueError('Invalid or oversized PNG')
    w,h=struct.unpack('>II',raw[16:24])
    if not (32<=w<=16384 and 32<=h<=16384): raise ValueError('Unexpected image dimensions')
    return raw,w,h

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--brief',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--dry-run',action='store_true');a=p.parse_args()
    brief=json.loads(a.brief.read_text(encoding='utf8'))
    if brief.get('ratio') not in ['2:3','9:16','16:9','1:1'] or not isinstance(brief.get('prompt'),str) or len(brief['prompt'])>12000: raise ValueError('Invalid compiled brief')
    if a.out.exists(): raise FileExistsError('Output already exists; choose a new directory.')
    if a.dry_run:
        print(json.dumps({'status':'ready_not_generated','model':MODEL,'ratio':brief['ratio'],'store':False,'requests':0}));return
    key=os.environ.get('GEMINI_API_KEY','')
    if len(key)<16: raise ValueError('Set your own GEMINI_API_KEY locally. Do not paste it into a chat or command argument.')
    request=urllib.request.Request(ENDPOINT,data=json.dumps({'model':MODEL,'input':brief['prompt'],'store':False,'response_format':{'type':'image','mime_type':'image/png','aspect_ratio':brief['ratio'],'image_size':'1K'}}).encode(),headers={'Content-Type':'application/json','x-goog-api-key':key},method='POST')
    try:
        with urllib.request.urlopen(request,timeout=120) as r:
            payload=r.read(21_000_001)
        if len(payload)>21_000_000: raise ValueError('Response too large')
    except urllib.error.HTTPError as e:
        raise ValueError(f'Provider returned HTTP {e.code}; check key, billing, model access and region. No automatic retry.') from None
    except (urllib.error.URLError,TimeoutError):
        raise ValueError('Connection failed or timed out. Upstream billing may still apply; no automatic retry.') from None
    finally: key=None
    raw,w,h=image_from_response(json.loads(payload))
    a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'result.png').write_bytes(raw)
    (a.out/'provenance.json').write_text(json.dumps({'model':MODEL,'provider':'Google Gemini','nativeWidth':w,'nativeHeight':h,'requestedSize':'1K','recipeVersion':brief['version'],'recipe':brief['recipe'],'review':'unreviewed','attempts':1},ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'status':'generated_unreviewed','image':str(a.out/'result.png'),'nativePixels':[w,h]},ensure_ascii=False))

if __name__=='__main__':
    try:main()
    except (ValueError,FileExistsError,OSError,KeyError) as e:raise SystemExit(str(e))
