from array import array  ## import modul array

my_array = array('i', [1, 2, 3, 4, 5])  ## bikin array awal

print("\nStep 11")  ## judul step 11
print(my_array.buffer_info())  ## tampilkan info buffer (alamat memori & panjang array)


# =========================
# OUTPUT
# =========================

# Step 11
# (alamat_memori, 5)