alien_o = {"color":"green","points":5}

print(alien_o['color'])
print(alien_o['points'])

alien_o['x_position'] = 0
alien_o['y_position'] = 25

print(alien_o)

alien_1 = {}

print(alien_1)
alien_1['color'] = 'green'
alien_1['points'] = 9

print(alien_1)



# 一行一行运行
alien_3 = {'x_position': 0 , 'y_position': 25 , 'speed': 'medium'}
print(f"Original position : {alien_3['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

# 新位置为旧位置加上移动距离

alien_3['x_position'] = alien_3['x_position'] + x_increment

print(f"new position:{alien_3['x_position']}")

# 删除键值

alien_4 = {"color":"green","points":5}
del alien_4["color"]
print(alien_4)

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range (30):
    new_alien = {"color":"green", "points" : 5, "speed":"slow" }
    aliens.append(new_alien)

for alien in aliens[:3]:  #:3表示前三个
    if alien["color"] == "green": #==用于判断 返回Boolean值， = 用于赋值
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("完成")

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien
