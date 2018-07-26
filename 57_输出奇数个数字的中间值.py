N = int(input('输入一个整数：'))
while True:
    if N % 2 == 0:
        print('您输入的数字有误,请重新输入')
        N = int(input('重新输入的数字为：'))
    else:
        # print(N)
        break
L = []
for i in range(0,N):
    num = int(input('输入{0}个整数：'.format(N)))
    L.append(num)
print('中间位置的数字为{0}'.format(L[(len(L)) // 2]))
