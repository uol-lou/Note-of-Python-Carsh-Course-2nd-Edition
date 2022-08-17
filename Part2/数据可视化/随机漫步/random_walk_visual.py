import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    rw = RandomWalk()

    rw.fill_walk()
    # rw.get_point_value()

    plt.style.use("classic")

    # figsize = (16,9) 意为图片的长宽尺寸，单位为一英寸
    fig, ax = plt.subplots(figsize=(16, 9))
    point_numbers = range(rw.num_point)

    # cmap告诉pyplot使用哪个颜色来映射，y值较小的为浅蓝色，y值较大的为深蓝色
    # colormaps reference
    # 记住cmap = plt.cm.Blues这个用法！！
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors="none", s=5)

    # 设定起始点为绿色，终点为红色
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c="red", edgecolors="none", s=100)

    # 隐藏X Y 轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Would you like another one? y/n")

    if keep_running == "n":
        break
