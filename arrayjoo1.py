import numpy as np  ## import numpy buat kerja dengan array 2D

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])  ## bikin array awal 4x4

print("Array Awal:")  ## kasih judul output
print(twoDArray)      ## nampilin array awal

insertArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)  ## sisipkan baris di index 1
print("\nSetelah Insert:")  ## judul setelah insert
print(insertArray)          ## tampilkan hasil setelah insert

appendArray = np.append(insertArray, [[1,2,3,4]], axis=0)  ## tambah baris di akhir
print("\nSetelah Append:")  ## judul setelah append
print(appendArray)          ## tampilkan hasil setelah append

print("\nJumlah baris:", len(appendArray))   ## hitung total baris
print("Jumlah kolom:", len(appendArray[0]))  ## hitung total kolom


# =========================
# OUTPUT YANG DIHARAPKAN
# =========================

# Array Awal:
# [[11 15 10  6]
#  [10 14 11  5]
#  [12 17 12  8]
#  [15 18 14  9]]
#
# Setelah Insert:
# [[11 15 10  6]
#  [ 1  2  3  4]
#  [10 14 11  5]
#  [12 17 12  8]
#  [15 18 14  9]]
#
# Setelah Append:
# [[11 15 10  6]
#  [ 1  2  3  4]
#  [10 14 11  5]
#  [12 17 12  8]
#  [15 18 14  9]
#  [ 1  2  3  4]]
#
# Jumlah baris: 6
# Jumlah kolom: 4