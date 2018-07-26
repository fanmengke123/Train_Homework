List = [(1.4,'《Give up,hold on to me》'),(1.343,'《The private dishes of the husbands》'),
        (0.92,'《My father-in-lawwill do martiaiarts》'),(0.862,'《North Canton still believe in love》'),
        (0.553,'《Impossible task》'),(0.411,'《Sparrow》'),(0.164,'《East of dream Avenue》'),
        (0.259,'《The prodigal son of the new frontier town》'),(0.394,'《Distant distance》'),
        (0.562,'《Music legend》')]

List.sort(reverse=True)
print('电视剧的收视率排行榜：')
for i in List:
    print(i[1] + '收视率： ' + str(i[0]) + '%')
