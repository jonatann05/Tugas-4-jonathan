from array import array  ## import modul array

print("Step 1")  ## judul step 1
my_array = array('i',[1,2,3,4,5])  ## bikin array awal

for i in my_array:  ## looping isi array
    print(i)        ## print tiap elemen

# keluar dari loop dulu (biar tidak ikut indent)
print("\nStep 5")  ## judul step 5
my_array1 = array('i', [10,11,12])  ## array tambahan
my_array.extend(my_array1)          ## gabungin array1 ke array utama
print(my_array)                     ## tampilkan hasil akhir


# =========================
# OUTPUT
# =========================

# Step 1
# 1
# 2
# 3
# 4
# 5
#
# Step 5
# array('i', [1, 2, 3, 4, 5, 10, 11, 12])