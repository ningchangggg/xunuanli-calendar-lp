"""煦暖曆落地頁 v11（2026-11-26）：整頁改「煦暖書店・店員選書」風格（阿寧從比稿改選 C）。
規則：字一律凝書體（Cream，不設粗體）；標籤、推薦卡、內頁特寫都不能蓋到照片裡的產品，找空位放，找不到就移到照片外。
併入 11/24 v9：六色經典款／底座款同步輪播、規格圖裁掉上方空白。"""
import json, os, random
D = os.path.dirname(os.path.abspath(__file__))

CSS = '''
@font-face{font-family:Cream;src:url(fonts_cream.otf)}
:root{--kraft:#D8C2A3;--board:#2E3A33;--board2:#3A4A40;--chalk:#F3EBDD;--paper:#FFFDF7;--ink:#2B211D;--text:#4A3D36;--wine:#8B2E3E;--pink:#F2C9BE;--yl:#F3D37A;--mute:#8E7B6C;--line:#E2D3BE}
*{box-sizing:border-box;margin:0;padding:0}
body{width:432px;background:#ddd;font-family:Cream,serif;color:var(--text);-webkit-font-smoothing:antialiased}
b,h1,h2,h3{font-weight:normal}
section{width:432px;position:relative;overflow:hidden;background:var(--kraft) repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 2px,transparent 2px 5px)}
.eyebrow{font-size:13px;letter-spacing:.24em;color:var(--wine);text-align:center}
h2{font-size:28px;line-height:1.4;color:var(--ink);text-align:center;letter-spacing:.06em}
.lead{font-size:14.5px;line-height:1.85;text-align:center;letter-spacing:.05em}
.hd{text-align:center;position:relative}.hd h2{margin-top:10px}.hd .lead{margin-top:10px}
.sign{display:inline-block;border:1px solid rgba(243,235,221,.5);padding:4px 14px;font-size:12px;letter-spacing:.3em;color:var(--chalk);margin-bottom:14px}
.dark{background:var(--board)}
.dark .eyebrow{color:#E7B9A6}.dark h2{color:#F7F0E3}.dark .lead{color:#D9D2C4}
.chip{display:inline-block;background:var(--board);color:var(--chalk);font-size:12px;letter-spacing:.24em;padding:5px 14px 6px}
.chip i{font-style:normal;color:#E7B9A6;margin-left:8px}
.dark .chip{background:var(--wine)}.dark .chip i{color:var(--pink)}

/* 03 受眾 */
#s03{padding:0 0 6px}
#s03 header{background:var(--board);padding:34px 24px 30px;text-align:center;position:relative}
#s03 header .eyebrow{color:#E7B9A6}#s03 header h2{color:#F7F0E3;margin-top:10px}#s03 header .lead{color:#E3DCCF;margin-top:10px}
#s03 header:after{content:"";position:absolute;left:0;right:0;bottom:-10px;height:10px;background:linear-gradient(rgba(0,0,0,.18),transparent)}
.shelf{padding:30px 0 0}
.bk{position:relative;padding:0 16px 44px}
.sec3{padding-top:0}
.bk .ph{position:relative}
.kd{position:absolute;left:12px;top:12px;display:flex;align-items:baseline;gap:8px;background:rgba(46,58,51,.9);padding:5px 12px 6px}
.kd b{font-size:15px;color:var(--chalk);letter-spacing:.14em}.kd span{font-size:10px;color:#E7B9A6;letter-spacing:.2em}
.bk .ph{height:320px;background-size:cover;box-shadow:0 14px 26px rgba(60,40,20,.28)}
.obi{position:relative;background:var(--wine);color:#FBF4EA;padding:12px 110px 14px 18px;box-shadow:0 8px 16px rgba(60,20,20,.22)}
.obi .k{font-size:11.5px;letter-spacing:.24em;color:var(--pink)}
.obi .h{font-size:20px;line-height:1.45;letter-spacing:.05em;margin-top:4px}
.obi .s{position:absolute;right:16px;top:14px;font-size:11px;letter-spacing:.14em;color:var(--pink);text-align:right;line-height:1.6}
.desk{display:flex;align-items:flex-start;gap:16px;padding:0 6px;margin-top:24px}
.bk.rv .desk{flex-direction:row-reverse}
.pop{position:relative;flex:1;background:var(--paper);padding:0 0 14px;box-shadow:0 8px 18px rgba(50,30,15,.26);transform:rotate(-2deg);margin-top:8px}
.bk.rv .pop{transform:rotate(2deg)}
.pop .bar{background:var(--board);color:var(--chalk);font-size:12px;letter-spacing:.24em;padding:6px 12px;display:flex;justify-content:space-between}
.pop .bar span{color:#E7B9A6}
.pop .for{font-size:12px;color:var(--mute);letter-spacing:.14em;margin:11px 14px 0}
.pop .who{font-size:19.5px;white-space:nowrap;color:var(--ink);margin:2px 14px 0;letter-spacing:.08em;border-bottom:1.5px dashed #C9B49A;padding-bottom:5px}
.pop .v{font-size:16px;line-height:1.65;color:var(--text);margin:9px 14px 0;letter-spacing:.03em}
.pop .v:before{content:"如果你也是";display:block;font-size:11.5px;color:var(--wine);letter-spacing:.16em}
.pop .pin{position:absolute;left:50%;top:-40px;margin-left:-17px}
.mk{position:relative;width:118px;flex:none;transform:rotate(3deg);padding-top:10px}
.bk.rv .mk{transform:rotate(-3deg)}
.mk img{width:118px;display:block;box-shadow:0 8px 16px rgba(0,0,0,.32);position:relative}
.mk .rb{position:absolute;left:50px;top:-14px;width:16px;height:50px;background:var(--wine);clip-path:polygon(0 0,100% 0,100% 100%,50% 86%,0 100%)}
.tg{margin:10px auto 0;width:max-content;background:var(--yl);color:var(--ink);font-size:11.5px;letter-spacing:.1em;padding:4px 12px 5px;border-radius:14px;box-shadow:0 3px 8px rgba(0,0,0,.18)}
.tg b{font-size:14px;margin-left:4px}

/* 03b 聖誕到貨：櫥窗黑板 */
#s03b{padding:4px 16px 28px}
#s03b .xm{position:relative;height:150px;background:var(--board);border:6px solid #A9845B;box-shadow:inset 0 0 0 2px rgba(0,0,0,.25),0 10px 20px rgba(60,40,20,.3);text-align:center;color:var(--chalk);overflow:hidden}
#s03b .rib{position:absolute;right:-46px;top:20px;width:190px;transform:rotate(38deg);background:var(--wine);color:#FBF4EA;font-size:12px;letter-spacing:.2em;padding:6px 0;box-shadow:0 3px 8px rgba(0,0,0,.3)}
#s03b .sm{font-size:11px;letter-spacing:.2em;padding-top:26px;color:#E7B9A6}
#s03b .big{font-size:40px;letter-spacing:.14em;margin-top:8px}
#s03b .ft{font-size:13px;letter-spacing:.14em;margin-top:6px;color:#D9D2C4}
#s03b .sh{position:absolute;top:0;bottom:0;width:26%;left:-40%;background:linear-gradient(100deg,transparent,rgba(243,211,122,.28),transparent);animation:sweep 2.5s linear infinite}
#s03b .sp{position:absolute;width:8px;height:8px;background:var(--yl);clip-path:polygon(50% 0,62% 38%,100% 50%,62% 62%,50% 100%,38% 62%,0 50%,38% 38%);animation:tw 2.5s linear infinite}
@keyframes sweep{0%{left:-40%}55%{left:120%}100%{left:120%}}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}12%{opacity:1;transform:scale(1.3) rotate(20deg)}26%{opacity:0;transform:scale(.4)}}

/* 04 數字列：吊牌 */
#s04{display:flex;gap:10px;padding:8px 16px 30px}
#s04>div{flex:1;background:var(--paper);text-align:center;padding:22px 4px 14px;position:relative;box-shadow:0 6px 14px rgba(60,40,20,.18);clip-path:polygon(14% 0,86% 0,100% 12%,100% 100%,0 100%,0 12%)}
#s04>div:before{content:"";position:absolute;left:50%;top:8px;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:var(--kraft);box-shadow:inset 0 1px 2px rgba(0,0,0,.3)}
#s04 .n{font-size:30px;color:var(--wine);line-height:1.1}
#s04 .n small{font-size:14px;margin-left:2px}
#s04 .c{font-size:12.5px;color:var(--text);margin-top:6px;letter-spacing:.06em}

/* 05 內頁牆：書架 */
#s05{padding:38px 0 0}
#s05 .wall{position:relative;height:520px;margin-top:22px;overflow:hidden}
#s05 .wall img{position:absolute;width:86px;box-shadow:0 8px 16px rgba(0,0,0,.45)}
#s05 .wall:after{content:"";position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,var(--board))}

/* HOW TO USE：閱讀指南 */
.how{padding:38px 16px 34px}
.how h2{margin-top:14px}.how .lead{margin-top:8px}
.mv{margin-top:22px;background:var(--paper);padding:10px 10px 0;box-shadow:0 14px 28px rgba(60,40,20,.25)}
.mv .ph{height:470px;background-size:cover;background-position:center}
.mv .ob{display:flex;align-items:center;gap:10px;margin:0 -10px;padding:13px 18px;background:var(--wine);color:#FBF4EA;font-size:15.5px;letter-spacing:.1em}
.mv .ob .k{font-size:12px;color:var(--pink);letter-spacing:.22em}
.mv .ob .e{margin-left:auto;font-size:11.5px;color:var(--pink);letter-spacing:.22em}
.how.dark .mv{background:#F3EBDD}

/* 06 一頁拆解：目次 */
#s06{padding:38px 16px 34px}
#s06 .box{margin-top:20px;background:var(--paper);box-shadow:0 10px 24px rgba(60,40,20,.22)}
#s06 .cap{height:64px;background:var(--board);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:15.5px;color:var(--chalk);letter-spacing:.05em;text-align:center;padding:0 12px}
#s06 .cap small{font-size:11.5px;color:#E7B9A6;letter-spacing:.16em;margin-bottom:3px}
#s06 .pgv{position:relative;height:340px}
#s06 .pgi{position:absolute;left:100px;top:16px;width:200px;height:307px;background-size:cover;box-shadow:0 8px 18px rgba(40,25,15,.28)}
#s06 .lb{position:absolute;width:64px;font-size:12.5px;color:var(--ink);letter-spacing:.04em;line-height:1.35}
#s06 .lb b{display:inline-block;width:19px;height:19px;line-height:19px;border-radius:50%;background:var(--yl);color:var(--ink);font-size:10.5px;text-align:center;margin-bottom:3px}
#s06 .lb.l{left:6px;text-align:left}#s06 .lb.r{right:2px;text-align:right}
#s06 .ln{position:absolute;height:0;border-top:1px dashed var(--wine)}

/* 09 作家專區 */
#s09{padding:38px 16px 32px}
.wr{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:22px}
.wr figure{margin:0;background:var(--paper);padding:4px 4px 0;box-shadow:0 4px 10px rgba(0,0,0,.3)}
.wr .im{height:104px;background-size:cover;background-position:center top}
.wr figcaption{font-size:12px;color:var(--ink);text-align:center;padding:6px 0 7px;letter-spacing:.04em;white-space:nowrap}
#s09 .tip{font-size:12.5px;color:#E9DCC6;text-align:center;margin-top:20px;letter-spacing:.08em}

/* 10 六色 */
#s10{padding:38px 0 30px}
#s10 .kind6{display:flex;align-items:baseline;justify-content:center;gap:10px;margin:16px auto 0;width:max-content;background:var(--board);padding:6px 18px 7px}
#s10 .kind6 b{font-size:17px;color:var(--chalk);letter-spacing:.14em}#s10 .kind6 span{font-size:11px;color:#E7B9A6;letter-spacing:.16em}
#s10 .g6{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 16px;margin-top:16px}
#s10 .g6 figure{margin:0;background:var(--paper);padding:5px 5px 0;box-shadow:0 6px 14px rgba(60,40,20,.2)}
#s10 .g6 .im{height:118px;background-size:cover;background-position:center}
#s10 .g6 figcaption{font-size:14px;color:var(--ink);text-align:center;padding:7px 0 8px;letter-spacing:.1em}
#s10 .g6 figcaption small{display:block;font-size:10px;color:var(--wine);letter-spacing:.2em;margin-top:2px}
#s10 .nt{font-size:11.5px;color:var(--mute);text-align:center;margin-top:14px;letter-spacing:.08em}

/* 11 規格：版權頁 */
#s11{padding:0 0 28px}
#s11 .ph{height:400px;background:url(img/spec.jpg) center 75%/cover}
#s11 .st{margin:18px 16px 0;background:var(--paper);box-shadow:0 12px 26px rgba(60,40,20,.22)}
#s11 .st .h{display:flex;justify-content:space-between;align-items:center;padding:10px 18px;background:var(--board);color:var(--chalk);font-size:12px;letter-spacing:.24em}
#s11 .st .h span:last-child{color:#E7B9A6}
#s11 .row{display:flex;padding:11px 18px;border-top:1px dashed var(--line);font-size:14px;line-height:1.6}
#s11 .row:first-of-type{border-top:0}
#s11 .k{width:62px;flex:none;color:var(--wine);letter-spacing:.16em}
#s11 .v{color:var(--ink);letter-spacing:.04em}

/* 12 收尾 */
#s12 .ph{height:540px;background-size:cover;background-position:center}
#s12 .shade{position:absolute;left:0;right:0;top:0;height:250px;background:linear-gradient(rgba(25,18,12,.55),transparent)}
#s12 .tx2{position:absolute;left:24px;right:24px;top:30px;color:#fff}
#s12 .a{font-size:28px;line-height:1.45;letter-spacing:.06em;text-shadow:0 2px 12px rgba(40,25,15,.45)}
#s12 .b{font-size:14px;line-height:1.8;margin-top:10px;letter-spacing:.06em;color:#FFF3E4;text-shadow:0 1px 8px rgba(40,25,15,.5)}
#s12 .nx{background:var(--board);color:var(--chalk);text-align:center;font-size:14px;letter-spacing:.12em;padding:18px 24px 20px;line-height:1.8}
#s12 .nx .tg{margin-top:10px}
'''

