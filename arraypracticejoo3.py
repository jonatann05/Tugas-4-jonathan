from array import array  ## import modul array

# kita buat array dulu
my_array = array('i', [1,2,3,4,5])  ## bikin array integer

print("\nStep 3")  ## judul step 3
my_array.append(6)  ## nambah angka 6 ke dalam array
print(my_array)     ## tampilkan array setelah ditambah


# =========================
# OUTPUT
# =========================

# Step 3
# array('i', [1, 2, 3, 4, 5, 6])