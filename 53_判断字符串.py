def is_let_or_dit(s):
    flag1 = True #汉字
    flag2 = True #字母和数字
    flag3 = True #其他字符
    for i in s:
        if u'\u4e00' <= i and i <= u'\u9fff':
            flag1 = False
        elif i.isalnum():
            if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
                flag2 = True
            else:
                flag2 = False

        else:
            flag3 = False

    if(flag1 == flag2 == flag3):
        print('Yes')
    else:
        print('No')

string = input('请输入一串字符：')
p = is_let_or_dit(string)
