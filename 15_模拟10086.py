print("欢迎使用10086自助查询系统！")
print("输入1：查询当前余额")
print("输入2：显示您当前剩余流量")
print("输入3：显示您当前的剩余通话，单位为分钟")
input_number = int(input("请输入您要查询的功能："))
if input_number == 1:
    print("您当前余额为15元")
elif input_number == 2:
    print("您当前剩余流量2G")
elif input_number == 3:
    print("您当前剩余通话200分钟")

