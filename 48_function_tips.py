import datetime

time = datetime.datetime.now().weekday()

def function_tips(n):
    mot =['今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择',
          '今天星期二：\n含泪播种的人一定能笑着收获',
          '今天星期三：\n做对的事情比把事情做对更重要',
          '今天星期四：\n不要等到明天，明天太遥远，今天就行动',
          '今天星期五：\n命运给予我们的不是失望之酒，而是机会之杯',
          '今天星期六：\n求知若饥，虚心若愚',
          '今天星期日：\n成功属于那些从不说“不可能”的人']
    return mot[n]

fmk_result = function_tips(time)
print(fmk_result)
