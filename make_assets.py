from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def font(size, weight=700):
    try:
        f = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', size)
        f.set_variation_by_axes([weight])
        return f
    except Exception:
        return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', size)

BG=(11,11,15); FG=(245,245,240); ACC=(214,48,48); MUTE=(150,150,160)

def base(w,h):
    im=Image.new('RGB',(w,h),BG); d=ImageDraw.Draw(im)
    # faint grid
    step=max(40,w//28)
    for x in range(0,w,step): d.line([(x,0),(x,h)],fill=(20,20,26),width=1)
    for y in range(0,h,step): d.line([(0,y),(w,y)],fill=(20,20,26),width=1)
    # red glow top-right
    glow=Image.new('RGB',(w,h),BG); gd=ImageDraw.Draw(glow)
    gd.ellipse([w*0.62,-h*0.5,w*1.25,h*0.55],fill=(120,22,22))
    glow=glow.filter(ImageFilter.GaussianBlur(w//9))
    im=Image.blend(im,glow,0.55)
    return im

def banner(path, w=1136, h=600):
    im=base(w,h); d=ImageDraw.Draw(im)
    pad=int(w*0.062)
    d.text((pad,pad),"IVYHACKS  ·  UNIVERSITY OF PENNSYLVANIA  ·  OCT 10–11",font=font(int(h*0.046),600),fill=MUTE)
    big=font(int(h*0.27),800)
    d.text((pad-4,int(h*0.17)),"BEAT",font=big,fill=FG)
    d.text((pad-4,int(h*0.41)),"MUSE.",font=big,fill=ACC)
    sub=font(int(h*0.057),500)
    d.text((pad,int(h*0.73)),"Build the best realtime AI that runs 24/7. Win $4K.",font=sub,fill=FG)
    d.text((pad,int(h*0.83)),"Tokens + architecture on us.",font=sub,fill=MUTE)
    im.save(path,quality=92); print(path,im.size)

def poster(path, s=1080):
    im=base(s,s); d=ImageDraw.Draw(im); pad=72
    d.text((pad,pad),"IVYHACKS",font=font(44,600),fill=MUTE)
    big=font(236,800)
    d.text((pad-6,150),"BEAT",font=big,fill=FG)
    d.text((pad-6,370),"MUSE.",font=big,fill=ACC)
    d.text((pad,640),"Build the best realtime AI\nthat runs 24/7. Win $4K.",font=font(54,500),fill=FG,spacing=10)
    rows=["Sat Oct 10 – Sun Oct 11","University of Pennsylvania","Free · meals covered · 300 spots","Tokens + architecture on us"]
    y=820
    for r in rows:
        d.ellipse([pad,y+14,pad+14,y+28],fill=ACC); d.text((pad+34,y),r,font=font(38,500),fill=FG); y+=56
    im.save(path,quality=92); print(path,im.size)

banner('hero_banner.jpg'); poster('poster_square.jpg')
