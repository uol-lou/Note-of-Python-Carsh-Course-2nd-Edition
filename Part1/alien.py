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

5