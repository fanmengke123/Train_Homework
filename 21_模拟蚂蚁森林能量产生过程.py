print("能量来源有如下几种：")
print("生活缴费、行走捐、共享单车、线下支付、网络购票")
#source = input("查询能量请输入能量来源，退出程序请输入0！\t")

while(1):
    source = input("查询能量请输入能量来源，退出程序请输入0! ")

    if source == "行走捐":
        print("200g")
    elif source == "生活缴费":
        print("300g")
    elif source == "共享单车":
        print("350g")
    elif source == "线下支付":
        print("380g")
    elif source == "网络购票":
        print("500g")
    elif source == "0":
        break
    else:
        print("您的输入有误！")
