"""煦暖曆落地頁實拍動圖片段（2026-11-24）。麻豆素材，裁 4:5，彩度 1.3、對比 1.04（麻豆原色已偏柔，不拉到 1.45 以免膚色過艷）。"""
import subprocess,os,shutil,sys
from concurrent.futures import ThreadPoolExecutor
M="/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/煦暖曆/毛片/麻豆_影片_0812/"
FPS=15
C={
 'x_tear':  (M+'C0246.mp4', 2.6, 7.4, 1.2, 0.30),
 'x_share': (M+'C0234.mp4', 3.0, 9.6, 1.5, 0.40),
 'x_wall':  (M+'C0421.mp4', 1.0, 11.8, 2.0, 0.45),
 'x_flip':  (M+'C0252.mp4', 0.0, 9.6, 2.0, 0.40),
}
def run(item):
    n,(src,t0,t1,sp,cy)=item
    od=os.path.dirname(os.path.abspath(__file__))+f'/clips/{n}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
    vf=(f"setpts=PTS/{sp},fps={FPS},crop=iw:iw*1.25:0:(ih-iw*1.25)*{cy},"
        f"scale=1080:1350:flags=lanczos,eq=saturation=1.3:contrast=1.04")
    subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',src,'-vf',vf,'-q:v','2',f'{od}/%03d.jpg'],check=True,stdin=subprocess.DEVNULL)
    return n,len(os.listdir(od))
sel=sys.argv[1:] or list(C)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,[(k,C[k]) for k in sel]): print(r)
