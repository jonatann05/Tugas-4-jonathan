from array import array  ## import modul array

# array awal (harus ada dulu)
my_array = array('i', [1,2,3,4,5])  ## bikin array awal

print("\nStep 6")  ## judul step 6
tempList = [20,21,22]  ## list sementara yang mau ditambah

my_array.fromlist(tempList)  ## masukin isi list ke array
print(my_array)  ## tampilkan hasil akhir


# =========================
# OUTPUT
# =========================

# Step 6
# array('i', [1, 2, 3, 4, 5, 20, 21, 22])