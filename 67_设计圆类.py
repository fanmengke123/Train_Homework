class Circle():

    def __init__(self, center_of_circle, radius, color):
        self.center_of_circle = center_of_circle
        self.radius = radius
        self.color = color

    def circle_perimeter(self):

        perimeter = 2 * 3.14 * self.radius
        print('圆心在{}的半径{}cm颜色为{}的圆的周长为{}'.format(
            self.center_of_circle,self.radius,self.color,perimeter
        ))

    def circle_area(self):

        area = 3.14 * self.radius ** 2
        print('圆心在{}的半径{}cm颜色为{}的圆的面积为{}'.format(
            self.center_of_circle,self.radius,self.color,area
        ))

circle = Circle('(0,0)',1,'Red')
circle.circle_perimeter()
circle.circle_area()
