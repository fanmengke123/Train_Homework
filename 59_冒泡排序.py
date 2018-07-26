L = []
while True:
    num = int(input('输入一个整数：'))
    if num == 0:
        break
    L.append(num)
# print(L)
def maopao_max_min(L):
    # pass
    #比较的趟数
    for i in range(len(L) - 1):
        #一趟中比较的次数
        for j in range(len(L) - i - 1):
            if L[j] < L[j + 1]:
                L[j],L[j + 1] = L[j + 1],L[j]
    return L

def maopao_min_max(L):
    # pass
    #比较的趟数
    for i in range(len(L) - 1):
        #一趟中比较的次数
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j],L[j + 1] = L[j + 1],L[j]
    return L

print('从小到大排序为：{0}'.format(maopao_min_max(L)))
print('从大到小排序为：{0}'.format(maopao_max_min(L)))
