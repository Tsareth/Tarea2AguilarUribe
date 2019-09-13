def result(A, B):
    if(isinstance(A, int) is False):
        return -1
    elif(isinstance(B, int) is False):
        return -2
    elif A < B:
        return -3
    else:
        x = A + B
        y = A - B
        z = A * B
        return "Suma:", x, "Resta:", y, "Multiplicacion:", z
