import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return x**3 + x**2 - 3*x - 3 

x1 = float(input("Masukkan Interval awal : "))
x2 = float(input("Masukkan Interval akhir: "))
n = int(input("Banyak Iterasi : "))

start = x1
end = x2

if f(x1)*f(x2) < 0:
    ArrTable = []
    for i in range(n):
        x3 = (x1 + x2)/2
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)

        ArrTable.append([x1, x2, x3, f1, f2, f3])

        if f1*f3 < 0:
            x2 = x3

        elif f1*f3 > 0:
            x1 = x3
            
        else:
            break
    print("-------------------------------------------------------------")
    Table = pd.DataFrame(ArrTable, columns=['x1', 'x2', 'x3', 'f1', 'f2', 'f3'])
    Table.index = np.arange(1, len(Table)+1)
    print(Table)
    print("-------------------------------------------------------------")
    print(f"\n Akar dari persamaan tersebut adalah {x3}\n")
else:
    print("Error Input")

x = np.arange(start, end, 0.01)
y = f(x)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y)
plt.show()
