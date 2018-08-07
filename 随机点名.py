import time
import random


def read_info():
    with open('name.txt', 'r') as f:
        resu = f.read()
        result = resu.split(',')
    return result

s_list = read_info()

for i in range(3, 0, -1):
    time.sleep(1)
    print(i)
print(random.choice(s_list))
