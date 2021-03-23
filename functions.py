def addobject(value, board):
    value = list(value)
    print(value)
    if value[-1] == "Point":
        x = float(value[0])
        y = float(value[1])
        name = value[2]
        if int(x) == x:
            x = int(x)
        if int(y) == y:
            y = int(y)
        board.addpoint(x, y, name)
    elif value[-1] == "Circle":
        x = float(value[0])
        y = float(value[1])
        r = float(value[2])
        name = value[3]
        if int(x) == x:
            x = int(x)
        if int(y) == y:
            y = int(y)
        if int(r) == r:
            r = int(r)
        board.addcircle(x, y, r, name)
    elif value[-1] == "Line":
        a = float(value[0])
        b = float(value[1])
        name = value[2]
        if int(a) == a:
            a = int(a)
        if int(b) == b:
            b = int(b)
        board.addline(a, b, name)
