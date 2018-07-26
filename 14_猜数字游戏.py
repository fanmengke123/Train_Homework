import random
number = random.randint(1,10)
input_number = int(input("请您输入您想输入的数字："))

if number == input_number:
    print("胜利")
else:
    print("失败，你是一个loser")
