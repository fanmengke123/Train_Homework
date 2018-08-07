file = open('/home/fanmengke/桌面/wenjian.txt')

while True:

    line = file.readline()
    if not line.startswith('#'):
        print(line.rstrip())

    if len(line) == 0:
        break

file.close()
