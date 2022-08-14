#在字典中存储列表
pizza = {'crust':['thick'],
         'troppings':['mushroom','extra cheese']
}

# 概述所点的披萨
print(f"what you order is {pizza['crust']}")

for tropping in pizza['troppings']:
    print(tropping)

#遍历字典中的所有列表的方法 ps：一定要是列表！否则会把一个字符拆分成一个一个的字母
for crust,tropping in pizza.items():
    print(crust.title())
    for tro in tropping:
        print(tro)