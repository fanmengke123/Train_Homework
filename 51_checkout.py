price_list = []

def fun_checkout(*args):
    discount_amount = 1
    sum_price = 0
    for price in set(price_list):
        sum_price += price
    if sum_price >= 500 and sum_price < 1000:
        discount_amount = sum_price * 0.9
    elif sum_price >= 1000 and sum_price < 2000:
        discount_amount = sum_price * 0.8
    elif sum_price >= 2000:
        discount_amount = sum_price * 0.7
    elif sum_price >= 3000:
        discount_amount = sum_price * 0.6
    print('合计金额为：{0}\t 应付金额为：{1}'.format(sum_price,discount_amount))



while True:
    price = float(input("输入商品金额（输0表示输入完毕）"))
    price_list.append(price)

    if price == 0:
        break

fun_checkout(price_list)
