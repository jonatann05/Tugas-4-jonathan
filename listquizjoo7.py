arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]                # membuat list 2D

for i in range(0, 4):                   # loop dari index 0 sampai 3
    print(arr[i].pop())                 # pop() ambil elemen terakhir dari setiap baris


# proses:
# baris 0 → ambil 4
# baris 1 → ambil 7
# baris 2 → ambil 11
# baris 3 → ambil 15


# A. 1 2 3 4
# B. 1 4 8 12
# C. 4 7 11 15 (this is the right answer)
#    karena pop() selalu mengambil elemen terakhir tiap sub-list
# D. 12,13,14,15