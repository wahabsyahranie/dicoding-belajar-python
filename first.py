greeting = 'Hello World'
print(greeting)

addition = 2+2
result = addition - 1
print(result)

#ini melakukan input dan menyimpan ke variabel name
# name = input('Masukkan nama:')
# print(name)

"""
ini komentar dengan multi baris
Hello
"""

age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

##pada python menginisiasi ulang variabel tidak mengubah nilainya, karena variabel tersebut tersimpan dalam memori dengan id yang berbeda
x = 6
print(type(x))

x = "7"
print(type(x))
print(id(x))

x = 6.0
print(type(x))
print(id(x))

x = "7"
print(type(x))
print(id(x))

x = 1+2j
print(type(x))
print(id(x))

#menyimpan string lebih dari satu baris dengan single atau doubel quote
multi_line = """Halo!
Kapan terakhir kali kita bertemu
Kita bertemu hari jum'at yang lalu.
"""
print(multi_line)

#indexing
print(multi_line[0])

# #string pada python immutable
# multi_line[0] = 'Y'
# print(multi_line[0])

#ambil beberapa substring
print(multi_line[2:])

#formatted string
name = 'Wahab Syahranie'
print(f"Hello nama saya {name}")

#%-formatting
print("Nama saya %s" % (name))

#str.format
print("Kedua nama saya {}" .format(name))

#data collection atau list
x = [1, 2.2 , 'Dicoding']
print(type(x))
print(x[2])
##list bersifat mutable
x[2] = 'indonesia'
print(x[2])

#berbagai macam indexing
print(x[1])
print(x[-1])

#slicing
x = ['laptop', 'mouse', 'keyboard', 'webcam', 'microphone', 'headset']
print(x[0:5:2])
print(x[0:2])
print(x[1:])
print(x[:3])
print(x[:2])

#tuple bersifat immutable
x = (1, "dicoding", 1+2j)
print(type(x))
print(x[0:2])

#set adala kumpulan item tanpa urutan / tidak berlaku indexing (unordered collection)
x = {1,2,7,1,24,5}
# print(x[0])

#set juga bersifat unik, artinya data tidak akan duplikat, manfaatkan untuk menghilangkan duplikasi
x = {1,2,7,1,24,5,24,5}
print(x)

#set adalah himpunan dalam matematika, berarti kita dapat melakukan operasi union (gabungan)

