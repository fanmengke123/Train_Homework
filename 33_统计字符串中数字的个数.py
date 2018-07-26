count = 0
string = input("请输入：")
for i in string:
    if i.isdigit():
        count += 1
print(count)
