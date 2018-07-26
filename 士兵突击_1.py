from MyWarehouse import 士兵突击_2_Gun
class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def open_fire(self):
        if self.gun is None:
            print('{}还没有枪,无法射击'.format(self.name))
            return

        print('士兵{}发起冲锋...冲啊！！！'.format(self.name))

        士兵突击_2_Gun.ak47.fill_bullet(10)

        士兵突击_2_Gun.ak47.shoot()

p1 = Soldier('许三多', 士兵突击_2_Gun.ak47)
p1.open_fire()


# class Gun:
#     def __init__(self, name, bullet_count):
#         self.name = name
#         self.bullet_count = bullet_count
#
#     def shoot(self):
#         if self.bullet_count < 0 :
#             print('{}枪没有子弹,射击失败'.format(self.name))
#             return
#
#         self.bullet_count -= 1
#         print('{}发射子弹{}'.format(self.name,self.bullet_count))
#
#     def fill_bullet(self, count):
#         self.bullet_count += count
#
# p1 = Soldier('许三多')
# p1.open_fire()
# ak47 = Gun('AK47',10)
# ak47.fill_bullet(10)
# ak47.shoot()
