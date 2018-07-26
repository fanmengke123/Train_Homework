class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '{}占地{}平米'.format(self.name, self.area)


bed = HouseItem('席梦思',4)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',1.5)
print(bed)
print(chest)
print(table)


class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.surplus_area = area
        self.item_list = []

    def __str__(self):
        return '户型：{}, 总面积{}, 剩余面积{}, 家具名称列表{}'.format(
            self.type, self.area, self.surplus_area, self.item_list)

    def add_items(self, item):
        print('要添加{}'.format(item))

        if item.area > self.surplus_area:
            print('{}的面积太大,不能添加到房子中'.format(item.name))
            return

        self.item_list.append(item.name)

        self.surplus_area -= item.area


house = House('三室一厅',120)
house.add_items(bed)
house.add_items(chest)
house.add_items(table)
print(house)
