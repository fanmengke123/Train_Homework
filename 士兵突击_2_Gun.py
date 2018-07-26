class Gun:
    def __init__(self, name, bullet_count):
        self.name = name
        self.bullet_count = bullet_count

    def shoot(self):
        if self.bullet_count < 0 :
            print('{}枪没有子弹,射击失败'.format(self.name))
            return

        self.bullet_count -= 1
        print('{}发射子弹1颗子弹,剩余{}颗子弹'.format(self.name,self.bullet_count))

    def fill_bullet(self, count):
        self.bullet_count += count
        print('枪{}填充了{}颗子弹'.format(self.name, self.bullet_count))
ak47 = Gun('AK47',10)