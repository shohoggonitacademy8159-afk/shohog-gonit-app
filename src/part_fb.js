let ADMIN_USER=null;
setTimeout(function(){
  const timer=setTimeout(()=>{ if(RSTATE==='loading'){ RSTATE='error'; softRender(); } },15000);
  try{
    if(!(window.SohogDB&&window.SohogDB.init(window.SOHOG_FIREBASE))){ clearTimeout(timer); RSTATE='off'; softRender(); return; }
    DB=window.SohogDB;
    DB.onAuth(u=>{
      ADMIN_USER=u;
      // অ্যাপে নতুন অ্যাকাউন্ট খোলার কোনো ব্যবস্থা নেই, তাই লগইন করা মানেই অ্যাডমিন।
      // প্রকাশের আসল অনুমতি Firebase-এর Rules ঠিক করে (সেখানে অ্যাডমিনের ইমেইল আছে)।
      CAN_EDIT=!!u;
      watchResults(CAN_EDIT);
      if(S.view==='adminLogin'&&CAN_EDIT){ go('admin'); toast('অ্যাডমিন হিসেবে লগইন হয়েছে'); return; }
      softRender();
    });
    DB.collection('routines').orderBy('date').onSnapshot(snap=>{
      clearTimeout(timer);
      ROUT=snap.docs.map(d=>Object.assign({id:d.id},d.data()));
      RSTATE='ready'; softRender(); sendPendingResults();
    },()=>{ clearTimeout(timer); RSTATE='error'; softRender(); });
    DB.collection('syllabus').onSnapshot(snap=>{
      const m={}; snap.docs.forEach(d=>{ m[d.id]=Object.assign({id:d.id},d.data()); }); SYL=m;
      if(S.sf&&!S.sf.dirty) S.sf.vals=null; if(S.cf&&!S.cf.dirty) S.cf.vals=null; softRender();
    },()=>{});
  }catch(e){ clearTimeout(timer); RSTATE='off'; softRender(); }
},0);
function vAdminLogin(){
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="profile" aria-label="ফিরে যান">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>অ্যাডমিন লগইন</h1><span style="width:44px"></span></div>
    <p class="muted" style="margin:0">এই অংশ শুধু একাডেমির পরিচালকের জন্য। শিক্ষার্থীদের লগইন লাগবে না।</p>
    ${RSTATE==='off'?`<div class="empty">অ্যাপটি এখনো সার্ভারের সাথে যুক্ত করা হয়নি।</div>`:''}
    <form id="adminForm" novalidate style="display:flex;flex-direction:column;gap:14px">
      <div class="field"><label for="adEmail">ইমেইল</label>
        <input class="input" id="adEmail" type="email" autocomplete="username" placeholder="অ্যাডমিনের ইমেইল লিখুন"></div>
      <div class="field"><label for="adPass">পাসওয়ার্ড</label>
        <input class="input" id="adPass" type="password" autocomplete="current-password"></div>
      <div class="error" id="adErr" role="alert">${S.adminDenied?'এই অ্যাকাউন্টটি অ্যাডমিন নয়, অথবা ইন্টারনেট সংযোগ নেই।':''}</div>
      <button class="btn" type="submit" ${S.signing?'disabled':''}>${S.signing?'যাচাই হচ্ছে…':'লগইন করুন'}</button>
    </form>
  </div>`;
}
