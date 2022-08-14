# 列表之间移动元素
unconfirmed_user = ['a', 'b', 'c']
confirmed_user = [

]

while unconfirmed_user:
    # pop用法，移除列表最后一个元素，并返回它！
    current_user = unconfirmed_user.pop()

    print(current_user)
    confirmed_user.append(current_user)

for user in confirmed_user:
    # 执行后的会发现，列表顺序也是反转的吗
    print(user)
