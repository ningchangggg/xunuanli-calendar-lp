"""煦暖曆落地頁 page.html（照旅行 v28 規範），2026-11-24。base.css 共用，煦暖曆專屬放 EXTRA。"""
import json, random, os
D = os.path.dirname(os.path.abspath(__file__))
css = open(f'{D}/base.css').read()
EXTRA = '''
.cd .tk p mark{color:inherit;background:linear-gradient(100deg,transparent 2%,rgba(248,222,96,.72) 4%,rgba(246,214,80,.6) 60%,rgba(248,222,96,.75) 96%,transparent 98%) no-repeat 0 72%/100% 58%;padding:0 3px;margin:0 -1px;border-radius:2px 5px 3px 6px}
.cd .tk .route{width:92px}.cd .tk .route b{font-size:15px}
#s03b .sh{animation:sweep 2.5s linear infinite}
#s03b .sp{animation:tw 2.5s linear infinite}
@keyframes sweep{0%{left:-40%}55%{left:120%}100%{left:120%}}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}12%{opacity:1;transform:scale(1.15) rotate(20deg)}26%{opacity:0;transform:scale(.4)}}
#s04 .n{font-size:28px}
/* 05 內頁牆 */
#s05{background:var(--night);padding:38px 0 0}
#s05 .eyebrow{color:#E9A493}#s05 h2{color:#fff;margin-top:10px}#s05 .lead{color:#C9C1B5;margin-top:8px;padding:0 16px}
#s05 .wall{position:relative;height:520px;margin-top:22px;overflow:hidden}
#s05 .wall img{position:absolute;width:86px;box-shadow:0 6px 14px rgba(0,0,0,.45)}
#s05 .wall:after{content:"";position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,var(--night))}
/* 06 一頁拆解 */
#s06{padding:40px 20px 34px;background:var(--paper)}
#s06 .box{margin-top:20px;background:#fff;border-radius:8px;box-shadow:0 8px 22px rgba(30,27,25,.12);overflow:hidden}
#s06 .cap{height:62px;background:var(--paper2);border-bottom:1px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:15.5px;color:var(--ink);letter-spacing:.05em;text-align:center;padding:0 12px}
#s06 .cap small{font-size:11.5px;color:var(--brick);letter-spacing:.14em;margin-bottom:3px}
#s06 .pgv{position:relative;height:340px}
#s06 .pgi{position:absolute;left:96px;top:16px;width:200px;height:307px;background-size:cover;box-shadow:0 6px 16px rgba(30,27,25,.22)}
#s06 .lb{position:absolute;width:62px;font-size:12.5px;color:var(--ink);letter-spacing:.04em;line-height:1.35}
#s06 .lb b{display:block;font-family:"Helvetica Neue",Arial;font-size:10px;color:var(--brick);letter-spacing:.16em;margin-bottom:2px}
#s06 .lb.l{left:6px;text-align:left}#s06 .lb.r{right:6px;text-align:right}
#s06 .ln{position:absolute;height:0;border-top:1px dashed var(--brick)}
/* 08 full */
#s08 .ph{height:540px}
/* 09 作家牆 */
#s09{background:var(--night);padding:38px 16px 30px;color:#fff}
#s09 .eyebrow{color:#E9A493}#s09 h2{color:#fff;margin-top:10px}#s09 .lead{color:#C9C1B5;margin-top:8px}
.wr{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:20px}
.wr figure{margin:0}
.wr .im{height:112px;background-size:cover;background-position:center top;border-radius:3px}
.wr figcaption{font-size:12.5px;color:#F3EEE5;text-align:center;margin-top:7px;letter-spacing:.06em;white-space:nowrap}
#s09 .tip{font-size:12.5px;color:#B9C2CE;text-align:center;margin-top:18px;letter-spacing:.06em}
/* 10 六色 */
#s10 .g6{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:0 16px;margin-top:20px}
#s10 .g6 figure{margin:0;background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 4px 12px rgba(30,27,25,.1)}
#s10 .g6 .im{height:124px;background-size:cover;background-position:center}
#s10 .g6 figcaption{font-size:13px;color:var(--ink);text-align:center;padding:7px 0 8px;letter-spacing:.08em}
#s10 .g6 figcaption small{display:block;font-family:"Helvetica Neue",Arial;font-size:9px;color:var(--taupe);letter-spacing:.16em;margin-top:2px}
#s12 .ph{height:540px}
#s12 .tx{top:30px;bottom:auto}#s12 .shade{top:0;bottom:auto;height:240px;background:linear-gradient(rgba(20,16,12,.55),transparent)}
'''

