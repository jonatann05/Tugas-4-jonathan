from array import array  ## import modul array

my_array = array('i', [1, 2, 3, 4, 5, 6, 10, 11, 12, 20, 21, 22])  ## bikin array awal

print("\nStep 8")  ## judul step 8
my_array.pop()  ## hapus elemen terakhir di array
print(my_array)  ## tampilkan hasil setelah pop


# =========================
# OUTPUT
# =========================

# Step 8
# array('i', [1, 2, 3, 4, 5, 6, 10, 11, 12, 20, 21])