print("为了您和其他人的安全，严禁酒后驾车！")

alcoholicity = int(input("请输入每100毫升血液中的究竟含量："))

if alcoholicity <= 10:
    print("您还构不成饮酒行为，可以开车，但是要注意安全！")
elif alcoholicity > 10 and alcoholicity <= 90:
    print("您已经达到了酒后驾驶的标准，请不要开车！")
elif alcoholicity > 10 and alcoholicity <= 90:
    print("您已经达到了酒后驾驶的标准，请不要开车！")
else:
    print("您已经达到了醉酒驾驶的标准，请千万不要开车！")

