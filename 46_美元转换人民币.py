def change(dollar):
    return dollar * 6.28

dollar = float(input("请输入美元的金额："))

rmb = change(dollar)
print("转化后的人民币金额为：%.3f"%rmb)

