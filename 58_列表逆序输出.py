info = [1,2,3,4,5]
print('方法一：')
info.reverse()
print(info)

info = [1,2,3,4,5]
print('方法二：')
print(info[::-1])

'''未实现'''
# info = [1,2,3,4,5]
# print('方法三：')
# for i in (0,len(info)//2):
#     info[i],info[len(info) - 1 - i] = info[len(info) - 1 - i],info[i]
# print(info)
