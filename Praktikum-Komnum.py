# PROBLEM :
# Dapatkan akar dari persamaan  f(x) = x^3 + x^2 – 3x – 3 = 0 yang terletak di antara x = 1 dan x = 2.

# ANALISIS :
# Membuat sebuah program yang dapat menghitung akar dari persamaan f(x) = x^3 + x^2 – 3x – 3 = 0,
# kemudian setelah ditemukan perubahan  tanda kita bisa mendapatkan interval baru.

import numpy as np # library numpy yang berfungsi untuk menggenerate angka
import pandas as pd # library pandas untuk membantu dalam pembuatan tabel
import matplotlib.pyplot as plt # library matplotlib untuk membantu dalam pembuatan grafik perkiraan

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

        tabel_tabulasi.append([x1, x2, x3, f1, f2, f3]) # memasukkan nilai x1, x2, x3, f1, f2,dan f3 kedalam array "tabel_tabulasi"
      
      # Dilakukan pengecekan untuk menentukan nilai x1 atau x2 berdasarkan nilai hasil perkalian f1*f3.  

        if f1*f3 > 0: # jika nilai f1*f3 > 0, maka
            x1 = x3 # nilai x1 = x3
            
        elif f1*f3 < 0: # jika nilai f1*f3 < 0, maka
            x2 = x3 # nilai x2 = x3
            
        else: 
            break # perulangan berhenti
        
    print("-------------------------------------------------------------")
    tabel = pd.DataFrame(tabel_tabulasi, columns=['x1', 'x2', 'x3', 'f1', 'f2', 'f3']) # menambahkan nama kolom pada tabel
    tabel.index = np.arange(1, len(tabel)+1) # memunculkan indeks iterasi ke-.. pada samping tabel
    print(tabel) # mencetak tabel dengan isinya
    print("-------------------------------------------------------------")
    
    print(f"\n Akar dari persamaan tersebut adalah {x3}\n") # dioutputkan nilai x3, sebagai akar dari persamaan tersebut 

else:
    print("Error Input") # mencetak "Error Input" ketika input yang dimasukkan tidak sesuai

x = np.arange(start, end+0.01, 0.01) # x merupakan variabel yang bakal menyimpan array nilai x yang akan membentuk grafik
y = f(x) # mendeklarasikan variabel y = f(x)
plt.grid() # menambahkan grid kedalam plot grafik
plt.xlabel("X") # menambahkan xlabel "X" kedalam plot grafik
plt.ylabel("Y") # menambahkan ylabel "Y" kedalam plot grafik
plt.plot(x, y) # plot grafik x dan y
plt.show() # menampilkan plot grafik 