C = [
    dict(n='01', who='喜歡文字的人', voice='書買了一疊，<br>一本都沒翻完。', line='每天一頁，讀完一位作家<br>想對你說的話。', md='08.18', img='q1', pg='pg1', fx='50% 40%'),
    dict(n='02', who='需要一點溫柔的人', voice='最近好累，<br>好像沒人問我還好嗎。', line='撕下今天這一頁，<br>剛好有人接住你的疲憊。', md='11.28', img='q2', pg='pg2', fx='50% 45%'),
    dict(n='03', who='交換禮物', voice='預算一千，<br>不想送用完就丟的東西。', line='365 天，<br>他每天早上都會想起你。', md='02.24', img='q3', pg='pg3', fx='30% 60%'),
    dict(n='04', who='聖誕禮物', voice='想謝謝他，<br>可是說不出口。', line='讓作家替你說，<br>一天說一次。', md='07.17', img='q4', pg='pg4', fx='45% 30%'),
]


def pin():
    return '''<svg width="34" height="58" viewBox="0 0 34 58"><defs><linearGradient id="wd" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset=".5" stop-color="#fff" stop-opacity=".15"/><stop offset="1" stop-color="#000" stop-opacity=".2"/></linearGradient></defs>
<rect x="9" y="0" width="16" height="44" rx="3" fill="#C9A77C"/><rect x="9" y="0" width="16" height="44" rx="3" fill="url(#wd)"/>
<rect x="6" y="18" width="22" height="7" rx="2" fill="#8E8E8E"/><rect x="15" y="40" width="4" height="18" fill="#B8956A"/></svg>'''