P = [
 dict(n='01', who='喜歡文字的人', h='睡前總想讀一段，被文字安慰', k1='每天', v1='作家語錄', k2='陪你', v2='365 天',
      p='連俞涵、周慕姿、陳繁齊…<br>每天一位作家，<mark>寫給今天的你</mark>。', img='q1'),
 dict(n='02', who='需要一點溫柔的人', h='日子好累，只想有人說聲沒關係', k1='每天', v1='今日指南', k2='用來', v2='安放心情',
      p='撕下今天這一頁，<br>讀到的那句剛好<mark>接住你</mark>。', img='q2'),
 dict(n='03', who='交換禮物', h='禮物預算一千，送一份有溫度的心意', k1='送給', v1='閨蜜同事', k2='挑選', v2='六款顏色',
      p='挑一個最像他的顏色，<br>拆開那一刻，他就知道<mark>你懂他</mark>。', img='q3'),
 dict(n='04', who='聖誕禮物', h='送給今年辛苦了的那個人', k1='送給', v1='重要的人', k2='陪他', v2='365 天',
      p='每天早上撕一頁，<br>都是你<mark>替他說的加油</mark>。', img='q4'),
]
def card(x):
    return f'''<div class="cd"><div class="ph" style="background-image:url(img/{x["img"]}.jpg)"><div class="ov"><div class="no en">NO. {x["n"]}</div><div class="who">{x["who"]}</div><h3>{x["h"]}</h3></div></div>
<div class="tk"><div class="route"><div>{x["k1"]}<b>{x["v1"]}</b></div><div>{x["k2"]}<b>{x["v2"]}</b></div></div><div><p>{x["p"]}</p></div></div></div>'''

def how(i, sid, h, lead, clip, step, en):
    return f'''<section id="{sid}" class="how{' alt' if i % 2 == 0 else ''}">
  <div class="eyebrow">HOW TO USE 0{i}</div><h2>{h}</h2><div class="lead">{lead}</div>
  <div class="mv"><div class="ph" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div>
    <div class="stub"><span class="en">STEP 0{i}</span><b>{step}</b><span class="en">{en}</span></div></div>
</section>'''

random.seed(7)
wall = ''
k = 1
for r in range(5):
    for c in range(5):
        if k > 28: break
        x = c * 92 - 20 + (r % 2) * 40 + random.uniform(-6, 6)
        y = r * 112 - 20 + random.uniform(-6, 6)
        wall += f'<img src="img/wall/{k:02d}.jpg" style="left:{x:.0f}px;top:{y:.0f}px;transform:rotate({random.uniform(-4,4):.1f}deg)">'
        k += 1

caps = json.load(open(f'{D}/gif/caps_x_days.json'))
# 頁面元素位置（200×307 內頁，左上 96,16）
LB = [('l', 36, '01', '月份'), ('r', 36, '02', '節氣<br>倒數日'), ('l', 80, '03', '大日期'),
      ('r', 156, '04', '今日指南'), ('l', 210, '05', '作家語錄'), ('r', 304, '06', '作者出處')]
lbs = ''
for side, y, n, t in LB:
    lbs += f'<div class="lb {side}" style="top:{y-14}px"><b>{n}</b>{t}</div>'
    if side == 'l': lbs += f'<i class="ln" style="left:66px;width:44px;top:{y}px"></i>'
    else: lbs += f'<i class="ln" style="right:66px;width:44px;top:{y}px"></i>'

W = [('w1', 'Queenie Kao'), ('w2', '周慕姿'), ('w3', '喬心誌'), ('w4', '林達陽'), ('w5', '沈希默'), ('w6', '知寒'), ('w7', '連俞涵'), ('w8', '陳繁齊')]
wr = ''.join(f'<figure><div class="im" style="background-image:url(img/{a}.jpg)"></div><figcaption>{b}</figcaption></figure>' for a, b in W)
C6 = [('c1', '餘燼', 'EMBER'), ('c2', '暮槿', 'DUSK'), ('c3', '亞麻', 'LINEN'), ('c4', '靜灣', 'BAY'), ('c5', '藤花', 'WISTERIA'), ('c6', '初瀨', 'SHOAL')]
g6 = ''.join(f'<figure><div class="im" style="background-image:url(img/{a}.jpg)"></div><figcaption>{b}<small>{e}</small></figcaption></figure>' for a, b, e in C6)

