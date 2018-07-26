import math
#两条直角分别为a，b
a = int(input("输入直角边a："))
b = int(input("输入直角边b："))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print("斜边长为：%d"%c)	
