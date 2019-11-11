def some_loop(x):
    z = 0
    for i in range(x):
        for j in range(100):
            z += i * j * x
        return z
