
import openpyxl
from datetime import datetime
import os

plan = []
plan_2 = []
timing = []

day_exel = {
    'Понедельник' : ['B3', 'E10'],
    'Вторник' : ['B15', 'E22'],
    'Среда' : ['B27', 'E34'],
    'Четверг' : ['B39', 'E46'],
    "Пятница" : ['B51','E58'],
    }

weekday_exel = {
    0 : 1,
    1 : 13,
    2 : 25,
    3 : 37,
    4 : 49,
    }


def next_day(name): 
    book = openpyxl.open(os.path.realpath('file_save/'+name.lower()+".xlsx"), read_only=True)

    classR = ''
    Result_stroke = ''

    next_day = datetime.weekday(datetime.now()) + 1
    sheet = book.active

    days = day_exel[sheet[weekday_exel[next_day]][0].value]
    next_day_main = sheet[days[0] : days[-1]]
    for lessons, group, teacher, classrom in next_day_main:
            if type(classrom.value) == float:
                classR = '%.0f' % classrom.value
            else:
                classR = classrom.value
            plan_2.append((lessons.value, group.value, teacher.value, classR))

    for stroke_lines in plan_2[:-1]:
       Result_stroke += ' '.join(map(str, stroke_lines)) + '\n'
    return Result_stroke

def main(name):
    
    book = openpyxl.open(os.path.realpath('file_save/'+name.lower()+".xlsx"), read_only=True)

    Result_stroke = ''
    classR = ''
    day = datetime.weekday(datetime.now())
    sheet = book.active

    days = day_exel[sheet[weekday_exel[day]][0].value]
    to_day_main = sheet[days[0] : days[-1]]
    for lessons, group, teacher, classrom in to_day_main:
        if type(classrom.value) == float:
            classR = '%.0f' % classrom.value
        else:
            classR = classrom.value
        plan.append((lessons.value, group.value, teacher.value, classR))
    for stroke_lines in plan[:-1]:
        Result_stroke += ' '.join(map(str, stroke_lines))  + '\n'
    return Result_stroke            

if __name__ == "__main__":
    main()