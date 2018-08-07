number = int(input('输入学生的成绩：'))

def judge_grade(n):

    if number >= 90:
        print('A优秀')
    elif number >= 80 and number < 90:
        print('B良好')
    elif number >= 70 and number < 80:
        print('C及格')
    elif number >= 0 and number < 70:
        print('D不及格')

if __name__ == '__main__':

    try:
        assert number >= 0 and number <= 100
        judge_grade(number)
    except:
        print('您输入的成绩不合法')
