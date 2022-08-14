#让用户选择何时退出
message = ""
while message != "quit":
    message = input("Say something:")

    #如果输入的是quit，也不会打出quit
    if message != "quit":
        print(message)

while True:
    message = input("Say something2:")

    #最后也不会把quit打印出来
    if message == "quit":
        break
    else:
        print(message)