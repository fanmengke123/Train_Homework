triangle = [[1],[1,1]]

for i in range(2,6):
    
    line = [1]
    for j in range(0,i - 1):
        line.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
    
    line.append(1)
    triangle.append(line)

for a in triangle:
    print(a,end = '\n')
