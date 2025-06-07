#array dan list merupakan hal yang berbeda dalam Python. Kendati demikian, Anda bisa menggunakan list sebagai array dalam Python.
#jika benar-benar ingin menggunakan array, kita perlu mengimport library dan modul array
#nilai dalam array harus sama, sedangkan list boleh berbeda
import array

#list
x = [1,2,3,4,5]
print(x)

#array
x = array.array('i',[1,2,3,4,5])
print(x)
print(type(x))

#list bisa dibagi menjadi linear dan non-linear
#linear
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
print(siswa)
print(siswa[0])

#array comperhenssion
var_arr = [0 for i in range(10)]
print(var_arr)
#mengubah nilai default
for i in range(10):
  var_arr[i] = i
print(var_arr)
#mengakses nilai dalam array/indexing
print(var_arr[0])

#pemprosessan sekuensial
var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
  current_element = var_arr[i]
  next_index = i+1
  if next_index < len(var_arr):
      next_element = var_arr[next_index]
  else:
      next_element = None
  print(f"Current element: {current_element}, next elements: {next_element}")

#mengambil nilai terbesar dalam array
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(1, len(var_arr)):
   right_pointer = var_arr[i]
   if right_pointer > left_pointer:
      left_pointer = right_pointer
print(left_pointer)

var_array = [i for i in range(101)]
jumlah_nilai = len(var_array)
nilai = 0
for i in var_array:
   nilai += i
result = nilai/jumlah_nilai
print(result)