def s03():
    clips = {1: 'x_wallq2', 2: 'x_q3'}
    out = '''<section id="s03"><header><div class="sign">煦暖書店　本週選書</div><div class="eyebrow">誰適合煦暖曆？</div>
<h2>店員推薦：<br>今年最好送的一本</h2><div class="lead">365 位作家，一天一頁。<br>給愛讀的人、累了的人，也給你想謝謝的人。</div></header><div class="shelf">'''
    for i, x in enumerate(C):
        m, d = x['md'].split('.')
        if i:
            out += f'<section id="s03_{i+1}" class="sec3">'
        clip = clips.get(i)
        src = f'gif/clips/{clip}/001.jpg' if clip else f'img/{x["img"]}.jpg'
        dc = f' data-clip="{clip}"' if clip else ''
        kd = ''
        if clip == 'x_q3':
            kd = '<div class="kd" data-caps="x_q3">' + json.load(open(f'{D}/gif/caps_x_q3.json'))[0] + '</div>'
        out += f'''<div class="bk{" rv" if i % 2 else ""}"><div class="ph"{dc} style="background-image:url({src});background-position:{x["fx"]}">{kd}</div>
<div class="obi"><div class="k">店員手寫推薦 NO.{x["n"]}</div><div class="h">{x["line"]}</div><div class="s">365 位作家<br>每天一頁</div></div>
<div class="desk"><div class="pop"><div class="pin">{pin()}</div><div class="bar">推薦給<span>NO.{x["n"]}</span></div><div class="for">這本書，推薦給</div><div class="who">{x["who"]}</div><div class="v">{x["voice"]}</div></div>
<div class="mk"><div class="rb"></div><img src="img/{x["pg"]}.jpg"></div></div></div>'''
        out += '</div></section>' if i == 0 else '</section>'
    return out


