squares1 = []
for value in range(1,6):
    square = value**2
    squares1.append(square)

print(squares1)

squares2 = []
for value in range(1,6):
    squares2.append(value**2)

print(squares2)

# **指乘方运算

print(min(squares2))
print(max(squares2))
print(sum(squares2))

# 列表解析
squares3 = [value**2 for value in range(1,11)]
print(squares3)

