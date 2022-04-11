xomap = [["y3 ", "( )", "( )", "( )"], [" 2 ", "( )", "( )", "( )"], [" 1 ", "( )", "( )", "( )"], ["   ", " 1 ", " 2 ", " 3x"]]
# создали матрицу

first = input("Who is first? X or O: ")   
if first == "x":
    first = "(X)"
    second = "(O)"
elif first == "o":
    first = "(O)"
    second = "(X)"
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



mapxo()
for i in range(9):
    xodo(int(input("x:")), int(input("y:")), first)
    print()
    xodo(int(input("x:")), int(input("y:")), second)
    print()