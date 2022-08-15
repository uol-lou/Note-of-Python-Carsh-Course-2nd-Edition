# 练习返回值

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print(get_formatted_name("jimi", "saklei"))


# 若函数的形参不一定存在，则可以给它一个空白的默认值
# "middle_name" = ""意味给一个空的middle name 如果最后不定义也可以
def get_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name


print(get_full_name("Masaaki", "sakley"))


# 传递列表
def greeting(names):
    # 自动识别列表并执行
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)


username = ["hanna", "joe", "lui"]
greeting(username)
# 切片表示方法
greeting(username[:])


