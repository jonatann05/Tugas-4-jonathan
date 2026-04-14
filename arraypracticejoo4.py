from array import array  ## import modul array

my_array = array('i',[1,2,3,4,5])  ## bikin array integer

for i in my_array:  ## looping tiap elemen
    print(i)        ## tampilkan satu per satu

print("\nStep 4")  ## judul step 4
my_array.insert(3, 11)  ## sisipkan angka 11 di index ke-3
print(my_array)         ## tampilkan array setelah insert


# =========================
# OUTPUT
# =========================

# 1
# 2
# 3
# 4
# 5
#
# Step 4
# array('i', [1, 2, 3, 11, 4, 5])