def how(i, sid, h, lead, clip, step, en, dark=False):
    return f'''<section id="{sid}" class="how{' dark' if dark else ''}"><div class="hd"><span class="chip">閱讀指南<i>HOW TO USE 0{i}</i></span>
<h2>{h}</h2><div class="lead">{lead}</div></div>
<div class="mv"><div class="ph" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div>
<div class="ob"><span class="k">STEP 0{i}</span>{step}<span class="e">{en}</span></div></div></section>'''


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
caps6 = json.load(open(f'{D}/gif/caps_x_c1.json'))[0]
LB = [('l', 36, '1', '月份'), ('r', 36, '2', '節氣<br>倒數日'), ('l', 80, '3', '大日期'),
      ('r', 156, '4', '今日指南'), ('l', 210, '5', '作家語錄'), ('r', 304, '6', '作者出處')]
lbs = ''
for side, y, n, t in LB:
    lbs += f'<div class="lb {side}" style="top:{y-28}px"><b>{n}</b><br>{t}</div>'
    lbs += f'<i class="ln" style="{"left:70px" if side == "l" else "right:66px"};width:{40 if side == "l" else 44}px;top:{y}px"></i>'

W = [('w1', 'Queenie Kao'), ('w2', '周慕姿'), ('w3', '喬心誌'), ('w4', '林達陽'), ('w5', '沈希默'), ('w6', '知寒'), ('w7', '連俞涵'), ('w8', '陳繁齊')]
wr = ''.join(f'<figure><div class="im" style="background-image:url(img/{a}.jpg)"></div><figcaption>{b}</figcaption></figure>' for a, b in W)
C6 = [('c1', '餘燼', 'EMBER'), ('c2', '暮槿', 'DUSK'), ('c3', '亞麻', 'LINEN'), ('c4', '靜灣', 'BAY'), ('c5', '藤花', 'WISTERIA'), ('c6', '初瀨', 'SHOAL')]
g6 = ''.join(f'<figure><div class="im" data-c6="x_{a}" style="background-image:url(gif/clips/x_{a}/001.jpg)"></div><figcaption>{b}<small>{e}</small></figcaption></figure>' for a, b, e in C6)
sp = ''.join(f'<i class="sp" style="left:{l}%;top:{t}%;animation-delay:{d}s"></i>' for l, t, d in [(8, 18, 0), (90, 70, .5), (14, 76, 1), (80, 16, 1.5), (50, 88, 2)])

