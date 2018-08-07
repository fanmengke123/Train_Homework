class Credit:
    def __init__(self,number,passwd = '123456'):
        self.number = number
        if passwd == '123456':
            print('信用卡' + number + '的默认密码为' + passwd)
        else:
            print('重置信用卡' + number + '的密码为' + passwd)

credit = Credit('123456789865432')
credit1 = Credit('123456789865432','456789')
