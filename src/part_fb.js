let ADMIN_USER=null;
setTimeout(function(){
  const timer=setTimeout(()=>{ if(RSTATE==='loading'){ RSTATE='error'; softRender(); } },15000);
  try{
    if(!(window.SohogDB&&window.SohogDB.init(window.SOHOG_FIREBASE))){ clearTimeout(timer); RSTATE='off'; softRender(); return; }
    DB=window.SohogDB;
    DB.onAuth(async u=>{
      ADMIN_USER=u;
      if(!u){ CAN_EDIT=false; acctSignedOut(); return; }
      // শিক্ষার্থীরাও এখন লগইন করে, তাই অ্যাডমিন কিনা সার্ভারের Rules দিয়ে যাচাই (admin/check শুধু অ্যাডমিন পড়তে পারেন)।
      // ইন্টারনেট না থাকলে আগের বার যে ইমেইল অ্যাডমিন ছিল সেটি ধরে নেওয়া হয়।
      const adm=AUTHBUSY&&S.view!=='adminLogin'?false:await DB.checkAdmin();
      CAN_EDIT=adm===true||(adm===null&&!!S.adminEmail&&S.adminEmail===u.email);
      if(CAN_EDIT){
        if(S.adminEmail!==u.email){ S.adminEmail=u.email; persist(); }
        adminWatchAll();
        if(S.view==='adminLogin'){ go('admin'); toast('অ্যাডমিন হিসেবে লগইন হয়েছে'); return; }
        softRender(); return;
      }
      if(S.view==='adminLogin'&&!AUTHBUSY){ S.adminDenied=true; S.signing=false; DB.signOut(); render(); return; }
      acctSignedIn(u);
    });
    DB.collection('routines').orderBy('date').onSnapshot(snap=>{
      clearTimeout(timer);
      ROUT=snap.docs.map(d=>Object.assign({id:d.id},d.data()));
      RSTATE='ready'; softRender(); sendPendingResults(); watchResults(true); sendPendingReports(); refreshPays(); scheduleExamNotifs();
    },()=>{ clearTimeout(timer); RSTATE='error'; softRender(); });
    DB.collection('syllabus').onSnapshot(snap=>{
      const m={}; snap.docs.forEach(d=>{ m[d.id]=Object.assign({id:d.id},d.data()); }); SYL=m; SYL_READY=true; scheduleExamNotifs();
      if(S.sf&&!S.sf.dirty) S.sf.vals=null; if(S.cf&&!S.cf.dirty) S.cf.vals=null; softRender();
    },()=>{});
  }catch(e){ clearTimeout(timer); RSTATE='off'; softRender(); }
},0);
function vAdminLogin(){
  return `<div class="screen">
    <div class="topbar"><button class="iconbtn" data-go="profile" aria-label="ফিরে যান">${svg('back','width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"')}</button><h1>অ্যাডমিন লগইন</h1><span style="width:44px"></span></div>
    <p class="muted" style="margin:0">এই অংশ শুধু একাডেমির পরিচালকের জন্য। শিক্ষার্থীরা নিজেদের অ্যাকাউন্ট দিয়ে লগইন করবে।</p>
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
