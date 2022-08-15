# 每次期末考完都意味着很长一段时间的Emo...

# 绘制简单图纸
import matplotlib.pyplot as plt

squares = [1, 4, 5, 13, 11]
# 变量fig表示整张图片，变量ax表示图片中的各个图表
# fig表示这张画布，ax通过ax.plot(squares)表示这条线
fig,ax = plt.subplots()
ax.plot(squares)

plt.show()
