def function_bim(name, height, weight):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        print('您的体重过轻了')
    elif BMI >= 18.5 and BMI < 24.9:
        print('您的体重在正常范围，继续保持哦')
    elif BMI >= 24.9 and BMI < 29.9:
        print('您有点过重了哦，注意减肥')
    elif BMI >= 24.9:
        print('您太胖了，放弃治疗吧')
    print('{0}的BMI指数为：{1}'.format(name,BMI))

print("{0}的身高为：{1}米\t 体重：{2}kg".format('路人甲', 1.83, 60))
function_bim('路人甲', 1.83, 60)
print("")
print("{0}的身高为：{1}米\t 体重：{2}kg".format('路人乙', 1.6, 50))
function_bim('路人乙', 1.6, 50)
