import os
import sys

# 用户信息列表
user_list = []
# 学生信息列表
stu_list = []

def save_user_info():
    file = open('user.txt', 'w')
    for user in user_list:
        for i in user:
            file.write(i + ' ')
        file.write('\n')
    file.close()

def read_user_info():
    rs = os.path.exists('user.txt')
    if rs == True:
        file = open('user.txt', 'r')
        contents = file.readlines()
        for user in contents:
            user = user.strip('\n')
            list_1 = user.split(' ')
            list_1.pop()
            user_list.append(list_1)
            return user_list
        file.close()

def save_stu_info():
    file = open('imformation.txt', 'w')
    for student in stu_list:
        for people in student:
            file.write(people + ' ')
        file.write('\n')
    file.close()

def read_stu_info():
    rs = os.path.exists('imformation.txt')
    if rs == True:
        file = open('imformation.txt', 'r')
        contents = file.readlines()
        for people in contents:
            people = people.strip('\n')
            list_1 = people.split(' ')
            list_1.pop()
            stu_list.append(list_1)
            return stu_list
        file.close()

def register():
    name = input('输入您注册的用户名：')
    passwd = input('输入您注册的密码：')
    user_list.append([name, passwd])
    save_user_info()
    print('恭喜您注册成功,您现在可以进行登录使用该系统！')

def login():
    name = input('输入用户名：')
    password = input('输入密码：')
    if (u'\u4e00' <= name and name <= u'\u9fff') and (u'\u4e00' <= password and password <= u'\u9fff'):
        raise Exception('不能输入汉字')
    else:
        for user in user_list:
            if name == user[0] and password == user[1]:
                print('登陆成功')
                main()
            else:
                continue

def add_stu_info():
    name = input('请输入要添加的学生姓名：')
    age = input('请输入要添加的学生年龄：')
    sex = input('请输入要添加的学生性别：')
    phone = input('请输入要添加的学生电话号码：')
    stu_list.append([name, age, sex, phone])
    save_stu_info()
    print('============================')
    print('添加成功！！！')

def modify_stu_info():
    if len(stu_list) == 0:
        print('============================')
        print('没有学生信息,无法修改！')
        return  # 强制结束函数执行，return下所有代码都不会执行
    find_all()
    put = int(input('请输入您要修改的学生编号：'))
    while put not in range(0, len(stu_list)):
        put = int(input('编号不存在,请重新输入：'))
    name = stu_list[put]
    age = stu_list[put]
    sex = stu_list[put]
    phone = stu_list[put]
    new_name = input('请输入您修改后的姓名：')
    new_age = input('请输入您修改后的年龄：')
    new_sex = input('请输入您修改后的性别：')
    new_phone = input('请输入您修改后的电话号码：')
    stu_list[put] = [new_name, new_age, new_sex, new_phone]
    save_stu_info()
    print('============================')
    print('修改成功！！！')

def find_by_id():
    if (len(stu_list) == 0):
        print('   (列表为空,无法查询！)   ')
        return
    put = int(input('请输入您要查询学生的编号：'))
    while put not in range(0, len(stu_list)):
        put = int(input('编号不存在,请重新输入：'))
    find_list = stu_list[put]
    name = find_list[0]
    age = find_list[1]
    sex = find_list[2]
    phone = find_list[3]
    print('编号：%s,姓名：%s,年龄：%s,性别：%s,电话号码：%s' % (put, name, age, sex, phone))

def find_by_name():
    if (len(stu_list) == 0):
        print('   (列表为空,无法查询！)   ')
        return
    while True:
        name1 = input('请输入您要查询学生的姓名：')
        find = False
        for put in range(0, len(stu_list)):
            find_list = stu_list[put]
            name = find_list[0]
            age = find_list[1]
            sex = find_list[2]
            phone = find_list[3]
            if name == name1:
                find = True
                print('编号：%s, 姓名：%s, 年龄：%s, 性别：%s, 电话号码：%s' % (put, name1, age, sex, phone))
        if find == False:
            print('姓名不存在,请重新输入姓名：')
        else:
            break

