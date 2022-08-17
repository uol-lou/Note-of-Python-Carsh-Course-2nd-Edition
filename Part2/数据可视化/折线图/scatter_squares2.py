# 绘制1000个点
import matplotlib.pyplot as plt

x_values = range(1, 1000)
# 记住这个写法
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

# color设置颜色 可以使用固定模板如red、blue，也可以使用RGB相对于1的系数值
ax.scatter(x_values, y_values, c=[0, 0.8, 0], cmap=plt.cm.Blues, s=1)

# 设定XY轴的取值范围
ax.axis([0, 1000, 0, 1100000])

plt.show()

# 将图表保存
plt.savefig("squares.png", bbox_inches='tight')
