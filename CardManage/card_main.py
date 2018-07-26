#! /usr/bin/python3

import card_tools

while True:
    card_tools.show_menu()


    action = input("请选择操作功能：")

    print("您选择的操作是：%s"%action)

    if action in ['1','2','3']:
        if action == '1':
            card_tools.new_cards()
        elif action == '2':
            card_tools.show_all()
        elif action == '3':
            card_tools.search_card()

    elif action == '0':
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print('输入错误，请重新输入！')
