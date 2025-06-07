#ekspresi adalah kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna menghasilkan suatu nilai
x = 10
y = 2
result = x-y
print(result)

#penggabungan
angka = [2,4,5,7]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)
replikasi = huruf*2
print(replikasi)

#ekspresi uner (ekspresi biner sudah dimodul sebelumnya)
a = True
a = not a
print(a)
b = 6
b -= 1
print(b)
c = 6
c += 1
print(c)
d = 10
print(-d)

#ekspresi menurut tioe data yang dihasilkan
#ekspresi aritmatika
print(2+2)
#ekspresi relasional
print(3<10)
#ekspresi logika
print(False or True)

#operator aritmatika
x = 11
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)

#operator relasional operan integer
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print('__________--------________')
#operator relasional operan string 
x = 'Dicoding'
y =  'Indonesia'
print(x == y)
print(x != y)
print(x > y) #khusus string operasi seperti ini akan membandingkan huruf pertama pada string.
print(x < y)
print(x >= y)
print(x <= y)

print('__________--------________')
#operator logika
print('Logika and')
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('Logika Or')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('Logika Not')
print(not True)
print(not False)

print('__________--------________')
#operator assignment
# +=
x = 11
x += 5
print(x)
# -=
x = 11
x -= 5
print(x)
# *=
x = 11
x *= 5
print(x)
# /=
x = 11
x /= 5
print(x)
#%=
x = 11
x%= 5
print(x)

"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silaka
diskon = 500000
cek_diskon = (dico > diskon) * 0.10
potongan = dico * cek_diskon
total_harga = dico - potongan

print(cek_diskon)
print(potongan)
print(total_harga)