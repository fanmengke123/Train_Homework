user = 'fmk'
passwd = '123456'
money = 10000
print("欢迎来到自助银行取款，请登录!")
user_name = input("请输入你的账号：")
password = input("输入你的密码：")
if user_name == user and passwd == password:
    print("欢迎您%s"%user_name)
    draw_money = int(input("请输入您的取款金额："))
    if draw_money < money:
        surplus_money = money - draw_money
        print("您取了%d元钱，剩余%d元"%(draw_money,surplus_money))
    else:
        print("没钱，取个毛的钱！")
else:
    print("非法账户")
