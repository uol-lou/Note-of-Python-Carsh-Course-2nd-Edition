# 读取文件内容 每行读取 自动补齐enter
# 这样写的话，会多一列空行，因为read到达文件末尾时会返回一个空字符串
with open('file.txt') as file:
    contents = file.read()
print(contents)
# 这样就可以删除最后多出来的空行
print(contents.rstrip())

#逐行读取
filename = open('file.txt')
for line in filename:
    print(line)
    print(line.rstrip())