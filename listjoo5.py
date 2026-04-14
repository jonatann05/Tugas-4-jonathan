numlist = list()  ## bikin list kosong buat nampung angka

while True:  ## looping terus sampai user selesai
    inp = input('Enter a number: ')  ## input dari user
    if inp == 'done': break  ## kalau ketik done, berhenti

    value = float(inp)  ## ubah input jadi angka
    numlist.append(value)  ## masukin ke list

average = sum(numlist) / len(numlist)  ## hitung rata-rata dari semua data di list
print('Average:', average)  ## tampilkan hasil


# =========================
# CONTOH INPUT
# =========================
# 10
# 20
# 30
# done

# =========================
# OUTPUT
# =========================
# Average: 20.0