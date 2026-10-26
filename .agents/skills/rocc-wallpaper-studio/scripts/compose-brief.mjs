#!/usr/bin/env node
import {readFile,mkdir,writeFile,access,rm} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {compileBrief} from '../references/planner.mjs';
const args=process.argv.slice(2),opts={};
try{
 if(args.includes('--help')){console.log('node compose-brief.mjs --subject TEXT [--recipe rocc] [--language zh|en] [--format poster] [--palette paper] [--title TEXT] --out DIR');process.exit(0);}
 const allowed=new Set(['subject','recipe','format','palette','title','out','language']);
 for(let i=0;i<args.length;i+=2){const k=args[i].replace(/^--/,'');if(!allowed.has(k)||args[i+1]===undefined)throw new Error('未知选项或缺少参数；用 --help 查看。');opts[k]=args[i+1];}
 if(!opts.out)throw new Error('必须用 --out 指定新的输出目录。');
 const data=JSON.parse(await readFile(new URL('../references/recipes.json',import.meta.url),'utf8'));
 const brief=compileBrief(data,opts),out=path.resolve(opts.out),names=['brief.json','brief.md','prompt.txt'];
 for(const n of names){let exists=false;try{await access(path.join(out,n));exists=true;}catch{}if(exists)throw new Error(`拒绝覆盖已有文件：${n}`);}
 await mkdir(out,{recursive:true});
 const created=[];
 try{for(const [n,body] of [['brief.json',JSON.stringify(brief,null,2)],['brief.md',brief.taskMarkdown],['prompt.txt',brief.prompt]]){await writeFile(path.join(out,n),body,{encoding:'utf8',flag:'wx'});created.push(path.join(out,n));}}
 catch(e){await Promise.all(created.map(p=>rm(p,{force:true})));throw e;}
 console.log(JSON.stringify({status:'brief_ready',imageGenerated:false,files:names.map(n=>path.join(out,n))}));
}catch(e){console.error(e.message);process.exitCode=1;}
