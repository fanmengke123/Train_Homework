count = 0
for i in range(1,100):
    if i % 7 == 0 or i % 10 == 7:
        count += 1
    else:
        continue

print('从数到99共抬腿{0}次'.format(count))