body = f'''
<section id="s03">
  <div class="eyebrow">誰適合煦暖曆？</div>
  <h2>聖誕禮物 x 交換禮物<br><span class="mark">送禮送到心坎裡</span></h2>
  <div class="lead">一天一句作家寫給你的話，<br>365 天，都有人陪。</div>
  {''.join(card(x) for x in P)}
</section>
<section id="s03b"><div class="xm"><div class="sh"></div>
  <i class="sp" style="left:8%;top:14%;animation-delay:0s"></i><i class="sp" style="left:88%;top:20%;animation-delay:.5s"></i><i class="sp" style="left:93%;top:72%;animation-delay:1s"></i><i class="sp" style="left:5%;top:78%;animation-delay:1.5s"></i><i class="sp" style="left:50%;top:6%;animation-delay:2s"></i>
  <div class="en sm">CHRISTMAS DELIVERY</div><div class="big">聖誕節前到貨</div></div></section>
<section id="s04">
  <div><div class="n">365</div><div class="c">句作家語錄</div></div>
  <div><div class="n">6<small>款</small></div><div class="c">年度代表色</div></div>
  <div><div class="n">2<small>種</small></div><div class="c">經典款・底座款</div></div>
</section>
<section id="s05">
  <div class="eyebrow">一年 365 頁</div>
  <h2>每一天，<br>都是一張風景</h2>
  <div class="lead">大日期、今日指南、作家語錄、農曆節氣，<br>一頁全彩，每天換一種心情。</div>
  <div class="wall">{wall}</div>
</section>
{how(1, 's05a', '早上撕下一頁，<br>讀一句給今天的話', '陽光透過紙頁，<br>今天的那句話剛好亮起來。', 'x_tear', '撕下今天', 'TEAR')}
<section id="s06">
  <div class="eyebrow">一頁有什麼？</div>
  <h2>一頁一句，<br><span class="mark">每天都設計過</span></h2>
  <div class="box"><div class="cap" data-caps="x_days">{caps[0]}</div>
  <div class="pgv"><div class="pgi" data-clip="x_days" style="background-image:url(gif/clips/x_days/001.jpg)"></div>{lbs}</div></div>
</section>
{how(2, 's06a', '跟喜歡的人，<br>交換今天的那一句', '你撕到的、她撕到的，<br>剛好都是對方需要的話。', 'x_share', '交換一句', 'SHARE')}
{how(3, 's07', '撕下來的每一頁，<br>貼成一面風景牆', '一天一張，貼滿一整面，<br>一年的心情都看得見。', 'x_wall', '貼成風景牆', 'COLLECT')}
<section id="s08" class="full">
  <div class="ph" data-clip="x_flip" style="background-image:url(gif/clips/x_flip/001.jpg)"></div><div class="shade"></div>
  <div class="tx"><div class="a">今天的你，<br>會翻到哪一句？</div></div>
</section>
<section id="s09">
  <div class="eyebrow">作家陣容</div>
  <h2>他們為 2027 的你<br>寫了這些字</h2>
  <div class="lead">每位作家一句獨家語錄，<br>陪你走過一整年。</div>
  <div class="wr">{wr}</div>
  <div class="tip">還有更多作家與好書摘句，一起陪你 365 天</div>
</section>
<section id="s10">
  <div class="eyebrow">年度代表色</div>
  <h2>六款顏色，<br>挑一個最像你的</h2>
  <div class="lead">經典款撕頁直立，底座款附可替換的立架</div>
  <div class="g6">{g6}</div>
  <div class="nt">實拍色彩依螢幕顯示略有差異</div>
</section>
<section id="s11">
  <div class="ph"></div>
  <div class="stub"><div class="hd"><span class="en">XUNUANLI 2027</span><span class="en">DAILY CALENDAR</span></div>
    <div class="row"><span class="k">尺寸</span><span class="v">9 × 16 公分，直式手撕</span></div>
    <div class="row"><span class="k">造型</span><span class="v">經典款、底座款</span></div>
    <div class="row"><span class="k">內容</span><span class="v">365 頁全彩，大日期、今日指南、作家語錄、農曆、倒數日</span></div>
    <div class="row"><span class="k">外盒</span><span class="v">厚磅紙盒，可直接送禮</span></div>
    <div class="row"><span class="k">重量</span><span class="v">520 g（含外盒 665 g）</span></div>
  </div>
</section>
<section id="s12" class="full">
  <div class="ph" style="background-image:url(img/end.jpg)"></div><div class="shade"></div>
  <div class="tx"><div class="a">每天一句，<br>剛好接住今天的你</div><div class="b">日子不一定順，<br>但每天早上，都有人先對你說聲早安。</div></div>
</section>
'''
html = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><title>煦暖曆落地頁 v6</title>
<style>
{css}
{EXTRA}
</style></head><body>
{body}
</body></html>'''
open(f'{D}/page.html', 'w').write(html)
print('ok', len(html))
