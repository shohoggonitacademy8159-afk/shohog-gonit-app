# অ্যাপ আইকন (src/icon_src.png — অংকবাড়ি লোগো) থেকে Android লঞ্চার আইকন ও ওয়েব আইকন তৈরি
# - ic_launcher.png: পুরো লোগো (সোনালি ফ্রেমসহ), বাইরের সাদা কোণ স্বচ্ছ
# - ic_launcher_foreground.png (adaptive): ফ্রেম ছাড়া ভেতরের অংশ, নিরাপদ এলাকায়; পটভূমি ক্রিম রঙ
# - ic_launcher_round.png: ক্রিম বৃত্তে ভেতরের অংশ
import os
from PIL import Image, ImageDraw, ImageFilter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES=os.path.join(ROOT,'android/app/src/main/res')
BG=(253,251,245)
src=Image.open(os.path.join(ROOT,'src/icon_src.png')).convert('RGBA'); W=src.width
# বাইরের সাদা কোণ স্বচ্ছ: কোণ থেকে flood-fill
im=src.copy(); px=im.load()
from collections import deque
seen=set(); q=deque([(0,0),(W-1,0),(0,W-1),(W-1,W-1)])
while q:
    x,y=q.popleft()
    if (x,y) in seen or not(0<=x<W and 0<=y<W): continue
    r,g,b,a=px[x,y]
    if r<235 or g<235 or b<225: continue
    seen.add((x,y)); px[x,y]=(r,g,b,0)
    q.extend(((x+1,y),(x-1,y),(x,y+1),(x,y-1)))
full=im
# ফ্রেম ছাড়া ভেতরের অংশ (গোলাকার কোণ ক্রিম দিয়ে ঢাকা)
m=int(W*0.05); inner=src.crop((m,m,W-m,W-m)).convert('RGBA')
mask=Image.new('L',inner.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,inner.width-1,inner.height-1),radius=int(W*0.13),fill=255)
base=Image.new('RGBA',inner.size,BG+(255,)); base.paste(inner,(0,0),mask); inner=base
def fg(size,share):
    c=Image.new('RGBA',(size,size),(0,0,0,0)); s=int(size*share); t=inner.resize((s,s),Image.LANCZOS)
    c.paste(t,((size-s)//2,(size-s)//2)); return c
def rnd(size):
    c=Image.new('RGBA',(size*4,size*4),BG+(255,)); s=int(size*4*0.74); t=inner.resize((s,s),Image.LANCZOS)
    c.paste(t,((size*4-s)//2,(size*4-s)//2))
    mk=Image.new('L',c.size,0); ImageDraw.Draw(mk).ellipse((0,0,c.width-1,c.height-1),fill=255)
    out=Image.new('RGBA',c.size,(0,0,0,0)); out.paste(c,(0,0),mk); return out.resize((size,size),Image.LANCZOS)
for d,k in {'mdpi':1,'hdpi':1.5,'xhdpi':2,'xxhdpi':3,'xxxhdpi':4}.items():
    L,F=round(48*k),round(108*k); dr=os.path.join(RES,'mipmap-'+d)
    full.resize((L,L),Image.LANCZOS).save(os.path.join(dr,'ic_launcher.png'))
    rnd(L).save(os.path.join(dr,'ic_launcher_round.png'))
    fg(F,0.56).save(os.path.join(dr,'ic_launcher_foreground.png'))
open(os.path.join(RES,'values/ic_launcher_background.xml'),'w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#FDFBF5</color>\n</resources>')
for s in (192,512): full.resize((s,s),Image.LANCZOS).save(os.path.join(ROOT,f'www/icon-{s}.png'))
# প্রিভিউ: বৃত্ত/স্কুইর্কল মাস্কে adaptive আইকন কেমন দেখাবে
P=432; prev=Image.new('RGB',(P*3+40,P),(40,40,40))
a=Image.new('RGBA',(P,P),BG+(255,)); f=fg(P,0.56); a.alpha_composite(f)
cm=Image.new('L',(P,P),0); ImageDraw.Draw(cm).ellipse((P*18/108,P*18/108,P*90/108,P*90/108),fill=255)
v=a.crop((int(P*18/108),int(P*18/108),int(P*90/108),int(P*90/108))).resize((P,P)); cm2=cm.crop((int(P*18/108),int(P*18/108),int(P*90/108),int(P*90/108))).resize((P,P))
prev.paste(v,(0,0),cm2)
sm=Image.new('L',(P,P),0); ImageDraw.Draw(sm).rounded_rectangle((0,0,P-1,P-1),radius=P//4,fill=255); prev.paste(v,(P+20,0),sm)
prev.paste(full.resize((P,P)),(2*P+40,0),full.resize((P,P)))
prev.save('/tmp/icon_prev.png'); print('icons done')
