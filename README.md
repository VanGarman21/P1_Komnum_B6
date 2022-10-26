# P1_Komnum_B6
 
Praktikum 1 Komputasi Numerik
KomNum B
 
Kelompok  6
Nama Anggota :
1.  M. Armand Giovani (502511054)
2.  Fathin Muhashibi Putra (5025211229)
3.  Dafarel Fatih Wirayudha (5025211120)

## Implementasi Metode Bolzano pada program Python

Kami mencari sebuah persamaan yang akan diselesaikan dengan metode bolzano yang nantinya akan kami selesaikan dengan program Python.
Untuk persamaannya sendiri, kami mengambil dari ppt pertemuan ke 2

   ![Screenshot 2022-10-26 185234](https://user-images.githubusercontent.com/100523471/198019298-8f16483e-9bd6-444d-9559-7b1f27486db2.png)


Kemudian kami, definisikan fungsi tersebut kedalam program dan juga mendeklarasikan variabel untuk batas-batas dalam metode bolzano yaitu `x1`, `x2` dan `x3` sebagai batas baru. Selanjutnya kami mendeklarasikan `f1`, `f2` dan `f3` sebagai variabel yang menampilkan hasil fungsi dari  `x1`, `x2` dan `x3`. Kemudian, kami mendeklarasikan counter untuk looping iterasi metode bolzano. 

```
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
```

Selanjutnya kami melakukan perhitungan dengan menggunakan looping sesuai dengan prinsip iterasi metode bolzano yang didalanmnya melakukan perhitungan untuk mendapatkan nilai dari `x3`, `f1`, `f2` dan `f3`. Kemudian hasil perhitungan yang didapatkan akan ditampilkan dalam kolom-kolom tabel yang telah ditentukan.

```
for i in range(n):
        x3 = (x1 + x2)/2
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
```

Setelah mendapatkan hasil perhitungan tersebut, program kami akan melakukan pengecekan nilai `f3` untuk menentukan nilai dari `x1` atau `x2`.
```
if f1*f3 < 0:
            x2 = x3

        elif f1*f3 > 0:
            x1 = x3
            
        else:
            break
```

