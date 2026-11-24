"""把收尾照片（DSC09495）日曆上的打樣內頁換成正式品 1/1 清晰印刷版。"""
import sys, glob, numpy as np, cv2
from PIL import Image, ImageEnhance, ImageFilter
S, PG = sys.argv[1], sys.argv[2]
DAY = '1.1'
base = Image.open(S+'/img/end_src.jpg').convert('RGB')
page = Image.open(glob.glob(PG+'/*_'+DAY+'.png')[0]).convert('RGB')
pw, ph = page.size
# 內頁上方約 3% 被盒蓋擋住
src = np.float32([[0, ph*0.03], [pw, ph*0.03], [pw, ph], [0, ph]])
dst = np.float32([[float(v) for v in p.split(',')] for p in sys.argv[3:7]])
M = cv2.getPerspectiveTransform(src, dst)
W, H = base.size
warped = cv2.warpPerspective(np.asarray(page), M, (W, H), flags=cv2.INTER_LANCZOS4)
mask = cv2.warpPerspective(np.full((ph, pw), 255, np.uint8), M, (W, H))
mask = cv2.erode(mask, np.ones((3, 3), np.uint8))
mask = cv2.GaussianBlur(mask, (5, 5), 0)
w = Image.fromarray(warped)
# 配合陽光：提亮、偏暖、略降對比
w = ImageEnhance.Brightness(w).enhance(float(sys.argv[7]) if len(sys.argv) > 7 else 1.25)
w = ImageEnhance.Contrast(w).enhance(0.82)
r, g, b = w.split(); r = r.point(lambda v: min(255, v*1.04)); b = b.point(lambda v: v*0.95); w = Image.merge('RGB', (r, g, b))
w = Image.blend(w, Image.new('RGB', w.size, (255, 246, 236)), 0.14)
out = Image.composite(w, base, Image.fromarray(mask))
out.save(S+'/img/end.jpg', quality=92)
print('ok')