body = s03() + f'''
<section id="s03b"><div class="xm"><div class="sh"></div>{sp}<div class="rib">現貨直出</div>
<div class="sm">IN STOCK • READY TO SHIP</div><div class="big">熱騰騰到貨</div><div class="ft">店員已經幫你包好，等你帶回家</div></div></section>
<section id="s04">
  <div><div class="n">365</div><div class="c">句作家語錄</div></div>
  <div><div class="n">6<small>款</small></div><div class="c">年度代表色</div></div>
  <div><div class="n">2<small>種</small></div><div class="c">經典款・底座款</div></div>
</section>
<section id="s05" class="dark"><div class="hd"><div class="eyebrow">一年 365 頁</div><h2>每一天，<br>都是一張風景</h2>
<div class="lead">大日期、今日指南、作家語錄、農曆節氣，<br>一頁全彩，每天換一種心情。</div></div>
<div class="wall">{wall}</div></section>
''' + how(1, 's05a', '早上撕下一頁，<br>讀一句給今天的話', '陽光透過紙頁，<br>今天的那句話剛好亮起來。', 'x_tear', '撕下今天', 'TEAR') + f'''
<section id="s06"><div class="hd"><div class="eyebrow">一頁有什麼？</div><h2>一頁一句，<br>每天都設計過</h2></div>
<div class="box"><div class="cap" data-caps="x_days">{caps[0]}</div>
<div class="pgv"><div class="pgi" data-clip="x_days" style="background-image:url(gif/clips/x_days/001.jpg)"></div>{lbs}</div></div></section>
''' + how(2, 's06a', '跟喜歡的人分享，<br>你喜歡的那段話', '今天的語錄想到了誰？<br>傳給你在乎的他／她', 'x_share', '交換一句', 'SHARE', dark=True) \
    + how(3, 's07', '撕下來的每一頁，<br>貼成一面風景牆', '一天一張，貼滿一整面，<br>一年的心情都看得見。', 'x_wall', '貼成風景牆', 'COLLECT') + f'''
<section id="s09" class="dark"><div class="hd"><div class="sign">本店作家專區</div><div class="eyebrow">作家陣容</div><h2>他們為了 2027 的你，<br>預備這段話</h2>
<div class="lead">365 位作家，用最深刻的體悟<br>陪你走過未來每一天</div></div>
<div class="wr">{wr}</div><div class="tip">還有更多作家與好書摘句，一起陪你 365 天</div></section>
<section id="s10"><div class="hd"><div class="eyebrow">年度代表色</div><h2>六款顏色，<br>挑一個明年的代表色</h2></div>
<div class="kind6" data-caps6>{caps6}</div><div class="g6">{g6}</div><div class="nt">實拍色彩依螢幕顯示略有差異</div></section>
<section id="s11"><div class="ph"></div><div class="st"><div class="h"><span>版權頁</span><span>COLOPHON</span></div>
<div class="row"><span class="k">書名</span><span class="v">2027 煦暖曆</span></div>
<div class="row"><span class="k">尺寸</span><span class="v">9 × 16 公分，直式手撕</span></div>
<div class="row"><span class="k">造型</span><span class="v">經典款、底座款</span></div>
<div class="row"><span class="k">內容</span><span class="v">365 頁全彩，大日期、今日指南、作家語錄、農曆、倒數日</span></div>
<div class="row"><span class="k">外盒</span><span class="v">厚磅紙盒，可直接送禮</span></div>
<div class="row"><span class="k">重量</span><span class="v">520 g（含外盒 665 g）</span></div></div></section>
<section id="s12"><div class="ph" style="background-image:url(img/end.jpg)"></div><div class="shade"></div>
<div class="tx2"><div class="a">每天一句，<br>剛好接住今天的你</div><div class="b">日子不一定順，<br>但每天早上，都有人先對你說聲早安。</div></div>
<div class="nx">找不到要送什麼的時候，<br>就送一整年的好句子。<div class="tg">明天，還有一位作家在等你</div></div></section>
'''
html = f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>煦暖曆落地頁 v14</title><style>{CSS}</style></head><body>{body}</body></html>'
open(f'{D}/page.html', 'w').write(html)
print('ok', len(html))
