/* ---------- অনুশীলনী (যেমন 2.1, 3.4) ---------- */
const exList=(cid,no)=>((COURSES[cid]&&COURSES[cid].exs)||{})[no]||[];
const exCh=ex=>+String(ex).split('.')[0];
const exNoteId=(cid,ex)=>`ex_${cid}_${String(ex).replace('.','_')}`;
const exDom=ex=>String(ex).replace('.','-');
function exDoc(cid,ex){ const r=SYL[exNoteId(cid,ex)]; return r&&canSee(r)?r:null; }
function exBank(cid,ex){ return bankFor(cid,exCh(ex)).filter(q=>q.ex===ex); }
function exercisesSection(cid,i){
  const list=exList(cid,i+1); if(!list.length) return '';
  return `<section class="ex-box" aria-label="অনুশীলনী"><h2 style="margin:0;font-size:18px">অনুশীলনী</h2>
    <div class="ex-grid">${list.map(ex=>{ const r=exDoc(cid,ex), nq=exBank(cid,ex).length, d=!!S.done[`${cid}:ex:${ex}`];
      return `<button class="ex-tile ${d?'done':''}" data-openex="${ex}"><b>${ex}</b><span>${[r?'নোট':'',nq?nq+' MCQ':''].filter(Boolean).join(' · ')||'শিগগিরই'}</span>${d?'<i>পড়া শেষ</i>':''}</button>`; }).join('')}</div>
  </section>`;
}
function mcqBox(cid,part,b,label){
  if(!b||!b.length) return '';
  const ne=b.filter(x=>x.lv==='সহজ').length, nm=b.filter(x=>x.lv==='মধ্যম').length;
  const card=(lv,desc)=>{const id=`mcq_${cid}_${part}_${lv}`, r=S.results[id];
    return `<button class="mcq-btn" data-quiz="${id}"><b>${MCQ_LV[lv]}</b><span>${desc}</span><span class="mcq-best">${r?`সেরা: ${r.best}/${r.total}`:'এখনো দেওয়া হয়নি'}</span></button>`;};
  return `<section class="mcq-box" aria-label="MCQ অনুশীলন">
    <div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap"><h2 style="margin:0;font-size:18px">${label||'MCQ অনুশীলন'}</h2><span class="muted" style="font-size:13px">মোট ${b.length}টি প্রশ্ন</span></div>
    <p class="muted" style="margin:0;font-size:13.5px">প্রতিবার সর্বোচ্চ ${MCQ_N}টি প্রশ্ন এলোমেলোভাবে আসবে। উত্তর দিলেই সঠিক উত্তর ও ব্যাখ্যা দেখাবে।</p>
    <div class="mcq-grid">${card('easy',`${ne}টি থেকে`)}${card('mid',`${nm}টি থেকে`)}${card('mix','সব প্রশ্ন')}</div>
  </section>`;
}
function vExercise(){
  const cid=S.course||'c10', ex=S.exKey, no=exCh(ex), c=COURSES[cid], list=exList(cid,no), idx=list.indexOf(ex);
  const r=exDoc(cid,ex), link=r?safeLink(r.link):'', k=`${cid}:ex:${ex}`, d=!!S.done[k], b=exBank(cid,ex);
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-opench="${no-1}" aria-label="অধ্যায়ে ফিরে যান">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>অনুশীলনী ${ex}</h1><span style="width:44px"></span></div>
    <div><span class="offer-tag">${c.name} · ${c.subj||''} · অধ্যায় ${no}</span>
      <h2 class="display" style="font-size:24px;margin-top:8px;overflow-wrap:anywhere">${esc(r&&r.title?r.title:'অনুশীলনী '+ex)}</h2>
      <span class="muted">${esc(chTitle(cid,no-1))}</span></div>
    ${r?`<section class="sylcard">
        ${!isLive(r)?`<span class="sched">শিক্ষার্থীরা দেখবে ${fmtDT(r.publishAt)} থেকে</span>`:''}
        ${r.note?`<p class="syl-text">${esc(r.note)}</p>`:''}
        ${link?`<a class="btn ghost linkbtn" href="${esc(link)}" target="_blank" rel="noopener">${svg('play')}<span>ভিডিও / লিংক খুলুন</span></a>`:''}
        <span class="muted" style="font-size:12.5px">প্রকাশ: ${fmtDT(r.publishAt||r.updatedAt)}</span>
      </section>`:`<div class="empty">এই অনুশীলনীর নোট এখনো প্রকাশ হয়নি।</div>`}
    ${b.length?mcqBox(cid,exDom(ex),b,`অনুশীলনী ${ex}-এর MCQ`):`<div class="empty" style="padding:12px">এই অনুশীলনীর MCQ এখনো যোগ হয়নি।</div>`}
    <button class="btn ${d?'ghost':''}" data-exdone style="width:100%">${d?'পড়া শেষ ✓ (আবার চাপলে বাতিল)':'পড়া শেষ চিহ্নিত করো'}</button>
    <div style="display:flex;gap:10px">
      ${idx>0?`<button class="btn ghost" style="flex:1" data-openex="${list[idx-1]}">অনুশীলনী ${list[idx-1]}</button>`:''}
      ${idx<list.length-1?`<button class="btn ghost" style="flex:1" data-openex="${list[idx+1]}">অনুশীলনী ${list[idx+1]}</button>`:''}
    </div>
  </div>`;
}
// রুটিন ও পরীক্ষা: একটি দিনে পুরো অধ্যায় বা নির্দিষ্ট অনুশীলনী
function unitPool(cid,u){ return (u.ex?exBank(cid,u.ex):bankFor(cid,u.ch)).map(x=>({ch:u.ch,n:x.n})); }
function unitLabel(cid,u){ return u.ex?`অনুশীলনী ${u.ex}`:`অধ্যায় ${u.ch}`; }
function unitOptions(cid,sel){
  return COURSES[cid].chapters.map((c,j)=>{ const no=j+1, nb=bankFor(cid,no).length;
    return `<option value="${no}" ${String(no)===sel?'selected':''}>${no}. ${esc(c)}${nb?' ('+nb+' MCQ)':''}</option>`+
      exList(cid,no).map(ex=>{ const n=exBank(cid,ex).length; return `<option value="${ex}" ${ex===sel?'selected':''}>   ↳ অনুশীলনী ${ex}${n?' ('+n+' MCQ)':''}</option>`; }).join('');
  }).join('');
}
