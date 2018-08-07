file = open('/home/fanmengke/桌面/number.txt')

number = file.readline()
number_list = []
for i in number.split(' '):
    number_list.append(int(i))

number_list.sort()
print(number_list)

file.close()
