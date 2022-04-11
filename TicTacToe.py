import re


xomap = [["y3 ", "( )", "( )", "( )"], [" 2 ", "( )", "( )", "( )"], [" 1 ", "( )", "( )", "( )"], ["   ", " 1 ", " 2 ", " 3x"]]
# создали матрицу

first = input("Who is first? x or o: ")   
while True:
    if first == "x":
        first = "(X)"
        second = "(O)"
        break
    else:
        first = input("Who is first? x or o: ")
while True:
    if first == "o":
        first = "(O)"
        second = "(X)"
        break
    else:
        first = input("Who is first? x or o: ")
# определяем выбор первого игрока

def mapxo(): 
    for i in range(4):
        for j in range(4):
            print(xomap[i][j], end="")
        print()
# рисуем поле

def xodo(x, y, lane):
    if x == 1 and y == 1:
        xomap[2][1] = lane
        return mapxo()
    elif x == 1 and y == 2:
        xomap[1][1] = lane
        return mapxo()
    elif x == 1 and y == 3:
        xomap[0][1] = lane
        return mapxo()
    elif x == 2 and y == 1:
        xomap[2][2] = lane
        return mapxo()
    elif x == 2 and y == 2:
        xomap[1][2] = lane
        return mapxo()
    elif x == 2 and y == 3:
        xomap[0][2] = lane
        return mapxo()
    elif x == 3 and y == 1:
        xomap[2][3] = lane
        return mapxo()
    elif x == 3 and y == 2:
        xomap[1][3] = lane
        return mapxo()
    elif x == 3 and y == 3:
        xomap[0][3] = lane
        return mapxo()
# заполняем поле

def inp(x, y):
    while True:
        x = input("x:")
        if x == "1" or x == "2" or x == "3":
            x = int(x)
            break
        else:
            print("Select a coordinate х: 1, 2 or 3!")
            mapxo()
    while True:
        y = input("y:")
        if y == "1" or y == "2" or y == "3":
            y = int(y)
            break
        else:
            print("Select a coordinate y: 1, 2 or 3!")
            mapxo()
    return x, y
# проверка правильности ввода координат

mapxo()

x, y = inp(None, None)
print(x, y)

xodo(x, y, first)
print()
xodo(x, y, second)
print()