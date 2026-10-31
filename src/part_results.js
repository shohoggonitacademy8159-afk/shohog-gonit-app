/* ---------- পরীক্ষার ফলাফল অ্যাডমিনের কাছে (Firebase: results সংগ্রহ) ---------- */
let RES={}, resUnsub=null;
function watchResults(on){
  if(on&&DB&&!resUnsub){
    resUnsub=DB.collection('results').onSnapshot(snap=>{ const m={}; snap.docs.forEach(d=>{ m[d.id]=Object.assign({id:d.id},d.data()); }); RES=m; softRender(); },()=>{ RES={}; });
  }
  if(!on&&resUnsub){ try{ resUnsub(); }catch(e){} resUnsub=null; RES={}; }
}
function sendResult(k){
  const r=S.exams[k]; if(!r||r.sent||!DB||!S.student) return;
  const parts=k.split('_'), course=parts[0], date=parts.slice(1).join('_');
  DB.collection('results').doc(`${k}_${S.dev}`).set({course,date,kind:r.kind||(parseD(date).getDay()===5?'friday':'daily'),examKey:k,
    name:S.student.name,roll:S.student.roll||'',score:r.score,total:r.total,late:!!r.late,at:new Date(r.at).toISOString(),device:S.dev})
    .then(()=>{ r.sent=true; persist(); },e=>{ if(e&&e.code==='permission_denied'){ r.sent=true; r.sendErr=true; persist(); } });
}
function sendPendingResults(){ Object.keys(S.exams||{}).forEach(sendResult); }

function vStudent(){
  const st=S.student||{name:'',roll:''};
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="${S.pendingExam?'routine':'profile'}" aria-label="ফিরে যাও">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>তোমার তথ্য</h1><span style="width:44px"></span></div>
    <p class="muted" style="margin:0">পরীক্ষার ফলাফল এই নামে শিক্ষকের কাছে যাবে। একবার দিলেই হবে, পরে "আরো" থেকে বদলানো যাবে।</p>
    <form id="stuForm" novalidate style="display:flex;flex-direction:column;gap:14px">
      <div class="field"><label for="stName">তোমার নাম</label><input class="input" id="stName" maxlength="60" autocomplete="name" value="${esc(st.name)}" placeholder="যেমন: রাফি আহমেদ"></div>
      <div class="field"><label for="stRoll">রোল বা মোবাইল নম্বর (ঐচ্ছিক)</label><input class="input" id="stRoll" maxlength="20" inputmode="numeric" value="${esc(st.roll||'')}" placeholder="যেমন: 12"></div>
      <div class="error" id="stErr" role="alert"></div>
      <button class="btn" type="submit">${S.pendingExam?'সংরক্ষণ করে পরীক্ষা শুরু করো':'সংরক্ষণ করো'}</button>
    </form>
  </div>`;
}

function resultsPanel(){
  const all=OFFER_IDS().flatMap(id=>examsFor(id)), keys=new Set(all.map(examKey));
  Object.values(RES).forEach(r=>{ if(r.examKey&&!keys.has(r.examKey)){ keys.add(r.examKey); all.push({course:r.course,date:r.date,kind:r.kind,marks:r.total}); } });
  const list=all.sort((a,b)=>a.date<b.date?1:-1);
  const cnt=k=>Object.values(RES).filter(r=>r.examKey===k).length;
  const today=todayISO();
  if(!S.resKey||!keys.has(S.resKey)){ const f=list.find(e=>e.date<=today&&cnt(examKey(e)))||list.find(e=>e.date<=today)||list[0]; S.resKey=f?examKey(f):''; }
  if(!list.length) return `<section class="admin"><div class="empty">এখনো কোনো পরীক্ষার রুটিন নেই। রুটিন প্রকাশ করলে এখানে প্রতিটি পরীক্ষার ফলাফল দেখা যাবে।</div></section>`;
  const rows=Object.values(RES).filter(r=>r.examKey===S.resKey).sort((a,b)=>b.score-a.score||String(a.at).localeCompare(String(b.at)));
  const n=rows.length, avg=n?(rows.reduce((s,r)=>s+r.score,0)/n):0, top=n?rows[0].score:0, tot=n?rows[0].total:0;
  let rank=0, prev=null;
  return `<section class="admin" aria-label="ফলাফল">
    <div><h2 class="display" style="font-size:22px">পরীক্ষার ফলাফল</h2>
    <p class="muted" style="margin:4px 0 0;font-size:14px">শিক্ষার্থী খাতা জমা দিলেই ফলাফল এখানে চলে আসে। ইন্টারনেট না থাকলে সংযোগ পাওয়ার পর আসবে।</p></div>
    <div class="field"><label for="resSel">পরীক্ষা</label>
      <select class="input" id="resSel" data-res="1">${list.map(e=>{const k=examKey(e);return `<option value="${k}" ${k===S.resKey?'selected':''}>${fmtD(parseD(e.date))} · ${e.kind==='friday'?'সাপ্তাহিক':'দৈনিক'} · ${COURSES[e.course]?COURSES[e.course].name:''} (${cnt(k)} জন)</option>`;}).join('')}</select></div>
    <div class="stats">
      <div class="stat"><b>${n}</b><span>জন জমা দিয়েছে</span></div>
      <div class="stat"><b>${n?avg.toFixed(1):'-'}</b><span>গড় নম্বর</span></div>
      <div class="stat"><b>${n?top+'/'+tot:'-'}</b><span>সর্বোচ্চ</span></div>
    </div>
    ${n?`<div class="res-wrap"><table class="res-table"><thead><tr><th>মেধা</th><th>নাম</th><th>রোল</th><th>নম্বর</th><th>জমা</th><th></th></tr></thead><tbody>
      ${rows.map((r,i)=>{ if(r.score!==prev){ rank=i+1; prev=r.score; } const d=new Date(r.at);
        return `<tr><td>${rank}</td><td class="nm">${esc(r.name)}${r.late?' <span class="late">দেরিতে</span>':''}</td><td>${esc(r.roll||'-')}</td><td><b>${r.score}/${r.total}</b></td><td class="tm">${isNaN(d)?'':pad2(d.getHours())+':'+pad2(d.getMinutes())}</td>
        <td><button class="link del" data-resdel="${esc(r.id)}">${S.resArmed===r.id?'নিশ্চিত?':'মুছুন'}</button></td></tr>`; }).join('')}
    </tbody></table></div>`:`<div class="empty">এই পরীক্ষার কোনো ফলাফল এখনো আসেনি।</div>`}
  </section>`;
}
