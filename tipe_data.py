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

#set adalah himpunan dalam matematika, berarti kita dapat melakukan operasi union (gabungan) dan intersection (irisan)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

#dictionary
x = {'name': 'emcy', 'age' : 8, 'isMarried' : False}
print(type(x))
#pengambilan nilai pada dictionary harus mengetahui key nya
print(x['name'])
#menambahkan nilai pada dictionary
x['job'] = 'Web Developer'
print(x)
#mengahpus nilai pada dictionary
del x['isMarried']
print(x)
#mengubah nilai pada dictionary
x['name'] = 'Dicoding'
print(x)

#konversi data
print(float(5))
print(int(-5.6))
print(int("25"))
print(str(25))
print(float("25"))
print(str(2.5))
print(set([1, 2, 3]))
print(tuple({1, 3, 5}))
print(list('hello'))
#konversi ke dictionary, data harus memiliki key-value
print(dict([[1,2], [3,4]]))
#konversi list dari beberapa tuple
print(dict([(3, 26), (6, 19)]))