# 每次期末考完都意味着很长一段时间的Emo...

# 绘制简单图纸
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 使用plt库的内置样式
plt.style.use("seaborn")

# 变量fig表示整张图片，变量ax表示图片中的各个图表
# fig表示这张画布，ax是指画笔，通过ax.plot(squares)表示这条线
fig, ax = plt.subplots()

# linewidth用于 给定先粗细
# input_values第一个参数为x轴，squares第二个参数为Y轴
ax.plot(input_values, squares, linewidth=3)

# 设定标题 无法使用中文
ax.set_title("quadra", fontsize=24)
# 设定X轴
ax.set_xlabel("value", fontsize=14)
# 设定Y轴
ax.set_ylabel("value^2", fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 绘制散点图 s = 200 意为点的大小
ax.scatter(3.3, 3.3,s =200)
ax.scatter(input_values,squares,s = 100)

for i in input_values:
    print("(",input_values[i-1],",",squares[i-1],")")

plt.show()
