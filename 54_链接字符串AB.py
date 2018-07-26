list1 = []
list2 = []

string = input('输入一串字符：')

for i,v in enumerate(string):
    if i % 2 == 0:
        list2.append(v)
    else:
        list1.append(v)

print('新的字符串A为：{0}'.format(str(list2)))
print('新的字符串B为：{0}'.format(str(list1)))
