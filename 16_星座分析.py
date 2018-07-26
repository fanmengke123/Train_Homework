print("请输入您的名字：")
name = input()

print("水瓶座请输入：1")
print("双鱼座请输入：2")
print("白羊座请输入：3")
print("金牛座请输入：4")
print("双子座请输入：5")
print("巨蟹座请输入：6")
print("狮子座请输入：7")
print("处女座请输入：8")
#print("请输入您要选择的编号：")
number = int(input("请输入您要选择的编号："))
if number == 1:
    print("%s,您好！水瓶座的您分析结果：日期是1月20~2月18，性格是XXX"%name)
elif number == 2:
    print("%s,您好！双鱼座的您分析结果：日期是2月19~3月20，性格是XXX"%name)
elif number == 3:
    print("%s,您好！白羊座的您分析结果：日期是3月21~4月19，性格是XXX"%name)
elif number == 4:
    print("%s,您好！金牛座的您分析结果：日期是4月20~5月20，性格是XXX"%name)
elif number == 5:
    print("%s,您好！双子座的您分析结果：日期是5月21~6月21，性格是XXX"%name)
elif number == 6:
    print("%s,您好！巨蟹座的您分析结果：日期是6月21~7月22，性格是XXX"%name)
elif number == 7:
    print("%s,您好！狮子座的您分析结果：日期是7月23~8月22，性格是XXX"%name)
elif number == 8:
    print("%s,您好！处女座的您分析结果：日期是8月23~9月22，性格是XXX"%name)


