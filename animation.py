#https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
#を参照
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#figureと、アニメーションしたい要素のセットアップ
#lineには後からデータを入れる
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

#axisと要素を初期化
#アニメーションが行われるベースフレームを作る
#lineはそれぞれのフレームの事に何をアップデートするかを伝えるためのオブジェクト
def init():
    line.set_data([], [])
    return line

#時系列グラフ
#パラメータiはフレームの番号: iに依存するsin波を描く
#lineを返して何を描画するかを伝える
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

#blit=True: 変更部分だけを描画する
#frame分のアニメーション
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

#アニメーションをmp4で保存
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()