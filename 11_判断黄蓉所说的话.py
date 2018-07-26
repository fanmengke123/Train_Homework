input_number = int(input("请输入一个整数："))
if input_number % 3 == 2 and input_number % 5 == 3 and input_number % 7 == 2:
    print(input_number)
else:
    print("输入有误")
