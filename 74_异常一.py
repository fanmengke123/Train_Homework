try:
    height = int(input('请输入您的身高：'))
    weight = int(input('请输入您的体重：'))
    standard_weight = height - 100

    if height >= 30 and height <=250:
        if weight > standard_weight * 0.95 and weight < standard_weight * 1.05:
            print('体重正常')
        elif weight < standard_weight * 0.95:
            print('体重不达标')
        elif weight > standard_weight * 1.05:
            print('体重超标')


    ex1 = Exception('您的身高也忒低了点吧,辣鸡')
    ex2 = Exception('您的身高是怎么长的啊,这么吊')

    if height < 30:
        raise ex1

    elif height > 250:
        raise ex2



except ValueError:
    print('请输入正确的数字')

except Exception as result:
    print('未知错误:{}'.format(result))

