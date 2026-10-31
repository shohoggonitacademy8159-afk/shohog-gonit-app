/* ---------- অধ্যায়ভিত্তিক নোট (অ্যাডমিন প্রকাশ করে, এক্সপ্লোরে দেখা যায়) ---------- */
const chId=(cid,i)=>`ch_${cid}_${pad2(i+1)}`;
function chDoc(cid,i){ const r=SYL[chId(cid,i)]; return r&&canSee(r)?r:null; }
function chTitle(cid,i){ const r=SYL[chId(cid,i)]; return (r&&r.title)||COURSES[cid].chapters[i]; }
const safeLink=u=>/^https:\/\/[^\s"'<>]+$/i.test(String(u||'').trim())?String(u).trim():'';

function vChapters(){
  const cid=S.course||'c10', c=COURSES[cid];
  const ready=c.chapters.filter((_,i)=>chDoc(cid,i)).length;
  const done=c.chapters.filter((_,i)=>S.done[cid+':'+i]).length;
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="${S.chFrom||'play'}" aria-label="ফিরে যান">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>${c.name} ${c.subj||''}</h1><span style="width:44px"></span></div>
    <div class="ch-head t-${c.t}">
      <span class="ch-art">${art(c.art)}</span>
      <div style="min-width:0"><b style="font-size:18px">${c.name}${c.sub?' ('+c.sub+')':''}</b><br><span>${c.subj||''} · ${bn(c.chapters.length)}টি অধ্যায়</span><br>
      <span class="muted" style="font-size:13px">${bn(ready)}টিতে নোট আছে · ${bn(done)}টি পড়া শেষ</span></div>
    </div>
    ${RSTATE==='loading'?'<div class="empty">অধ্যায়ের নোট আনা হচ্ছে…</div>':''}
    <div class="list" role="list">
      ${c.chapters.map((_,i)=>{const r=chDoc(cid,i), d=!!S.done[cid+':'+i];
        return `<button class="item" role="listitem" data-opench="${i}">
        <span class="num">${bn(i+1)}</span>
        <span class="t">${esc(chTitle(cid,i))}<br><span class="s">${r?(r.link?'নোট ও ভিডিও/লিংক আছে':'নোট আছে'):'নোট শিগগিরই আসবে'}</span></span>
        <span class="pill ${d?'done':'todo'}">${d?'পড়া শেষ':'পড়ুন'}</span></button>`}).join('')}
    </div>
  </div>`;
}
function vChapter(){
  const cid=S.course||'c10', i=S.chIdx||0, c=COURSES[cid], r=chDoc(cid,i), k=cid+':'+i, d=!!S.done[k];
  const link=r?safeLink(r.link):'';
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="chapters" aria-label="অধ্যায়ের তালিকায় ফিরে যান">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>অধ্যায় ${bn(i+1)}</h1><span style="width:44px"></span></div>
    <div><span class="offer-tag">${c.name} · ${c.subj||''}</span>
      <h2 class="display" style="font-size:26px;margin-top:8px;overflow-wrap:anywhere">${esc(chTitle(cid,i))}</h2></div>
    ${r?`<section class="sylcard">
        ${r.pending||!isLive(r)?`<span class="sched">শিক্ষার্থীরা দেখবে ${fmtDT(r.publishAt)} থেকে</span>`:''}
        ${r.note?`<p class="syl-text">${esc(r.note)}</p>`:''}
        ${link?`<a class="btn ghost linkbtn" href="${esc(link)}" target="_blank" rel="noopener">${svg('play')}<span>ভিডিও / লিংক খুলুন</span></a>`:''}
        <span class="muted" style="font-size:12.5px">প্রকাশ: ${fmtDT(r.publishAt||r.updatedAt)}</span>
      </section>`
      :`<div class="empty">এই অধ্যায়ের নোট এখনো প্রকাশ হয়নি।<br>প্রকাশ হলে এখানেই দেখা যাবে।</div>`}
    <button class="btn ${d?'ghost':''}" data-chdone style="width:100%">${d?'পড়া শেষ ✓ (আবার চাপলে বাতিল)':'পড়া শেষ চিহ্নিত করো'}</button>
    <div style="display:flex;gap:10px">
      ${i>0?`<button class="btn ghost" style="flex:1" data-opench="${i-1}">আগের অধ্যায়</button>`:''}
      ${i<c.chapters.length-1?`<button class="btn ghost" style="flex:1" data-opench="${i+1}">পরের অধ্যায়</button>`:''}
    </div>
  </div>`;
}

const CH_COURSES=()=>Object.keys(COURSES).filter(k=>COURSES[k].content);
function cfInit(){
  if(!S.cf) S.cf={course:CH_COURSES()[0], no:0, when:'now', at:'', vals:null, armed:false, dirty:false};
  if(!S.cf.vals){ const r=SYL[chId(S.cf.course,S.cf.no)];
    S.cf.vals={title:r&&r.title?String(r.title):COURSES[S.cf.course].chapters[S.cf.no], note:r?String(r.note||''):'', link:r?String(r.link||''):''}; }
  return S.cf;
}
function chapterPanel(){
  const cf=cfInit(), c=COURSES[cf.course], r=SYL[chId(cf.course,cf.no)];
  const filled=c.chapters.filter((_,i)=>SYL[chId(cf.course,i)]).length;
  return `<section class="admin" aria-label="অধ্যায়ের নোট প্রকাশ">
    <div><h2 class="display" style="font-size:22px">অধ্যায়ের নোট প্রকাশ কর</h2>
    <p class="muted" style="margin:4px 0 0;font-size:14px">${c.name} (${c.sub}) ${c.subj}: ${bn(c.chapters.length)}টি অধ্যায়, এর মধ্যে ${bn(filled)}টিতে নোট দেওয়া হয়েছে। শিক্ষার্থীরা এক্সপ্লোর → মাধ্যমিক স্তর থেকে দেখবে।</p></div>
    <div class="field"><label for="cfNo">অধ্যায়</label>
      <select class="input" id="cfNo" data-cf="no">${c.chapters.map((_,i)=>`<option value="${i}" ${i===cf.no?'selected':''}>${bn(i+1)}. ${esc(chTitle(cf.course,i))}${SYL[chId(cf.course,i)]?' ✓':''}</option>`).join('')}</select></div>
    <div class="field"><label for="cfTitle">অধ্যায়ের নাম</label>
      <input class="input" id="cfTitle" data-cfv="title" maxlength="80" value="${esc(cf.vals.title)}"></div>
    <div class="field"><label for="cfNote">নোট / পড়ার নির্দেশনা</label>
      <textarea class="input area" id="cfNote" data-cfv="note" maxlength="5000" rows="8" placeholder="যেমন: মূল সূত্র, গুরুত্বপূর্ণ উদাহরণ, কোন অনুশীলনী করতে হবে">${esc(cf.vals.note)}</textarea></div>
    <div class="field"><label for="cfLink">ভিডিও বা ফাইলের লিংক (ঐচ্ছিক)</label>
      <input class="input" id="cfLink" data-cfv="link" type="url" inputmode="url" placeholder="https://youtube.com/..." value="${esc(cf.vals.link)}"></div>
    ${whenUI('cf',cf)}
    <div class="error" id="cfErr" role="alert"></div>
    <button class="btn" data-cpublish style="width:100%" ${S.cpublishing?'disabled':''}>${S.cpublishing?'প্রকাশ হচ্ছে…':'অধ্যায়ের নোট প্রকাশ কর'}</button>
    ${r?`<div class="cur"><b>এই অধ্যায়ে প্রকাশিত:</b> ${isLive(r)?'শিক্ষার্থীরা দেখছে':'নির্ধারিত '+fmtDT(r.publishAt)}
      <button class="link del" data-cdel="1">${cf.armed?'নিশ্চিত? আবার চাপুন':'এই অধ্যায়ের নোট মুছুন'}</button></div>`:''}
  </section>
  <button class="btn ghost" data-chlist="${cf.course}">শিক্ষার্থীরা যেভাবে দেখবে</button>`;
}
async function publishChapter(){
  const cf=cfInit(), el=()=>document.getElementById('cfErr'), w=whenISO(cf);
  const title=cf.vals.title.trim(), note=cf.vals.note.trim(), link=cf.vals.link.trim();
  if(!note&&!link){ el().textContent='নোট অথবা লিংক, অন্তত একটি দিন।'; return; }
  if(link&&!safeLink(link)){ el().textContent='লিংকটি https:// দিয়ে শুরু হতে হবে।'; return; }
  if(w.err){ el().textContent=w.err; return; }
  S.cpublishing=true; render();
  try{
    await DB.collection('syllabus').doc(chId(cf.course,cf.no)).set({type:'chapter',course:cf.course,no:cf.no+1,title:title||COURSES[cf.course].chapters[cf.no],note,link,publishAt:w.iso,updatedAt:new Date().toISOString()});
    S.cpublishing=false; cf.vals=null; cf.dirty=false; const later=cf.when==='later'; cf.when='now'; cf.at=''; render();
    toast(later?'নোট নির্ধারিত সময়ে প্রকাশ হবে':'অধ্যায়ের নোট প্রকাশ হয়েছে');
  }catch(e){
    S.cpublishing=false; render();
    el().textContent=e&&e.code==='permission_denied'?'প্রকাশের অনুমতি নেই। Firebase-এর Rules-এ অ্যাডমিন ইমেইল মিলিয়ে দেখুন।':'প্রকাশ করা যায়নি। ইন্টারনেট সংযোগ দেখে আবার চেষ্টা করুন।';
  }
}
