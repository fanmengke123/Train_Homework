str1 = "I,love,python"
str2 = "aabbccddee"
str3 = "ab2b3n5nn2n67mm4n2"

print(str1[2:6])

str22 = 'dd'
str23 = 'ff'
print(str2.replace(str22,str23))


count = str3.count('n')
print("出现的次数为：%d"%count)

dic = {}
for i in str3:
    if i in dic:
        dic[i] = (dic[i] + 1)
    else:
        dic[i] = 1

print(dic)


