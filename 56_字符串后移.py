string = input('请输入一串字符：')

new =string[-1] + string[0:-1]
print('新的字符串为：{0}'.format(new))
