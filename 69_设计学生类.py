class Student():

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score)



xiaoming = Student('小明','18',[88,96,90])
print('学生姓名为：{}'.format(xiaoming.get_name()))
print('学生年龄为：{}'.format(xiaoming.get_age()))
print('三门课中最高成绩为：{}'.format(xiaoming.get_course()))
