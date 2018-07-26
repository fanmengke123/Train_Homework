s = input('请输入一串字符：')

string = ''
for i in s:
    if i.isalpha():
        string = string + i
    else:
        continue

# print(string)
dic = {}
for i in string.lower():
    if i in dic:
        dic[i] = (dic[i] + 1)
    else:
        dic[i] = 1

print(dic)
