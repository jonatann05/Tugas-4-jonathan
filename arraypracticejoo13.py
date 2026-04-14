from array import array  ## import modul array

my_array = array('i', [1, 2, 3])  ## bikin array awal

print("\nStep 13")  ## judul step 13
data = my_array.tobytes()  ## ubah array jadi bytes
print(data)  ## tampilkan hasil bytes

ints = array('i')  ## bikin array kosong baru
ints.frombytes(data)  ## isi array dari data bytes
print(ints)  ## tampilkan hasil konversi kembali


# =========================
# OUTPUT
# =========================

# Step 13
# b'...'
# array('i', [1, 2, 3])