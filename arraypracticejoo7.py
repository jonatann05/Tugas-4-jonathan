from array import array  ## import modul array

my_array = array('i',[1,2,3,11,4,5])  ## bikin array awal

print("\nStep 7")  ## judul step 7
my_array.remove(11)  ## hapus nilai 11 dari array
print(my_array)      ## tampilkan hasil setelah dihapus


# =========================
# OUTPUT
# =========================

# Step 7
# array('i', [1, 2, 3, 4, 5])