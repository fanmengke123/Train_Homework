print("---欢迎进入跳一跳小游戏，输入0即可退出---")
print("游戏即将开始，请准备！")
print("有效输入为(中心、音乐模块、微信支付模块)")
while(1):
    module = input("请输入：")
    if module == "中心":
        print("您的分数为32")
    elif module == "音乐模块":
        print("您的分数为30")
    elif module == "微信支付模块":
        print("您的分数为42")
    elif module == "0":
        break
    else:
        print("输入错误，请重新输入！")
