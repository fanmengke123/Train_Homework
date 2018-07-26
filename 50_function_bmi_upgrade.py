def function_bmi_upgearde(**kwargs):

        print('=========={0}=========='.format(list_info[i]['name']))
        print("身高：{0}米\t 体重：{1}kg".format(list_info[i]['身高'],list_info[i]['体重']))
        BMI = list_info[i]['体重'] / (list_info[i]['身高'] ** 2)
        print("BMI指数为：{0}".format(BMI))


        if BMI < 18.5:
            print('您的体重过轻了')
        elif BMI >= 18.5 and BMI < 24.9:
         print('您的体重在正常范围，继续保持哦')
        elif BMI >= 24.9 and BMI < 29.9:
            print('您有点过重了哦，注意减肥')
        elif BMI >= 24.9:
            print('您太胖了，放弃治疗吧')
        print("")
        # print('BMI指数为：{0}'.format(BMI))


list_info = [{'name':'绮梦','身高':1.7,'体重':65},{'name':'零语','身高':1.78,'体重':50},
             {'name':'黛兰','身高':1.72,'体重':66},{'name':'紫轩','身高':1.8,'体重':75},
             {'name':'冷伊一','身高':1.75,'体重':70}]

for i in range(0,len(list_info)):
    function_bmi_upgearde(**list_info[i])
