#!/usr/bin/env python3
"""www/index.html থেকে claude.ai artifact প্রিভিউ বানায়: আসল Firebase-এর বদলে মেমোরিতে থাকা ডেমো ডেটাবেস।"""
import re, sys, pathlib, json
root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1])
s = (root / 'www/index.html').read_text(encoding='utf-8')
mcq = (root / 'www/mcq.js').read_text(encoding='utf-8')

today_note = "অনুশীলনী 2.1 (নমুনা)"
MOCK = r"""
<script>
/* প্রিভিউ: মেমোরিতে থাকা ডেমো ডেটাবেস; পাতা বন্ধ করলে সব মুছে যায় */
(function(){
  const pad=n=>String(n).padStart(2,'0'), d=new Date(), today=`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
  const ago=new Date(Date.now()-3600e3).toISOString();
  const store={routines:{}, syllabus:{}, results:{}, reports:{}, pdfs:{}, payments:{}, users:{}, phones:{}};
  store.routines['c10_'+today]={course:'c10',date:today,kind:'daily',syllabus:'অনুশীলনী 2.1 (সেট)',chapter:2,ex:'2.1',publishAt:ago};
  store.syllabus['ex_c10_2_1']={type:'exnote',course:'c10',no:2,ex:'2.1',title:'অনুশীলনী 2.1: সেট (নমুনা নোট)',note:'এটি প্রিভিউয়ের নমুনা নোট।\nঅ্যাডমিন প্যানেল → অধ্যায় ট্যাব থেকে প্রতিটি অনুশীলনীর আলাদা নোট দেওয়া যায়।',link:'',publishAt:ago};
  const subs={routines:[],syllabus:[],results:[],reports:[],pdfs:[],payments:[],users:[],phones:[]}; let authCb=null; const accounts={}, dsubs=[]; let cur=null;
  const emit=n=>{ const docs=Object.entries(store[n]).map(([id,v])=>({id,data:()=>v})); subs[n].forEach(f=>f({docs})); dsubs.filter(w=>w.n===n).forEach(w=>w.f(store[n][w.id]?JSON.parse(JSON.stringify(store[n][w.id])):null)); };
  const aerr=c=>{ const e=new Error('auth'); e.code=c; return Promise.reject(e); };
  window.SohogDB={ init(){return true;}, onAuth(cb){ authCb=cb; setTimeout(()=>cb(null),20); },
    collection(n){ return { orderBy(){return this;}, onSnapshot(next){ subs[n].push(next); setTimeout(()=>emit(n),30); return ()=>{ subs[n]=subs[n].filter(f=>f!==next); }; },
      doc(id){ return { get:async()=>store[n][id]?JSON.parse(JSON.stringify(store[n][id])):null, set:async v=>{ store[n][id]=JSON.parse(JSON.stringify(v)); emit(n); }, delete:async()=>{ delete store[n][id]; emit(n); } }; } }; },
    signIn(email,pw){ email=String(email||'').toLowerCase(); const a=accounts[email];
      if(a&&a.pw!==pw) return aerr('auth/invalid-credential');
      if(!a&&email.endsWith('@phone.sohog.app')) return aerr('auth/invalid-credential');
      cur={uid:a?a.uid:'admin',email}; setTimeout(()=>authCb&&authCb(cur),5); return Promise.resolve(cur); },
    signUp(email,pw){ email=String(email||'').toLowerCase(); if(accounts[email]) return aerr('auth/email-already-in-use'); if(String(pw).length<6) return aerr('auth/weak-password');
      const uid='u'+Math.random().toString(36).slice(2,10); accounts[email]={pw,uid}; cur={uid,email}; setTimeout(()=>authCb&&authCb(cur),5); return Promise.resolve(cur); },
    resetPassword(email){ return accounts[String(email).toLowerCase()]?Promise.resolve():aerr('auth/user-not-found'); },
    checkAdmin(){ return Promise.resolve(!!cur&&cur.uid==='admin'); },
    docGet(n,id){ return Promise.resolve(store[n]&&store[n][id]?JSON.parse(JSON.stringify(store[n][id])):null); },
    docSet(n,id,v,merge){ store[n][id]=Object.assign(merge&&store[n][id]?store[n][id]:{},JSON.parse(JSON.stringify(v))); setTimeout(()=>emit(n),5); return Promise.resolve(); },
    docWatch(n,id,next){ const w={n,id,f:next}; dsubs.push(w); setTimeout(()=>next(store[n][id]?JSON.parse(JSON.stringify(store[n][id])):null),10); return ()=>{ const i=dsubs.indexOf(w); if(i>=0) dsubs.splice(i,1); }; },
    async signOut(){ cur=null; setTimeout(()=>authCb&&authCb(null),20); } };
  window.__SOHOG_TEST__={ kickOtherDevice(uid){ const u=store.users[uid]; if(u){ u.device='other-device'; emit('users'); } }, accounts, store };
  window.SOHOG_FIREBASE={apiKey:'demo'};
})();
</script>
"""
BANNER = """<div class="demo-bar" role="note">প্রিভিউ: এখানে করা কিছুই সংরক্ষণ হয় না। নতুন অ্যাকাউন্ট খুলে দেখতে পারেন; অ্যাডমিন অংশ দেখতে "অ্যাডমিন লগইন"-এ যেকোনো ইমেইল ও পাসওয়ার্ড দিন।</div>"""
title = re.search(r'<title>.*?</title>', s, re.S).group(0).replace('সহগ গণিত একাডেমি', 'সহগ গণিত একাডেমি প্রিভিউ')
head = s[s.index('<head>')+6:s.index('</head>')]
head = re.sub(r'<title>.*?</title>\n?', '', head, flags=re.S)
head = re.sub(r'<meta charset[^>]*>\n?|<meta name="viewport"[^>]*>\n?|<meta name="theme-color"[^>]*>\n?|<link rel="manifest"[^>]*>\n?|<link rel="icon"[^>]*>\n?|<link rel="apple-touch-icon"[^>]*>\n?', '', head)
head = head.replace('<script src="config.js"></script>\n', '').replace('<script src="db.js"></script>\n', MOCK).replace('<script src="mcq.js"></script>\n', '<script>\n' + mcq + '</script>\n')
head += '<style>.demo-bar{background:var(--amber-soft);color:var(--amber);font-size:13px;font-weight:600;text-align:center;padding:8px 16px;border-bottom:1px solid var(--line)}</style>\n'
body = s[s.index('<body>')+6:s.index('</body>')]
page = title + '\n<meta name="claude:viewport-fit-sides" content="cover">\n' + head + BANNER + body
assert 'config.js' not in page and 'src="db.js"' not in page
out.write_text(page, encoding='utf-8')
print('preview written', out, len(page))
