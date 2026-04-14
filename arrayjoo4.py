import numpy as np  ## import numpy buat array 2D

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])  ## bikin array awal

def searchTDArray(array, value):
    for i in range(len(array)):  ## looping baris
        for j in range(len(array[0])):  ## looping kolom
            if array[i][j] == value:  ## kalau ketemu nilai yang dicari
                return 'Value ditemukan di index ' + str(i) + ", " + str(j)  ## balikin posisi
    return 'Value tidak ditemukan'  ## kalau nggak ketemu

print("\nSearch:")  ## judul output search
print(searchTDArray(twoDArray, 11))  ## cari nilai 11

newTDArray = np.delete(twoDArray, 1, axis=0)  ## hapus baris index 1
print("\nSetelah Delete:")  ## judul setelah delete
print(newTDArray)  ## tampilkan array setelah dihapus

print("\nArray Asli:")  ## judul array asli
print(twoDArray)  ## tampilkan array sebelum diubah


# =========================
# OUTPUT YANG DIHARAPKAN
# =========================

# Search:
# Value ditemukan di index 0, 0
#
# Setelah Delete:
# [[11 15 10  6]
#  [12 17 12  8]
#  [15 18 14  9]]
#
# Array Asli:
# [[11 15 10  6]
#  [10 14 11  5]
#  [12 17 12  8]
#  [15 18 14  9]]