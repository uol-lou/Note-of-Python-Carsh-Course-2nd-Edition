# 在字典中存储列表
pizza = {'crust': ['thick'],
         'troppings': ['mushroom', 'extra cheese']
         }

# 概述所点的披萨
print(f"what you order is {pizza['crust']}")

for tropping in pizza['troppings']:
    print(tropping)

# 遍历字典中的所有列表的方法 ps：一定要是列表！否则会把一个字符拆分成一个一个的字母
for crust, tropping in pizza.items():
    print(crust.title())
    for tro in tropping:
        print(tro)


# 传递任意数量的实参
def make_pizza(*troppings):
    print(troppings)


# 最终的实参会被封装到一个元组中
make_pizza(1, 2, 3)
make_pizza('a', 'b', 'c')


# 注意实参和任意数量实参的位置
def make_pizza2(size, *tropping):
    print(size, tropping)


make_pizza2(12, "a")


# 创建任意数量的键值对型实参
def build_profil(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


# **user_info创建的是名称值对，它会被收录到字典一个字典中
user_profile = build_profil("albert", "einstein", local='abc', field='123')
print(user_profile)
