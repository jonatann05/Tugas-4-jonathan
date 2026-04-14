a = [1,2,3,4,5,6,7,8,9]           # Membuat list berisi 9 angka

a[::2] = 10,20,30,40,50,60         # a[::2] → pilih indeks 0,2,4,6,8 (total 5 elemen)
                                  # lalu mau diganti 6 nilai → jadi error karena jumlah tidak sama

print(a)                           # Tidak akan dijalankan karena sudah error di baris sebelumnya


# A. ValueError: attempt to assign sequence of size 6 to extended slice of size 5  (this is the right answer)
#    karena slice target hanya 5, sedangkan data yang dimasukkan ada 6
# B. [10, 2, 20, 4, 30, 6, 40, 8, 50, 60]
# C. [1, 2, 10, 20, 30, 40, 50, 60]
# D. [1, 10, 3, 20, 5, 30, 7, 40, 9, 50, 60]