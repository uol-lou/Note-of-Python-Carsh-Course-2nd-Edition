responses = {

}

polling_name = True

while polling_name:
    name = input("What is your name?")
    response = input("Which mountain is your favourite?")

    # 将回答存到字典中,name为字典title，response为字典内容
    responses[name] = response

    repeat = input("Any other?")
    if repeat == "no":
        polling_name = False
    elif repeat == "yes":
        continue
    # 这个地方应该不是这么写的，这样写内存会占用很多
    else:
        repeat = input("Yes or no?")

# 使用.item()来访问字典内容
for name, response in responses.items():
    print(name + "," + response)
