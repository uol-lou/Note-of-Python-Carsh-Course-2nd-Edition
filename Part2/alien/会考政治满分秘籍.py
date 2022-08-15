print("我是懒狗~")
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片

lena = mpimg.imread('doge.jpg')
lena.shape

plt.imshow(lena)  # 显示图片
plt.axis('off')  # 不显示坐标轴
plt.show()
