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

#返回字典
def
