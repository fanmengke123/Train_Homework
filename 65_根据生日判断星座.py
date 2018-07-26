'''根据生日可以判断所属星座.例如:生日为7月1日，属于巨蟹座。
编程实现根据输入的出生月份和日期判断所属星座。'''

'''十二星座中，排列第一的就是水瓶座，也叫做宝瓶座，起止时间为1月20日～2月18日；
排列第二的是双鱼座，起止时间为2月19日～3月20日；
排列第三的是白羊座，也叫做牧羊座，起止时间为3月21日～4月19日；
排列第四的是金牛座，起止时间为4月20日～5月20日；
排列第五的是双子座，起止时间为5月21日～6月21日；
排列第六的是巨蟹座，起止时间为6月22日～7月22日；
排列第七的是狮子座，起止时间为7月23日～8月22日；
排列第八的是处女座，也叫做室女座，起止时间为8月23日～9月22日；
排列第九的是天秤座，起止时间为9月23日～10月22日；
排列第十是的天蝎座，起止时间为10月23日～11月21日；
排列第十一的是射手座，也叫做人马座，起止时间为11月22日～12月21日；
排列第十二的是摩羯座，也叫做山羊座，因为“羯”就是一种羊，起止时间为12月22日～1月19日。
'''

# def xingzuo(month,day):
#     if (month == 1 and day >= 20) or (month == 2 and day <= 18):
#         return '水瓶座'
#     elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#         return '双鱼座'
#     elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
#         return '白羊座'
#     elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#         return '金牛座'
#     elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
#         return '双子座'
#     elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
#         return '巨蟹座'
#     elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#         return '狮子座'
#     elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#         return '处女座'
#     elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#         return '天秤座'
#     elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#         return '天蝎座'
#     elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#         return '射手座'
#     elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
#         return '摩羯座'


def xingzuo(month, day):
    n = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
'巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']

    day1 = [20,19,21,20,21,22,23,23,23,23,22,22]

    if day < day1[month - 1]:
        return n[month - 1]
    else:
        return n[month]


month = int(input('请输入月份：'))
day = int(input('请输入日期：'))

result = xingzuo(month, day)
print('%d月%d日星座为：%s'%(month,day,result))
