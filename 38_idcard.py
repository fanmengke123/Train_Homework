str1 = "程序员甲说：你知道我的生日吗?"
str2 = "程序员乙说：输入你的身份证号码"
str3 =  "123456199006277890"

year = str3[6:10]
month = str3[10:12]
day = str3[12:14]

print(str1)
print(str2)
print(str3)
print('你是%s年%s月%s日出生的，所以你的生日是%s月%s日'%(year,month,day,month,day))