def find_all():
    print('=========学生信息列表=========')
    if (len(stu_list) == 0):
        print('当前没有学生信息！')
    for put in range(0, len(stu_list)):
        find_list = stu_list[put]
        name = find_list[0]
        age = find_list[1]
        sex = find_list[2]
        phone = find_list[3]
        print('编号：%s, 姓名：%s, 年龄：%s, 性别：%s, 电话号码：%s' % (put, name, age, sex, phone))

def delete_by_id():
    if len(stu_list) == 0:
        print('============================')
        print('没有学生信息,无法删除！')
        return
    put = int(input('请输入您要删除的学生编号：'))
    while put not in range(0, len(stu_list)):
        put = int(input('编号不存在,请重新输入：'))

    del stu_list[put]
    save_stu_info()
    print('============================')
    print('删除成功！！！')

def delete_by_name():
    while True:
        name2 = input('请输入您要删除学生的姓名：')
        find = False
        for put in range(0, len(stu_list)):
            find_list = stu_list[put]
            name = find_list[0]
            if name == name2:
                find = True
                del stu_list[put]
                save_stu_info()
                print('============================')
                print('删除成功！！')
        if find == False:
            print('姓名不存在,请重新输入姓名：')
        else:
            break

def delete_all():
    stu_list.clear()
    save_stu_info()
    print('============================')
    print('已删除所有学生信息！！！')

def show_menu():
    print('============================')
    print('0.退出程序')
    print('1.添加学生')
    print('2.修改学生')
    print('3.查询学生')
    print('4.删除学生')
    print('5.帮助信息')
    print('============================')

def show_menu_0f_find():
    print('============================')
    print('1.按编号查询学生')
    print('2.按姓名查询学生')
    print('3.查询所有学生')
    print('============================')

def show_menu_of_delete():
    print('============================')
    print('1.按编号删除学生')
    print('2.按姓名删除学生')
    print('3.删除所有学生')
    print('============================')

def show_login():
    print('============================')
    print('1.注册')
    print('2.登录')
    print('============================')

def help():
    print('------学生信息管理系统------')
    print('    本系统主要是在学了python基础之后做的一个小项目,其中最重要的就是用文件进行信息的存储,' + '\n' +
          '因为学的知识有限，只是实现了一小部分功能,到目前为止还是有一点点小的bug存在,不过大部分' + '\n' +
          '的功能还是能实现的,等以后学习的只是更深之后再回头把这个项目完善.' + '\n' +
          '    本系统使用起来也是非常简便的，您只需要根据里面的提示信息正确输入,那么所有的功能都能' + '\n' +
          '正常实现.')

def main():
    read_stu_info()
    while True:
        show_menu()
        num = int(input('请选择您要进行的操作：'))
        while num not in range(0, 6):
            num = int(input('没有该选项,请重新输入：'))
        if num == 1:
            add_stu_info()
        elif num == 2:
            modify_stu_info()
        elif num == 3:
            show_menu_0f_find()
            num1 = int(input('请选择您要查询的方式：'))
            while num1 not in range(1, 4):
                num1 = int(input('没有该选项,请重新输入：'))
            if num1 == 1:
                find_by_id()
            elif num1 == 2:
                find_by_name()
            elif num1 == 3:
                find_all()
        elif num == 4:
            show_menu_of_delete()
            num2 = int(input('请选择您要删除的方式：'))
            while num2 not in range(1, 4):
                num2 = int(input('没有该选项,请重新输入：'))
            if num2 == 1:
                delete_by_id()
            elif num2 == 2:
                delete_by_name()
            elif num2 == 3:
                sure = input('确定删除所有信息？y(确定)/n(取消)：')
                if sure == 'y':
                    delete_all()
                elif sure == 'n':
                    print('删除操作已取消！')
                else:
                    print('输入有误')
        elif num == 5:
            help()
        else:
            print('谢谢使用,再见！')
            exit(0)

def first():
    read_user_info()
    while True:
        show_login()
        num = int(input('输入您要进行的操作编号：'))
        if num == 1:
            register()
        elif num == 2:
            login()
        else:
            num = input('您的输入有误,请按enter键重新输入')

first()
