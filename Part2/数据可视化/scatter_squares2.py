# 绘制1000个点
import matplotlib.pyplot as plt

x_values = range(1, 1000)
# 记住这个写法
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig,ax = plt.subplots()

ax.scatter(x_values,y_values,s =10)

# 设定XY轴的取值范围
ax.axis([0,1000,0,1100000])

plt.show()