for i in range(100,1000):
    #i的百位数 
    a = i // 100
    #i的十位数  
    b = i % 100 // 10
    #i的个位数  
    c = i % 10
    if i == a**3 +b**3 +c**3:
        print(i)
    i = i + 1
