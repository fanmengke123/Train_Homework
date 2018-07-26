class Animal():
    def __init__(self, color):
        self.color = color

    def call(self):
        print('颜色为{}的鱼在叫'.format(self.color))

class Fish(Animal):

    def __init__(self,tail,color):
        super().__init__(color)
        self.tail = tail

    def call(self):

        print('{}'.format(self.tail))
        super().call()
        # print('{}的颜色为{}的鱼在叫'.format(self.tail,self.color))

fish = Fish('长尾巴','灰色')
fish.call()
