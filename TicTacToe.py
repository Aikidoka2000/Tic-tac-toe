xomap = [["y3 ", "( )", "( )", "( )"], [" 2 ", "( )", "( )", "( )"], [" 1 ", "( )", "( )", "( )"], ["   ", " 1 ", " 2 ", " 3x"]]

first = input("Who is first? X or O: ")
if first == "x":
    first = "(X)"
    second = "(O)"
elif first == "o":
    first = "(O)"
    second = "(X)"

def mapxo():
    for i in range(4):
        for j in range(4):
            print(xomap[i][j], end="")
        print()

def xodo(x, y):
    if x == 1 and y == 1:
        xomap[2][1] = first
        return mapxo()
    elif x == 1 and y == 2:
        xomap[1][1] = first
        return mapxo()
    elif x == 1 and y == 3:
        xomap[0][1] = first
        return mapxo()
    elif x == 2 and y == 1:
        xomap[2][2] = first
        return mapxo()
    elif x == 2 and y == 2:
        xomap[1][2] = first
        return mapxo()
    elif x == 2 and y == 3:
        xomap[0][2] = first
        return mapxo()
    elif x == 3 and y == 1:
        xomap[2][3] = first
        return mapxo()
    elif x == 3 and y == 2:
        xomap[1][3] = first
        return mapxo()
    elif x == 3 and y == 3:
        xomap[0][3] = first
        return mapxo()


mapxo()
for i in range(9):
    xodo(int(input("x:")), int(input("y:")))
    print()