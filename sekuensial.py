#Sekuensial = program python dijalankan secara berurutan
# print("Selamat datang dalam program Python!\n")
# print("Silakan masukkan data diri Anda.")
# nama = input("Masukkan nama Anda: ")
# tahun_lahir = input("Masukkan tahun lahir Anda: ")
# umur = 2023 - int(tahun_lahir)
 
# print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
# print("Terima kasih telah menggunakan program Python!")


#python interpreter
#block code, python sensitif terhadap indentasi
for i in range(10):
  print(i)
# for i in range(10):
# print(i) #error karena tidak ada indent (spasi)

#python case-sensitive
teks = 'Dicoding'
Teks = 'Indonesia'
print(teks)
print(Teks)

#python one-liner (single statement/membuat sebuah kode dalam satu baris)
x = 1
y = 2
#penulisan umum
temp = x
x = y
y = temp
print('setelah pertukaran:')
print('x =', x)
print('y =', y)

x = 1
y = 2
#penulisan on-liner
x, y = y, x
print('setelah pertukaran:')
print('x =', x)
print('y =', y)