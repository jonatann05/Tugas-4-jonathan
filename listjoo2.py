myList = [1,2,3,4,5,6,7]  ## bikin list awal
print(myList)  ## tampilkan list awal

myList.insert(4,15)  ## sisipkan 15 di index ke-4
print(myList)  ## tampilkan setelah insert

myList.append(55)  ## tambahin 55 di akhir list
print(myList)  ## tampilkan setelah append

newList = [11,12,13,14]  ## list baru
myList.extend(newList)  ## gabungkan newList ke myList
print(myList)  ## tampilkan hasil akhir


# =========================
# OUTPUT
# =========================

# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 15, 5, 6, 7]
# [1, 2, 3, 4, 15, 5, 6, 7, 55]
# [1, 2, 3, 4, 15, 5, 6, 7, 55, 11, 12, 13, 14]