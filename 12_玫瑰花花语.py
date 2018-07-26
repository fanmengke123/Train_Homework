print("在古希腊神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，但是不同的朵数的玫瑰花代表的含义是不同的")

print("请输入您想送几多玫瑰花，我会告诉你玫瑰花的含义：")
number = int(input())
if number == 1:
    print("%s朵：你是我的唯一!"%number)
elif number == 3:
    print("%s朵：I Love You!"%number)
elif number == 10:
    print("%s朵：十全十美！"%number)
elif number == 99:
    print("%s朵：天长地久！"%number)
elif number == 108:
    print("%s朵：求婚!"%number)
elif number == 999:
    print("%s朵：土豪!"%number)
else:
    print("我也不知道了，你可以考虑送1朵，3朵，10朵......")
