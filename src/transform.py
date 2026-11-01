#!/usr/bin/env python3
"""Turns the claude.ai artifact page (src/app-source.html) into the installable app page (www/index.html)."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'src/app-source.html').read_text(encoding='utf-8')

def rep(a, b, count=1):
    global s
    assert a in s, 'missing: ' + a[:90]
    s = s.replace(a, b, count)

rep('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

# শিক্ষার্থীদের জন্য লগইন নেই: সরাসরি হোম
rep("view: saved.user ? 'home' : 'login',", "view: 'home',")
rep("""    <div class="profile-card"><span class="avatar">স</span><div style="min-width:0"><b style="font-size:18px">শিক্ষার্থী</b><br><span class="muted" style="word-break:break-all">${esc(bn(id))}</span></div></div>""",
    "")
rep("""      <button class="item" data-logout><span class="ic c-violet">${svg('back')}</span><span class="t">লগ আউট</span></button>""",
    """      ${CAN_EDIT?`<button class="item" data-adminout><span class="ic c-violet">${svg('back')}</span><span class="t">অ্যাডমিন লগ আউট</span></button>`
        :`<button class="item" data-go="adminLogin"><span class="ic c-violet">${svg('user')}</span><span class="t">অ্যাডমিন লগইন<br><span class="s">শুধু একাডেমির পরিচালকের জন্য</span></span></button>`}""")

# claude.ai ডেটা স্তরের জায়গায় Firebase
start = s.index("(async()=>{\n  const timer=setTimeout(()=>{ if(RSTATE==='loading'){ RSTATE='off'; softRender(); } },10000);")
end = s.index("})();", start) + len("})();")
s = s[:start] + "/*__FB__*/" + s[end:]

rep("""`<div class="empty">রুটিন দেখতে claude.ai-তে সাইন ইন করে অ্যাপটি খুলুন।</div>`""",
    """`<div class="empty">অ্যাপটি এখনো সার্ভারের সাথে যুক্ত করা হয়নি।</div>`""")
rep("""`<div class="empty">রুটিন আনা যায়নি। কিছুক্ষণ পরে অ্যাপটি আবার খুলুন।</div>`""",
    """`<div class="empty">রুটিন আনা যায়নি। ইন্টারনেট চালু করে অ্যাপটি আবার খুলুন।</div>`""")
rep("'প্রকাশের অনুমতি নেই। নিজের claude.ai অ্যাকাউন্টে ঢুকে খুলুন।'", "'প্রকাশের অনুমতি নেই। আবার অ্যাডমিন লগইন করুন।'")
rep("'রুটিন প্রকাশের অনুমতি নেই। অ্যাপের মালিক বা এডিটর হিসেবে খুলুন।'", "'রুটিন প্রকাশের অনুমতি নেই। আবার অ্যাডমিন লগইন করুন।'")
rep("ফোন বা কম্পিউটার, যেখান থেকেই নিজের claude.ai অ্যাকাউন্টে ঢুকে অ্যাপটি খুলবেন, এখান থেকে প্রকাশ করতে পারবেন। প্রকাশ করার সাথে সাথে শিক্ষার্থীদের অ্যাপে চলে যায়।",
    "ফোনের অ্যাপ বা কম্পিউটারের ওয়েব সংস্করণ, যেখান থেকেই অ্যাডমিন লগইন করবেন, এখান থেকে প্রকাশ করতে পারবেন। প্রকাশ করার সাথে সাথে শিক্ষার্থীদের অ্যাপে চলে যায়।")
rep("${RSTATE==='loading'?'যাচাই হচ্ছে…':'এই পাতা শুধু অ্যাপের মালিক দেখতে পারেন।'}",
    "এই পাতা শুধু অ্যাডমিন দেখতে পারেন।<br><button class=\"link\" data-go=\"adminLogin\">অ্যাডমিন লগইন</button>")
assert 'claude' not in s.replace('Claude','').lower().replace('claude-', ''), 'claude reference left'

s = s.replace("/*__FB__*/", (root / 'src/part_fb.js').read_text(encoding='utf-8'))
rep("routine:vRoutine,admin:vAdmin,", "routine:vRoutine,admin:vAdmin,adminLogin:vAdminLogin,")
rep("app.addEventListener('submit',e=>{\n  e.preventDefault();", """app.addEventListener('submit',e=>{
  e.preventDefault();
  if(e.target.id==='adminForm'){
    const em=document.getElementById('adEmail').value.trim().toLowerCase(), pw=document.getElementById('adPass').value, er=document.getElementById('adErr');
    if(!DB){ er.textContent='অ্যাপটি এখনো সার্ভারের সাথে যুক্ত করা হয়নি।'; return; }
    if(!em||!pw){ er.textContent='ইমেইল ও পাসওয়ার্ড দুটোই লিখুন।'; return; }
    S.signing=true; render();
    S.adminDenied=false;
    DB.signIn(em,pw).then(()=>{ S.signing=false; render(); })
      .catch(err=>{ S.signing=false; render(); const x=document.getElementById('adErr');
        const c=err&&err.code||'unknown';
        const m=/invalid-credential|wrong-password|user-not-found|invalid-login/.test(c)?'ইমেইল বা পাসওয়ার্ড ঠিক নেই।'
          :/invalid-email/.test(c)?'ইমেইলটি সঠিকভাবে লেখা হয়নি।'
          :/operation-not-allowed/.test(c)?'Firebase-এ Email/Password লগইন চালু করা নেই।'
          :/user-disabled/.test(c)?'এই অ্যাকাউন্টটি Firebase-এ বন্ধ করা আছে।'
          :/too-many-requests/.test(c)?'অনেকবার চেষ্টা হয়েছে। কিছুক্ষণ পরে আবার চেষ্টা করুন।'
          :/network/.test(c)?'ইন্টারনেট সংযোগ নেই।'
          :/api-key|app-not-authorized|unauthorized-domain/.test(c)?'অ্যাপটি Firebase-এ অনুমোদিত নয়।'
          :'লগইন করা যায়নি।';
        if(x) x.textContent=m+' (কোড: '+c.replace('auth/','')+')'; });
    return;
  }""")
rep("  if(t.hasAttribute('data-logout')){ S.user=null; persist(); go('login'); return; }",
    "  if(t.hasAttribute('data-adminout')){ DB.signOut().then(()=>{ go('home'); toast('অ্যাডমিন লগ আউট হয়েছে'); }); return; }")
rep("const authed=!!S.user && !['login','otp'].includes(S.view);", "const authed=true;")

head = """<!doctype html>
<html lang="bn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1F6FE5">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}
body{margin:0;font:14px/1.5 system-ui,sans-serif;-webkit-tap-highlight-color:transparent}
img{max-width:100%}
[hidden]{display:none!important}
</style>
<script src="config.js"></script>
<script src="db.js"></script>
<script src="mcq.js"></script>
"""
# <title> + <style> + markup are at the top of the artifact; move title/style into head, rest into body
m = re.match(r'(<title>.*?</title>\n)(.*?</style>\n)(.*)$', s, re.S)
title, styles, body = m.group(1), m.group(2), m.group(3)
out = head + title + styles + "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
(root / 'www/index.html').write_text(out, encoding='utf-8')
print('www/index.html written', len(out))
