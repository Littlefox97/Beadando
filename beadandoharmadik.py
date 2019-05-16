import numpy as np
import random

def sziget(x):
    base = np.full((100, 100), "~")
    vel1 = []
    vel2 = []
    a = random.randrange(2, 97, 4)
    c = random.randrange(2, 97, 4)
    for i in range(x):
        while a in vel1:
            a = random.randrange(2, 97, 4)
        vel1.append(a)
        while c in vel2:
            c = random.randrange(2, 97, 4)
        vel2.append(c)
        base[a][c] = "O"
        base[a - 1][c - 1] = "O"
        base[a][c - 1] = "O"
        base[a - 1][c] = "O"
        base[a + 1][c] = "O"
        base[a + 1][c - 1] = "O"
        base[a + 1][c + 1] = "O"
        base[a][c + 1] = "O"
        base[a - 1][c + 1] = "O"
    print(base)

while True:
    try:
        x=int(input("Adjon meg egy szamot: "))
        sziget(x)
        m = (100 - 3) // 4
        maxsziget = m * m
        print("Maximum sziget szam: ", maxsziget)
        break
    except ValueError:
        print("Nem megfelelő input.")
