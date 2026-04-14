import numpy as np  ## import numpy buat bikin array 2D

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])  ## bikin array 4x4

def traverseTDArray(array):
    print("\nTraversal Array:")  ## judul output
    for i in range(len(array)):  ## looping baris
        for j in range(len(array[0])):  ## looping kolom
            print(array[i][j])  ## tampilkan tiap elemen satu per satu

traverseTDArray(twoDArray)  ## panggil fungsi traversal


# =========================
# OUTPUT YANG DIHARAPKAN
# =========================

# Traversal Array:
# 11
# 15
# 10
# 6
# 10
# 14
# 11
# 5
# 12
# 17
# 12
# 8
# 15
# 18
# 14
# 9