
# 保存所有的名片字典
card_list = []


def show_menu():
    print('*' * 50)
    print("欢迎使用【名片管理系统】V1.0" + "\n\n" +
          "1. 新建名片" + "\n" +
          "2. 显示名片" + "\n" +
          "3. 查询名片" + "\n\n" +
          "0. 退出系统")
    print('*' * 50)


# show_menu()

def new_cards():
    print("******功能：新建名片******")
    print("")

    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号码：")
    email = input("请输入邮箱：")

    # 记录每个用户的具体信息
    card_dict = {'name': name, 'phone': phone, 'qq': qq, 'email': email}


    for i in card_list:
        if i['name'] == card_dict['name']:
            print('添加失败，该用户已存在')
            break
    else:
        card_list.append(card_dict)
        print(card_list)
        print("成功添加%s的名片" % card_dict['name'])
        print("")


def show_all():
    for i in ['姓名', '电话', 'QQ', '邮箱']:
        print(i, end='\t\t')
    print('')

    for a in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (a['name'], a['phone'], a['qq'], a['email']))

    if len(card_list) == 0:
        print("没有任何名片记录")


def search_card():
    name = input("输入您要查询的姓名：")
    for m in card_list:
        if name == m['name']:
            print('姓名\t\t电话\t\tQQ\t\t邮箱')
            print('%s\t\t%s\t\t%s\t\t%s\t\t' % (m['name'], m['phone'], m['qq'], m['email']))
            del_cards(m)
            break
    else:
        print("名片中没有%s这个名字" % name)


def del_cards(find_dict):
    action_str = input("请选择要执行的操作[1] 修改 [2] 删除 [0] 返回上级菜单")

    if action_str == '1':
        print('修改:')
        name = input("请输入修改后的姓名：")
        phone = input("请输入修改后的号码：")
        qq = input("请输入修改后的qq：")
        email = input("请输入修改后的email：")
        if len(name) > 0:
            find_dict['name'] = name
        else:
            name = find_dict['name']
        if len(phone) > 0:
            find_dict['phone'] = phone
        else:
            phone = find_dict['phone']
        if len(qq) > 0:
            find_dict['qq'] = qq
        else:
            qq = find_dict['qq']
        if len(email) > 0:
            find_dict['email'] = email
        else:
            email = find_dict['email']

        yuan = {'name': name, 'phone': phone, 'qq': qq, 'email': email}
        print(yuan)
        print('%s的名片修改成功' % yuan['name'])

    elif action_str == '2':
        card_list.remove(find_dict)
        print('删除成功！')

    elif action_str == '0':
        search_card()

