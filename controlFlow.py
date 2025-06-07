#percabangan
ketersediaan = 'Daging ayam'
if ketersediaan == 'Daging ayam':
  print('ibu membeli dan memasak ayam')
else:
  print('ibu membeli dan memasak tempe')

#one-liner percabangan
if ketersediaan == 'Daging ayam': print("Daging gak si")

#percabangan lebih dari dua
ketersediaan = 'Daging sapi'
if ketersediaan == 'Daging ayam':
  print('ibu membeli dan memasak ayam')
elif ketersediaan == 'Daging sapi':
  print('ibu membeli daging sapi')
else:
  print('ibu membeli dan memasak tempe')

#percabangan dengan multi indikator
nilai = 81
perilaku = 'tidak baik'
if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

#ternary operators (versi one-liner dari if dan else)
lulus = False
print('Selamat') if lulus else print('Perbaiki')

#opsi lain ternary adalah melibatkan tuple (hindari, komunitas python sendiri mengganggap bahwa ini kurang pythonic)
kelulusan = ('Perbaiki, anda belum lulus.', 'Selamat, anda lulus') [lulus]
print(kelulusan)

#perulangan
#for
data = [1,4,5,6,7,8]
for i in data:
  print(i)
for i in range(5):
  print(i)
#range(start,stop,step) stop bernilai eksklusif(nilai akhir tidak disertakan)
for i in range(1,9,2): print(i)

#while (perulangan yang menghasilkan true, false)  becarefull infinite loop
counter = 1 
while counter <= 5: 
  print(counter)
  counter += 1

#for bersarang (nested loop)
for i in range(1, 3):
  for j in range(1, 3):
    print(i,j)

#kontrol perulangan
#break
for i in range(2):
  print('perulangan luar:', i)
  for j in range(10):
    print('perulangan dalam:', j)
    if j == 1:
      break
for huruf in 'dico ding':
  if huruf == ' ':
    break
  print('huruf saat ini: {}'.format(huruf))

#continue (berhenti dan lanjut iterasi berikutnya)
for huruf in 'dico ding':
  if huruf == ' ':
    continue
  print('huruf saat ini: {}'.format(huruf))

#else setelah for
numbers = [1,3,5,6]
for num in numbers:
  if num == 3:
    print('angka ditemukan, program berhenti')
    break
else:
  print('angka tidak ditemukan')

#else setelah while
count = 0
while count < 3:
  print('dicoding indonesia')
  count += 1
else:
  print('Blok else dieksekusi karena kindisi pada while salah')

n = 10 
while n > 0:
  n = n - 1
  if n == 7:
    break
  print(n)
else:
  print('loop selesai')

#Pass (digunakan jika mengiginkan sebuah pernyataan atau blok pernyataan, tetapi tidak ada tindakan atau program tidak melakukan apapun)
x = 10
if x > 5:
  pass
else:
  print('Nilai x tidak memenuhi kondisi')

#list comprehension (membuat sebuah list baru berdasarkan list yang sudah ada)
angka = [1,2,3,4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)
#cara lain list comprehension
pangkat = [n**2 for n in angka]
print(pangkat)


evenNumber = []
for i in range(0, 501, 2):
  evenNumber.append(i)
print(evenNumber)

#error handling
#try-except
z = 0
try:
  print(1/z)
except:
  print('Anda tidak bisa membagi angka dengan {}'.format(z))
#pada program yang lebih kompleks kita bisa melakukan ini
# try:
#   # Blok kode Anda yang mungkin terjadi pengecualian.
# except:
#   # Pernyataan yang dioperasikan jika terjadi pengecualian.
# else:
#   # Pernyataan yang dioperasikan jika TIDAK terjadi pengecualian.
# finally:
#   # Pernyataan yang dioperasikan setelah semua pernyataan di atas terjadi.

var_dict = {"rata_rata": "1.0"}
try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

#raise exception (ketika membuat program ingin membatasi dengan kondisi tertentu)
var = -1
if var < 0:
  raise ValueError('Bilangan negatif tidak diperbolehkan')
else:
  for i in range(var):
    print(i+1)

