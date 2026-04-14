myList = [10,20,30,40,50,60,70,80,90]  ## bikin list angka

def searchinList(list, value):
    for i in list:  ## looping setiap elemen di list
        if i == value:  ## kalau ketemu nilai yang dicari
            return list.index(value)  ## balikin index-nya
    return 'The value does not exist in the list'  ## kalau tidak ketemu

print(myList)  ## tampilkan list awal
print(searchinList(myList, 60))  ## cari nilai 60


# =========================
# OUTPUT
# =========================

# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# 5