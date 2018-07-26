class Course():

    def __init__(self,course_id, course_name,course_teacher):
        self.course_id = course_id
        self.course_name = course_name
        self.course_teacher = course_teacher
        self.__location = '大兴二职'

    def show_course_info(self):
        print('课程编号：{}\n课程名称：{}\n任课老师:{}\n上课地点:{}'.format(
            self.course_id,self.course_name,self.course_teacher,self.__location
        ))

AI = Course('0001','人工智能','翁闻宇')
AI.show_course_info()
