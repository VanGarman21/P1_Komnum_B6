# P1_Komnum_B6
 
Praktikum 1 Komputasi Numerik
KomNum B
 
Kelompok  6
Nama Anggota :
1.  M. Armand Giovani (502511054)
2.  Fathin Muhashibi Putra (5025211229)
3.  Dafarel Fatih Wirayudha (5025211120)

## Implementasi Metode Bolzano pada program Python

Kami mencari sebuah persamaan yang akan diselesaikan dengan metode bolzano. Bahasa pemrograman yang kami gunakan adalah bahasa Python.

Untuk persamaannya sendiri, kami mengambil contoh soal dari ppt pertemuan ke 2

   ![Screenshot 2022-10-26 185234](https://user-images.githubusercontent.com/100523471/198019298-8f16483e-9bd6-444d-9559-7b1f27486db2.png)

Kemudian, kami definisikan fungsi tersebut kedalam program dan juga mendeklarasikan variabel sebagai interval batas-batas persamaan yaitu `x1`, `x2`, dan `x3` (sebagai batas baru). Selanjutnya kami mendeklarasikan `f1`, `f2` dan `f3` sebagai variabel yang menampilkan hasil fungsi dari  `x1`, `x2` dan `x3`. Kami juga mendeklarasikan counter (n) untuk looping iterasi metode bolzano. Selanjutnya kami mendeklarasikan variabel 'start' dan 'end' sebagai interval batas-batas persamaan dalam grafik.

```
def f(x): # mendefinisikan fungsi
    return x**3 + x**2 - 3*x - 3 # mengembalikan nilai fungsi f(x) = x^3 + x^2 - 3x - 3 

x1 = float(input("Masukkan Interval awal : ")) # Perintah untuk memasukkan nilai interval awal
x2 = float(input("Masukkan Interval akhir: ")) # Perintah untuk memasukkan nilai interval akhir
n = int(input("Masukkan Banyak Iterasi : ")) # Perintah untuk memasukkan banyaknya iterasi

start = x1 # nilai interval awal untuk pembuatan grafik 
end = x2 # nilai interval akhir untuk pembuatan grafik

if f(x1)*f(x2) < 0: # jika nilai 
    tabel_tabulasi = [] # mendefinisikan array dengan nama "tabel_tabulasi"
    for i in range(n): # melakukan perulangan sejumlah banyak iterasi (n)
        
        x3 = (x1 + x2)/2 # menghitung nilai x3
        f1 = f(x1) # menghitung nilai f1, dengan memasukkan nilai x1 pada fungsi persamaan f(x)
        f2 = f(x2) # menghitung nilai f2, dengan memasukkan nilai x2 pada fungsi persamaan f(x)
        f3 = f(x3) # menghitung nilai f3, dengan memasukkan nilai x1 pada fungsi persamaan f(x)

```

Selanjutnya kami melakukan perhitungan dengan menggunakan looping sesuai dengan prinsip iterasi metode bolzano yang didalanmnya melakukan perhitungan untuk mendapatkan nilai dari `x3`, `f1`, `f2` dan `f3`. Kemudian nantinya hasil perhitungan yang didapatkan akan ditampilkan dalam kolom-kolom tabel yang telah ditentukan.

```
if f(x1)*f(x2) < 0: # jika nilai 
    tabel_tabulasi = [] # mendefinisikan array dengan nama "tabel_tabulasi"
    for i in range(n): # melakukan perulangan sejumlah banyak iterasi (n)
        
        x3 = (x1 + x2)/2 # menghitung nilai x3
        f1 = f(x1) # menghitung nilai f1, dengan memasukkan nilai x1 pada fungsi persamaan f(x)
        f2 = f(x2) # menghitung nilai f2, dengan memasukkan nilai x2 pada fungsi persamaan f(x)
        f3 = f(x3) # menghitung nilai f3, dengan memasukkan nilai x1 pada fungsi persamaan f(x)

        tabel_tabulasi.append([x1, x2, x3, f1, f2, f3]) # memasukkan nilai x1, x2, x3, f1, f2,dan f3 kedalam array "tabel_tabulasi"
```

Setelah mendapatkan hasil perhitungan tersebut, program kami akan melakukan pengecekan untuk menentukan nilai `x1` atau `x2` berdasarkan nilai hasil operasi `f1*f3`.
```
if f1*f3 > 0: # jika nilai f1*f3 > 0, maka
            x1 = x3 # nilai x1 = x3
            
        elif f1*f3 < 0: # jika nilai f1*f3 < 0, maka
            x2 = x3 # nilai x2 = x3
            
        else: 
            break # perulangan berhenti
```

Selanjutnya, akan dihasilkan grafik yang berisi data-data hasil perhitungan untuk menentukan akar-akar persamaan dengan Metode Bolzano.
```
   print("-------------------------------------------------------------")
    tabel = praktikum.DataFrame(tabel_tabulasi, columns=['x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']) # menambahkan nama kolom pada tabel
    tabel.index = semangat.arange(1, len(tabel)+1) # memunculkan indeks iterasi ke-.. pada samping tabel
    print(tabel) # mencetak tabel dengan isinya
    print("-------------------------------------------------------------")
    
    print(f"\n Akar dari persamaan tersebut adalah {x3}\n") # dioutputkan nilai x3, sebagai akar dari persamaan tersebut 

    else:
    print("Error Input") # mencetak "Error Input" ketika input yang dimasukkan tidak sesuai
```
Tabel yang dihasilkan, yaitu sebagai berikut :


Terakhir, akan dihasilkan grafik persamaan Metode Bolzano.
```
x = semangat.arange(start, end+0.01, 0.01) # x merupakan variabel yang bakal menyimpan array nilai x yang akan membentuk grafik
y = f(x) # mendeklarasikan variabel y = f(x)
komnum.grid() # menambahkan grid kedalam plot grafik
komnum.xlabel("X") # menambahkan xlabel "X" kedalam plot grafik
komnum.ylabel("f(X)") # menambahkan ylabel "Y" kedalam plot grafik
komnum.plot(x, y) # plot grafik x dan y
komnum.show() # menampilkan plot grafik 
```
Grafik yang dihasilkan, yaitu sebagai berikut :
   ![Screenshot 2022-10-26 204837](https://user-images.githubusercontent.com/100523471/198044873-bbed0f06-4f02-4022-a398-706db8f61313.png)
