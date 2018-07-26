list1 = [{'车次':'T40','出发站-到达站':'长春-北京','出发时间':'00:12','到达时间':'12:20','历时':'12:08'},
        {'车次':'T298','出发站-到达站':'长春-北京','出发时间':'00:06','到达时间':'10:50','历时':'10:44'},
        {'车次':'Z158','出发站-到达站':'长春-北京','出发时间':'21:06','到达时间':'21:06','历时':'08:18'},
        {'车次':'Z62','出发站-到达站':'长春-北京','出发时间':'21:58','到达时间':'06:08','历时':'8:20'}]

print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时')
for i in list1:
    print('{0}\t\t{1}\t\t{2}\t\t\t{3}\t\t\t{4}'.format(i['车次'],i['出发站-到达站'],i['出发时间'],i['到达时间'],i['历时']))

checi = ''
start_end = ''
start_time = ''
for j in list1:
    checi = checi + j['车次'] + ' '
    start_end = start_end + j['出发站-到达站'] + ' '
    start_time = start_time + j['出发时间']  + ' '
# print(checi)
# print(start_time)
# print(start_end)
L1 = checi.strip().split(' ')
L2 = start_end.strip().split(' ')
L3 = start_time.strip().split(' ')

# print(L)
checi1 = input('请输入要购买的车次：')
if checi1 in L1:
    person = input('请输入乘车人：')
    index = L1.index(checi1)
    print('您已购%s车次 %s %s开，请%s尽快换区纸质车票。 【铁路客服】'%(checi1,L2[index],L3[index],person))
else:
    print('无本班次列车,请重新购买')
    exit(0)
