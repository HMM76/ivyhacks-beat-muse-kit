# Wide email header in the style of the Luma cover (black / white / red / acid, condensed caps, mono meta).
from PIL import Image, ImageDraw, ImageFont
W,H=1200,700
BG=(11,11,11); WHITE=(245,245,240); RED=(224,32,32); ACID=(208,240,48); MUTE=(140,140,140)
def cond(size, black=True): return ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', size, index=9 if black else 4)
def mono(size): return ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', size)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); pad=56
# wordmark + hairline + mono subline (top-left), like the cover
d.text((pad,pad-6),"IVYHACKS",font=cond(54),fill=WHITE)
d.line([(pad,pad+58),(pad+300,pad+58)],fill=WHITE,width=2)
d.text((pad,pad+68),"UNIVERSITY OF PENNSYLVANIA",font=mono(17),fill=MUTE)
# right-top mono tag
tag="300 SPOTS · FREE · MEALS COVERED"; tw=d.textlength(tag,font=mono(17)); d.text((W-pad-tw,pad+4),tag,font=mono(17),fill=MUTE)
# headline: BEAT MUSE. / WIN $4K.
big=cond(205)
y1=195
d.text((pad-6,y1),"BEAT",font=big,fill=WHITE)
bw=d.textlength("BEAT ",font=big)
d.text((pad-6+bw,y1),"MUSE.",font=big,fill=RED)
d.text((pad-6,y1+175),"WIN $4K.",font=big,fill=ACID)
# bottom mono strip
d.line([(pad,H-78),(W-pad,H-78)],fill=(42,42,42),width=2)
d.text((pad,H-58),"OCT 10 + 11, 2026",font=mono(18),fill=MUTE)
u="luma.com/d60fjmjy"; uw=d.textlength(u,font=mono(18)); d.text((W-pad-uw,H-58),u,font=mono(18),fill=ACID)
im.save('hero_banner.jpg',quality=92); print('hero_banner.jpg',im.size)
