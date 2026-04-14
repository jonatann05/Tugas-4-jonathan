import numpy as np  ## import numpy buat kerja sama array 2D

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])  ## bikin array awal

appendArray = np.append(twoDArray, [[1,2,3,4]], axis=0)  ## nambah baris baru di akhir array

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):  ## cek apakah index valid atau keluar batas
        print('Incorrect Index')  ## kalau salah index, kasih pesan error
    else:
        print(array[rowIndex][colIndex])  ## kalau benar, tampilkan nilai elemen

print("\nAkses Elemen:")  ## judul output
accessElements(appendArray, 3, 1)  ## ambil elemen baris 3 kolom 1


# =========================
# OUTPUT YANG DIHARAPKAN
# =========================

# Akses Elemen:
# 18