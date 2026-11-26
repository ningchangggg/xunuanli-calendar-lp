import os, shutil, base64, io
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
B="/Volumes/品牌發展培訓部/Ning's剪輯資料庫/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
NAME='11.27_煦暖曆_落地頁改版_v12_貼牆動圖_底座經典交替_標題字色'; O=B+NAME; P='11.27_煦暖曆_落地頁改版_v12'
SEC=[('s03','03_誰適合煦暖曆_店員推薦_01',0),('s03_2','03-2_店員推薦02_一頁頁貼上牆_GIF',1),('s03_3','03-3_店員推薦03_底座款經典款交替_GIF',1),('s03_4','03-4_店員推薦04',0),('s03b','03b_聖誕節前到貨_櫥窗黑板_GIF',1),('s04','04_數字列_吊牌',0),('s05','05_365頁內頁牆',0),
('s05a','05a_閱讀指南01撕下今天_GIF',1),('s06','06_一頁拆解_6天輪播_GIF',1),('s06a','06a_閱讀指南02分享那段話_GIF',1),('s07','07_閱讀指南03貼成風景牆_GIF',1),
('s09','09_作家專區',0),('s10','10_六款年度代表色_經典底座輪播_GIF',1),('s11','11_規格_版權頁',0),('s12','12_轉折',0)]
for sub in ['說明圖_1080寬','動圖_MP4備用','_原始檔']: os.makedirs(f'{O}/{sub}',exist_ok=True)
names=[]
for sid,nm,g in SEC:
    if g:
        shutil.copy(f'{D}/gif/enc/{sid}.gif',f'{O}/說明圖_1080寬/{nm}.gif'); shutil.copy(f'{D}/gif/enc/{sid}.mp4',f'{O}/動圖_MP4備用/{nm}.mp4'); names.append((sid,nm+'.gif',g))
    else:
        Image.open(f'{D}/sec/{sid}.png').convert('RGB').save(f'{O}/說明圖_1080寬/{nm}.jpg',quality=90); names.append((sid,nm+'.jpg',g))
head=f'<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>煦暖曆落地頁 v12</title><style>body{{margin:0;background:#888}}main{{max-width:432px;margin:0 auto;background:#fff}}img,video{{display:block;width:100%}}</style><main>'
open(f'{O}/{P}_整頁預覽_動態.html','w').write(head+'\n'.join(f'<img src="說明圖_1080寬/{n}">' for _,n,_ in names)+'</main>')
parts=[]
for sid,n,g in names:
    if g:
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{base64.b64encode(open(f"{D}/gif/enc/{sid}.mp4","rb").read()).decode()}"></video>')
    else:
        im=Image.open(f'{O}/說明圖_1080寬/{n}'); im=im.resize((864,round(im.height*864/im.width)),Image.LANCZOS); bio=io.BytesIO(); im.save(bio,'JPEG',quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(bio.getvalue()).decode()}">')
open(f'{O}/{P}_整頁預覽_單檔整合.html','w').write(head+''.join(parts)+'</main>')
ims=[]
for sid,n,g in names:
    ims.append(Image.open(f'{D}/gif/secframes/{sid}/{"012" if sid=="s03b" else "001"}.png').convert('RGB') if g else Image.open(f'{O}/說明圖_1080寬/{n}').convert('RGB'))
H=sum(i.height for i in ims); st=Image.new('RGB',(1080,H)); y=0
for i in ims: st.paste(i,(0,y)); y+=i.height
st.resize((540,H//2),Image.LANCZOS).save(f'{O}/{P}_整頁預覽_靜態第一格.jpg',quality=82)
for f in ['build_v11.py','shot_v10.py','render_v10.py','deliver_v12.py','page.html','fonts_cream.otf']: shutil.copy(f'{D}/{f}',f'{O}/_原始檔/{f}')
shutil.copy(f'{D}/gif/enc.sh',f'{O}/_原始檔/enc.sh'); shutil.copy(f'{D}/gif/caps_x_days.json',f'{O}/_原始檔/caps_x_days.json'); shutil.copy(f'{D}/gif/caps_x_c1.json',f'{O}/_原始檔/caps_x_c1.json'); shutil.copy(f'{D}/gif/caps_x_q3.json',f'{O}/_原始檔/caps_x_q3.json'); shutil.copy(f'{D}/wall_paste.py',f'{O}/_原始檔/wall_paste.py')
shutil.copytree(f'{D}/img',f'{O}/_原始檔/img',dirs_exist_ok=True)
print(O, H)
