arr = [1, 2, 3, 4, 5, 6]                # buat list

for i in range(1, 6):                  # looping dari index 1 sampai 5
    arr[i - 1] = arr[i]                # geser elemen ke kiri (copy dari kanan)

# proses perubahan:
# i=1 → arr[0]=2 → [2,2,3,4,5,6]
# i=2 → arr[1]=3 → [2,3,3,4,5,6]
# i=3 → arr[2]=4 → [2,3,4,4,5,6]
# i=4 → arr[3]=5 → [2,3,4,5,5,6]
# i=5 → arr[4]=6 → [2,3,4,5,6,6]

for i in range(0, 6):
    print(arr[i], end=" ")             # cetak semua elemen


# A. 1 2 3 4 5 6
# B. 2 3 4 5 6 1
# C. 1 1 2 3 4 5
# D. 2 3 4 5 6 6 (this is the right answer)
#    karena setiap elemen diganti dengan elemen di kanannya