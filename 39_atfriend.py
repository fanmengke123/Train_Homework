str1 = "@大学生精英班@扎克伯格@俞敏洪"
print("您@的好友有：")
a = str1.split('@')
for i in a[1:]:
    if a != '':
        print(i)


