/* ---------- রুটিন অনুযায়ী অনলাইন পরীক্ষা ---------- */
const examKey=e=>`${e.course}_${e.date}`;
const bankFor=(cid,no)=>(window.SOHOG_MCQ&&window.SOHOG_MCQ[cid]&&window.SOHOG_MCQ[cid][String(no)])||[];
const bankQ=(cid,ref)=>bankFor(cid,ref.ch).find(x=>x.n===ref.n);
function examChapters(e){ return e.kind==='friday'?e.chapters:(e.chapter?[e.chapter]:[]); }
function examPool(e){ return examChapters(e).flatMap(no=>bankFor(e.course,no).map(x=>({ch:no,n:x.n}))); }
const fmtLeft=ms=>{ const t=Math.max(0,Math.ceil(ms/1000)); return `${Math.floor(t/60)}:${String(t%60).padStart(2,'0')}`; };
const examLeft=run=>run.start+run.mins*60000-Date.now();

function examAction(e){
  const k=examKey(e), done=S.exams[k], today=todayISO();
  if(S.examRun&&!S.examRun.done&&S.examRun.key===k) return `<button class="btn" data-exgo="1">পরীক্ষা চলছে · ফিরে যাও (${fmtLeft(examLeft(S.examRun))} বাকি)</button>`;
  if(done) return `<div class="ex-done"><b>তোমার নম্বর: ${done.score}/${done.total}</b>${done.late?' <span class="muted">(দেরিতে)</span>':''}<button class="link" data-exview="${k}">উত্তর দেখো</button></div>`;
  if(e.date>today) return `<span class="muted" style="font-size:13.5px">পরীক্ষা খুলবে ${fmtD(parseD(e.date))} থেকে</span>`;
  const pool=examPool(e);
  if(!examChapters(e).length) return `<span class="muted" style="font-size:13.5px">এই দিনের জন্য কোনো অধ্যায় যুক্ত করা হয়নি, তাই অনলাইন পরীক্ষা নেই।</span>`;
  if(!pool.length) return `<span class="muted" style="font-size:13.5px">এই অধ্যায়ের প্রশ্ন এখনো যোগ হয়নি।</span>`;
  const n=Math.min(e.marks,pool.length);
  return `<button class="btn" data-exstart="${k}">${e.date===today?'পরীক্ষা দাও':'পরীক্ষা দাও (দেরিতে)'} · ${n}টি প্রশ্ন · ${e.mins} মিনিট</button>`;
}
function findExam(k){ return OFFER_IDS().flatMap(id=>examsFor(id)).find(e=>examKey(e)===k); }
function startExam(k){
  const e=findExam(k); if(!e||S.exams[k]) return;
  if(S.examRun&&!S.examRun.done){ toast('আগে চলমান পরীক্ষাটি শেষ করো'); return go('exam'); }
  const pool=examPool(e);
  for(let i=pool.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [pool[i],pool[j]]=[pool[j],pool[i]]; }
  const qs=pool.slice(0,Math.min(e.marks,pool.length));
  S.examRun={key:k,course:e.course,date:e.date,kind:e.kind,title:(e.kind==='friday'?'সাপ্তাহিক পরীক্ষা':'দৈনিক পরীক্ষা')+' · '+fmtD(parseD(e.date)),
    mins:e.mins,total:qs.length,qs,ans:{},start:Date.now(),late:e.date<todayISO(),done:false};
  persist(); go('exam');
}
function submitExam(auto){
  const run=S.examRun; if(!run||run.done) return;
  let score=0; run.qs.forEach((ref,i)=>{ const q=bankQ(run.course,ref); if(q&&run.ans[i]===q.a) score++; });
  run.done=true; run.score=score; run.end=Date.now();
  S.exams[run.key]={score,total:run.total,at:run.end,late:run.late,qs:run.qs,ans:run.ans,course:run.course,title:run.title};
  S.examView=run.key; S.examRun=null; S.exSubmitArmed=false; persist();
  go('examResult'); toast(auto?'সময় শেষ, খাতা জমা হয়েছে':'খাতা জমা হয়েছে');
}
function vExam(){
  const run=S.examRun;
  if(!run) return vRoutine();
  const answered=Object.keys(run.ans).length;
  return `<div class="screen">
    <div class="exam-bar" role="timer" aria-live="off">
      <div style="min-width:0"><b>${run.title}</b><span>${run.total} নম্বর · প্রতিটি প্রশ্নে 1</span></div>
      <span class="timer" id="examTimer">${fmtLeft(examLeft(run))}</span>
    </div>
    ${run.qs.map((ref,i)=>{const q=bankQ(run.course,ref); if(!q) return ''; return `<fieldset class="eq"><legend>${i+1}. ${esc(q.q)}</legend>
      ${q.o.map((o,k)=>`<label class="eopt"><input type="radio" name="eq${i}" value="${k}" data-eq="${i}" ${run.ans[i]===k?'checked':''}><span class="k">${'কখগঘ'[k]}</span><span>${esc(o)}</span></label>`).join('')}
    </fieldset>`;}).join('')}
    <div class="error" role="status" id="exHint">${run.total-answered>0?`${run.total-answered}টি প্রশ্নের উত্তর দেওয়া বাকি`:''}</div>
    <button class="btn" data-exsubmit style="width:100%">${S.exSubmitArmed?'নিশ্চিত? আবার চাপলে জমা হবে':`খাতা জমা দাও (${answered}/${run.total})`}</button>
  </div>`;
}
function vExamResult(){
  const r=S.exams[S.examView]; if(!r) return vRoutine();
  const pct=Math.round(r.score/r.total*100);
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="routine" aria-label="রুটিনে ফিরে যাও">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>ফলাফল</h1><span style="width:44px"></span></div>
    <div class="q-card" style="align-items:center;text-align:center">
      <span class="muted">${r.title}${r.late?' · দেরিতে দেওয়া':''}</span>
      <b style="font-size:44px;line-height:1.1;color:${pct>=60?'var(--good)':'var(--amber)'}">${r.score}/${r.total}</b>
      <span>${pct>=80?'চমৎকার!':pct>=60?'ভালো হয়েছে!':pct>=40?'আরও অনুশীলন দরকার':'অধ্যায়টি আবার পড়ো'}</span>
    </div>
    <h2 style="margin:0;font-size:17px">উত্তরপত্র</h2>
    ${r.qs.map((ref,i)=>{const q=bankQ(r.course,ref); if(!q) return ''; const my=r.ans[i];
      return `<div class="q-card" style="gap:8px"><p style="margin:0;font-weight:600">${i+1}. ${esc(q.q)}</p>
      ${q.o.map((o,k)=>`<div class="opt ${k===q.a?'right':k===my?'wrong':''}" style="cursor:default"><span class="k">${'কখগঘ'[k]}</span>${esc(o)}</div>`).join('')}
      <div class="feedback ${my===q.a?'ok':'no'}"><b>${my===undefined?'উত্তর দেওয়া হয়নি':my===q.a?'সঠিক':'ভুল'}</b> · ${esc(q.e)}</div></div>`;}).join('')}
    <button class="btn ghost" data-go="routine">রুটিনে ফিরে যাও</button>
  </div>`;
}
function todayExamBanner(){
  if(RSTATE!=='ready') return '';
  if(S.examRun&&!S.examRun.done) return `<button class="exam-banner" data-exgo="1">${svg('calendar')}<span><b>পরীক্ষা চলছে</b><br>${S.examRun.title} · ${fmtLeft(examLeft(S.examRun))} বাকি</span></button>`;
  const t=todayISO(), e=OFFER_IDS().flatMap(id=>examsFor(id)).find(x=>x.date===t&&!S.exams[examKey(x)]&&examPool(x).length);
  return e?`<button class="exam-banner" data-exstart="${examKey(e)}">${svg('calendar')}<span><b>আজ ${e.kind==='friday'?'সাপ্তাহিক':'দৈনিক'} পরীক্ষা আছে</b><br>${COURSES[e.course].name} ${COURSES[e.course].subj} · ${e.marks} নম্বর · ${e.mins} মিনিট</span></button>`:'';
}
setInterval(()=>{
  const run=S.examRun; if(!run||run.done) return;
  if(examLeft(run)<=0){ submitExam(true); return; }
  const el=document.getElementById('examTimer'); if(el){ el.textContent=fmtLeft(examLeft(run)); el.classList.toggle('low',examLeft(run)<60000); }
},1000);
