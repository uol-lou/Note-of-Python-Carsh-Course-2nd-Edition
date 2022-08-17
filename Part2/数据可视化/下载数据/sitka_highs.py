import csv
import matplotlib.pyplot as plt
# 添加日期
from datetime import datetime

filename = "sitka_weather_07-2018_simple.csv"

# with 语句适用于对资源进行访问的场合，
# 确保不管使用过程中是否发生异常都会执行必要的“清理”操作，
# 释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
with open(filename) as f:
    # The "iterable" argument can be any object that returns a line
    # of input for each iteration, such as a file object or a list.  The
    # optional "dialect" parameter is discussed below.  The function
    # also accepts optional keyword arguments which override settings
    # provided by the dialect.
    # 每次返回一行，形式为列表。
    # The returned object is an iterator.  Each iteration returns a row
    # of the CSV file (which can span multiple input lines).
    reader = csv.reader(f)
    # next()函数用于传入阅读器的对象
    # 它用来返回文件的下一行
    # 这里由于只调用了一次，所以只返回了第一行
    head_row = next(reader)
    print(head_row)

    # 调用enumerate() 来获取每个元素的位置及其索引值，
    for index, column_header in enumerate(head_row):
        print(index, column_header)

    highs = []
    dates = []
    lows = []
    # 按照每行列表来读取数据
    for row in reader:
        # datetime 中设置日期和时间格式的实参
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        # 每次执行循环时，都索引第五处的数据附加到highs末尾。并将其转换为int格式
        high = (5 * (int(row[5]) - 32)) / 9
        low = (5 * (int(row[6]) - 32)) / 9
        # high = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(highs)

    plt.style.use("seaborn")
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(dates, highs, c="red")

    ax.set_title("Highst Tempuratur in 2018,7", fontsize=20)
    ax.set_xlabel("date", fontsize=10)
    ax.set_ylabel("Tempuratur(C)", fontsize=16)
    # 对x轴进行自动适应，目前情况会变成斜体
    fig.autofmt_xdate()
    # Change the appearance of ticks, tick labels, and gridlines.
    # 更改刻度、刻度标签和网格线的bot外观。
    ax.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
