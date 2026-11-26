"""v12：第 2 張受眾卡（白牆貼頁 q2）一頁一頁再貼上 5 張內頁。只貼在空位，不碰到牆上原本的內頁。"""
import os, shutil, numpy as np
from PIL import Image, ImageFilter, ImageEnhance
D=os.path.dirname(os.path.abspath(__file__))
base=Image.open(f'{D}/img/q2.jpg').convert('RGB')
B=np.asarray(base).astype(np.float32)
# (牆面圖檔, 左上 x, y, 旋轉角)
P=[('04',112,128,-3.0),('09',702,110,2.5),('24',852,262,-2.0),('13',205,618,3.0),('26',840,612,-3.5)]
PW,PH=100,155
def page_layer(f,x,y,ang,scale=1.0):
    pg=Image.open(f'{D}/img/wall/{f}.jpg').convert('RGB').resize((PW,PH),Image.LANCZOS)
    pg=ImageEnhance.Contrast(pg).enhance(0.8); pg=ImageEnhance.Color(pg).enhance(0.8)
    a=np.asarray(pg).astype(np.float32)
    # 牆面光影：取底圖同位置亮度，相對平均值調整
    patch=B[y:y+PH,x:x+PW].mean(axis=2,keepdims=True)
    a=np.clip(a*(patch/patch.mean())**0.7*1.03+16,0,255)
    pg=Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    if scale!=1.0: pg=pg.resize((round(PW*scale),round(PH*scale)),Image.LANCZOS)
    pg=pg.rotate(ang,expand=True,resample=Image.BICUBIC)
    return pg
def shadow(pg,op):
    al=pg.split()[3].filter(ImageFilter.GaussianBlur(5))
    sh=Image.new('RGBA',pg.size,(40,30,25,0)); sh.putalpha(al.point(lambda v:int(v*op)))
    return sh
def place(canvas,f,x,y,ang,scale=1.0,lift=0):
    pg=page_layer(f,x,y,ang,scale)
    cx,cy=x+PW/2,y+PH/2
    px,py=round(cx-pg.width/2),round(cy-pg.height/2)
    sh=shadow(pg,0.28+0.15*lift)
    canvas.alpha_composite(sh,(px+3+round(6*lift),py+5+round(8*lift)))
    canvas.alpha_composite(pg,(px,py))
od=f'{D}/gif/clips/x_wallq2'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
frames=[]; done=[]
cur=base.convert('RGBA')
def snap(extra=None):
    c=base.convert('RGBA')
    for p in done: place(c,*p)
    if extra: place(c,*extra[0],**extra[1])
    frames.append(c.convert('RGB'))
for _ in range(10): snap()
for p in P:
    for k,(s,l) in enumerate([(1.14,1.0),(1.08,.7),(1.03,.35),(1.0,.1)]):
        snap((p,dict(scale=s,lift=l)))
    done.append(p)
    for _ in range(5): snap()
for _ in range(17): snap()
for i,f in enumerate(frames): f.save(f'{od}/{i+1:03d}.jpg',quality=92)
frames[-1].save(f'{D}/wallq2_last.jpg',quality=92)
print(len(frames))
