dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# 访问元组的方法

# dimensions[0] = 250会报错，元组无法直接修改

dimensions1 = (100 , )
print(dimensions1)
print(dimensions1[0])

# 元组一般带括号，且是由括号标识的

for dimension in dimensions:
    print(dimension)

# 遍历元组

dimensions = (400,100)
print(dimensions)

# 虽然不能修改元组元素，但可以给元组的元素重新赋值
# 即重新定义所有的元组

