/* ---------- অ্যাডমিনের যোগ করা MCQ (Firebase: syllabus সংগ্রহে type:'mcq') ---------- */
const QLV=['সহজ','মধ্যম','কঠিন'];
function customQs(cid,no){
  return Object.values(SYL).filter(r=>r.type==='mcq'&&r.course===cid&&+r.ch===+no&&Array.isArray(r.o)&&r.o.length===4)
    .sort((a,b)=>String(a.createdAt||'')<String(b.createdAt||'')?-1:1)
    .map(r=>({n:'x:'+r.id,q:String(r.q),o:r.o.map(String),a:+r.a,e:String(r.e||''),lv:QLV.indexOf(r.lv)>=0?r.lv:'মধ্যম',custom:true,id:r.id}));
}
function qfInit(){
  if(!S.qf) S.qf={course:CH_COURSES()[0], ch:1, mode:'one', q:'', o:['','','',''], a:-1, e:'', lv:'সহজ', bulk:'', parsed:null, editId:null, armed:'', busy:false, msg:'', showAll:false};
  return S.qf;
}
const LET={'ক':0,'খ':1,'গ':2,'ঘ':3,'a':0,'b':1,'c':2,'d':3};
function parseBulk(text){
  const blocks=String(text||'').replace(/\r/g,'').split(/\n\s*\n/).map(b=>b.trim()).filter(Boolean);
  const out=[], errs=[];
  blocks.forEach((b,bi)=>{
    const lines=b.split('\n').map(l=>l.trim()).filter(Boolean);
    const q={q:[],o:[null,null,null,null],a:-1,e:'',lv:'মধ্যম'};
    lines.forEach(l=>{
      let m;
      if((m=l.match(/^[\(（]?\s*([কখগঘabcdABCD])\s*[\)\.।:）]\s*(.+)$/))&&q.q.length){ q.o[LET[m[1].toLowerCase()]]=m[2].trim(); return; }
      if((m=l.match(/^(উত্তর|উঃ|উ:|ans(wer)?)\s*[:：\-=]?\s*[\(（]?\s*([কখগঘabcdABCD])/i))){ q.a=LET[m[3].toLowerCase()]; return; }
      if((m=l.match(/^(ব্যাখ্যা|সমাধান|explanation)\s*[:：\-]\s*(.*)$/i))){ q.e=m[2].trim(); return; }
      if((m=l.match(/^(স্তর|মান|level)\s*[:：\-]\s*(সহজ|মধ্যম|কঠিন)/i))){ q.lv=m[2]; return; }
      if(q.o.some(Boolean)) { q.e=q.e?q.e+' '+l:l; return; }
      q.q.push(l.replace(/^\d+\s*[\.\)।]\s*/,''));
    });
    const no=bi+1;
    if(!q.q.length) errs.push(`${no} নম্বর প্রশ্ন: প্রশ্নের লেখা নেই`);
    else if(q.o.some(x=>!x)) errs.push(`${no} নম্বর প্রশ্ন: ক, খ, গ, ঘ চারটি অপশনই লাগবে`);
    else if(new Set(q.o).size<4) errs.push(`${no} নম্বর প্রশ্ন: দুটি অপশন একই রকম`);
    else if(q.a<0) errs.push(`${no} নম্বর প্রশ্ন: "উত্তর: গ" এভাবে সঠিক উত্তর লিখুন`);
    else out.push({q:q.q.join(' '),o:q.o,a:q.a,e:q.e,lv:q.lv});
  });
  return {qs:out,errs,blocks:blocks.length};
}
async function saveQ(cid,ch,x,id){
  const docId=id||`q_${cid}_${ch}_${Date.now().toString(36)}${Math.random().toString(36).slice(2,6)}`;
  await DB.collection('syllabus').doc(docId).set({type:'mcq',course:cid,ch:+ch,q:x.q,o:x.o,a:x.a,e:x.e||'',lv:x.lv,createdAt:(id&&SYL[id]&&SYL[id].createdAt)||new Date().toISOString(),updatedAt:new Date().toISOString()});
}
function qbankPanel(){
  const qf=qfInit(), c=COURSES[qf.course], built=((window.SOHOG_MCQ||{})[qf.course]||{})[String(qf.ch)]||[], mine=customQs(qf.course,qf.ch);
  const L=['ক','খ','গ','ঘ'];
  const one=`<div class="field"><label for="qfQ">প্রশ্ন</label><textarea class="input area" id="qfQ" data-qf="q" rows="3" maxlength="600" placeholder="যেমন: √49 = কত?">${esc(qf.q)}</textarea></div>
    ${L.map((l,k)=>`<div class="qopt-row"><label class="qopt-pick"><input type="radio" name="qfA" value="${k}" data-qfa="${k}" ${qf.a===k?'checked':''}><span>${l}</span></label>
      <input class="input" data-qfo="${k}" maxlength="200" aria-label="অপশন ${l}" placeholder="অপশন ${l}" value="${esc(qf.o[k])}"></div>`).join('')}
    <p class="muted" style="margin:0;font-size:13px">সঠিক উত্তরের অক্ষরে (ক/খ/গ/ঘ) চাপ দিন।</p>
    <div class="field"><label for="qfLv">স্তর</label><select class="input" id="qfLv" data-qf="lv">${QLV.map(v=>`<option ${v===qf.lv?'selected':''}>${v}</option>`).join('')}</select></div>
    <div class="field"><label for="qfE">ব্যাখ্যা (ঐচ্ছিক)</label><textarea class="input area" id="qfE" data-qf="e" rows="2" maxlength="600" style="min-height:70px">${esc(qf.e)}</textarea></div>
    <button class="btn" data-qsave style="width:100%" ${qf.busy?'disabled':''}>${qf.busy?'সংরক্ষণ হচ্ছে…':qf.editId?'পরিবর্তন সংরক্ষণ কর':'প্রশ্ন যোগ কর'}</button>
    ${qf.editId?`<button class="btn ghost" data-qcancel style="width:100%">সম্পাদনা বাতিল</button>`:''}`;
  const pr=qf.parsed;
  const bulk=`<div class="field"><label for="qfBulk">প্রশ্নগুলো পেস্ট করুন</label>
    <textarea class="input area" id="qfBulk" data-qf="bulk" rows="12" placeholder="1. √49 = কত?&#10;ক) 5&#10;খ) 6&#10;গ) 7&#10;ঘ) 8&#10;উত্তর: গ&#10;ব্যাখ্যা: 7 × 7 = 49&#10;স্তর: সহজ&#10;&#10;2. পরের প্রশ্ন…">${esc(qf.bulk)}</textarea></div>
    <details class="fmt"><summary>লেখার নিয়ম</summary><p>প্রতিটি প্রশ্নের মাঝে একটি ফাঁকা লাইন রাখুন। প্রথমে প্রশ্ন, তারপর ক) খ) গ) ঘ) চারটি অপশন, তারপর "উত্তর: গ"। "ব্যাখ্যা:" ও "স্তর: সহজ/মধ্যম/কঠিন" ঐচ্ছিক; স্তর না দিলে মধ্যম ধরা হবে। ক. বা (ক) লিখলেও চলবে।</p></details>
    <button class="btn ghost" data-qparse style="width:100%">যাচাই কর</button>
    ${pr?`<div class="parse-res ${pr.errs.length?'bad':''}"><b>${pr.qs.length}টি প্রশ্ন ঠিক আছে</b>${pr.errs.length?` · ${pr.errs.length}টিতে সমস্যা`:''}
      ${pr.errs.length?`<ul>${pr.errs.slice(0,8).map(e=>`<li>${esc(e)}</li>`).join('')}${pr.errs.length>8?`<li>আরও ${pr.errs.length-8}টি…</li>`:''}</ul>`:''}</div>
      ${pr.qs.length?`<button class="btn" data-qbulksave style="width:100%" ${qf.busy?'disabled':''}>${qf.busy?esc(qf.msg||'যোগ হচ্ছে…'):`${pr.qs.length}টি প্রশ্ন যোগ কর`}</button>`:''}`:''}`;
  const shown=qf.showAll?mine.slice().reverse():mine.slice().reverse().slice(0,15);
  return `<section class="admin" aria-label="প্রশ্ন যোগ">
    <div><h2 class="display" style="font-size:22px">অধ্যায়ে প্রশ্ন যোগ কর</h2>
    <p class="muted" style="margin:4px 0 0;font-size:14px">যোগ করা প্রশ্ন সাথে সাথে অধ্যায়ের MCQ অনুশীলন ও রুটিনের পরীক্ষায় ব্যবহার হবে।</p></div>
    <div class="field"><label for="qfCh">অধ্যায় (${c.name} ${c.subj||''})</label>
      <select class="input" id="qfCh" data-qf="ch">${c.chapters.map((n,j)=>{const t=(((window.SOHOG_MCQ||{})[qf.course]||{})[String(j+1)]||[]).length+customQs(qf.course,j+1).length;return `<option value="${j+1}" ${j+1===+qf.ch?'selected':''}>${j+1}. ${esc(n)} (${t}টি প্রশ্ন)</option>`;}).join('')}</select></div>
    <div class="qcount"><span>আগে থেকে আছে: <b>${built.length}</b></span><span>আপনি যোগ করেছেন: <b>${mine.length}</b></span><span>মোট: <b>${built.length+mine.length}</b></span></div>
    <div class="seg" role="tablist"><label class="seg-opt"><input type="radio" name="qfmode" value="one" data-qfmode="one" ${qf.mode==='one'?'checked':''}><span>একটি করে</span></label>
      <label class="seg-opt"><input type="radio" name="qfmode" value="bulk" data-qfmode="bulk" ${qf.mode==='bulk'?'checked':''}><span>একসাথে অনেক</span></label></div>
    ${qf.mode==='bulk'?bulk:one}
    <div class="error" id="qfErr" role="alert">${esc(qf.err||'')}</div>
    ${mine.length?`<h3 style="margin:6px 0 0;font-size:16px">এই অধ্যায়ে আপনার যোগ করা প্রশ্ন</h3>
      <div class="list">${shown.map(x=>`<div class="qitem"><div style="flex:1;min-width:0"><b>${esc(x.q)}</b><br><span class="muted" style="font-size:13px">উত্তর: ${L[x.a]}) ${esc(x.o[x.a])} · ${x.lv}</span></div>
        <div class="qitem-act"><button class="link" data-qedit="${esc(x.id)}">সম্পাদনা</button><button class="link del" data-qdel="${esc(x.id)}">${qf.armed===x.id?'নিশ্চিত?':'মুছুন'}</button></div></div>`).join('')}</div>
      ${mine.length>15&&!qf.showAll?`<button class="link" data-qall style="align-self:center">সবগুলো দেখাও (${mine.length}টি)</button>`:''}`:''}
  </section>`;
}
async function qSaveOne(){
  const qf=qfInit(); qf.err='';
  const x={q:qf.q.trim(),o:qf.o.map(s=>s.trim()),a:qf.a,e:qf.e.trim(),lv:qf.lv};
  if(!x.q) qf.err='প্রশ্নের লেখা দিন।';
  else if(x.o.some(s=>!s)) qf.err='চারটি অপশনই পূরণ করুন।';
  else if(new Set(x.o).size<4) qf.err='দুটি অপশন একই রকম হয়েছে।';
  else if(x.a<0) qf.err='সঠিক উত্তরের অক্ষর (ক/খ/গ/ঘ) বেছে নিন।';
  if(qf.err){ render(); return; }
  qf.busy=true; render();
  try{ await saveQ(qf.course,qf.ch,x,qf.editId); const ed=!!qf.editId; Object.assign(qf,{q:'',o:['','','',''],a:-1,e:'',editId:null,busy:false}); render(); toast(ed?'প্রশ্ন সংরক্ষণ হয়েছে':'প্রশ্ন যোগ হয়েছে'); }
  catch(e){ qf.busy=false; qf.err=e&&e.code==='permission_denied'?'যোগ করার অনুমতি নেই। আবার অ্যাডমিন লগইন করুন।':'যোগ করা যায়নি। ইন্টারনেট সংযোগ দেখুন।'; render(); }
}
async function qSaveBulk(){
  const qf=qfInit(), list=(qf.parsed&&qf.parsed.qs)||[]; if(!list.length) return;
  qf.busy=true; qf.err=''; let done=0;
  try{
    for(const x of list){ qf.msg=`যোগ হচ্ছে… ${done}/${list.length}`; const b=app.querySelector('[data-qbulksave]'); if(b) b.textContent=qf.msg; await saveQ(qf.course,qf.ch,x); done++; }
    Object.assign(qf,{bulk:'',parsed:null,busy:false,msg:''}); render(); toast(`${done}টি প্রশ্ন যোগ হয়েছে`);
  }catch(e){ qf.busy=false; qf.err=`${done}টি যোগ হয়েছে, বাকিগুলো যোগ করা যায়নি। ইন্টারনেট দেখে আবার যাচাই করে যোগ করুন (আগেরগুলো বাদ দিয়ে)।`; render(); }
}
