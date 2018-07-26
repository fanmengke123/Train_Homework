age = int(input("输入年龄："))
subject = input("输入专业：")
college = input("输入是否重点大学：")

if (subject == "电子信息工程专业" and age > 25) or (subject == "电子信息工程专业" and college == "重点大学") or (age < 28 and subject == "计算机专业"):
    print("您被录取了")
else:
    print("抱歉，您未达到面试要求")
