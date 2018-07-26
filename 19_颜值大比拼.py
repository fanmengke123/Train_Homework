height = int(input("请输入身高："))
value = int(input("请输入身价："))
face = int(input("请输入颜值分："))

if height >= 180 and value >= 1000000 and face >= 99:
    print("高富帅")
elif value >= 1000000 and face >= 99 and (height < 180 and height > 160):
    print("富帅")
elif (value < 1000000 and value > 100) and(height < 180 and height > 160) and face >= 99:
    print("帅")
elif height <= 160 and value <= 100 and face <= 60:
    print("矮矬穷")
