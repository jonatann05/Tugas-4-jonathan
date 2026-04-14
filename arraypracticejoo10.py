from array import array  ## import modul array

my_array = array('i', [1, 2, 3, 4, 5])  ## bikin array awal

print("\nStep 10")  ## judul step 10
my_array.reverse()  ## membalik urutan isi array
print(my_array)     ## tampilkan hasil setelah dibalik


# =========================
# OUTPUT
# =========================

# Step 10
# array('i', [5, 4, 3, 2, 1])