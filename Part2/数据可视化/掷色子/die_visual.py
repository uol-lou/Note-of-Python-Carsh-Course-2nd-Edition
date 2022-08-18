# 掷色子的图表

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()
results = []

# 将掷色子的结果存到一个列表中
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

# 分析结果

frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 绘制直方图
# 对结果进行可视化
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Reslut"}
y_axis_config = {"title": "Result_Frequency"}

my_layout = Layout(title="Result of 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")

