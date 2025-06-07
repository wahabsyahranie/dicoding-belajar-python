#elemen matrix dideklarasikan memiliki tipe homogen yang artinya elemen tersebut harus mempunyai tipe sata yang sama, meskipun dalam list python kita dapat membuat matriks dengan tipe data berbeda, alangkah lebih baik jika tetap mengikuti aturan ini

#matriks dipython bisa dnegan nested list, akan tetapi metode ini sangatlah boros penyimpanan karena setiap elemen dalam list, akan disimpan dalam memori, alih-alih seperti ini, kita bisa menggunakan library numpy untuk lebih efisien.
matriks = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(matriks)

#install numpy pada komputer dengan terminal ->pip install numpy
import numpy

matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)

#kedepan kita akan menggunakan list python, ini agar kita dapat lebih memahami fundamental matriks.

#nested list dan nested for
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)

var_mat = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]
print(var_mat[2][1]) #var_mat[baris][kolom]

#operasi matriks
var_mat = [[5,0],
           [1,-2]]
def_mat = [[0 for j in range(2)] for i in range(2)]
for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2
print(def_mat)

#operasi matriks dengan numpy
var_mat = numpy.array([[5,0],
                       [1,-2]])
result = var_mat*2
print(result)

#eksplorasilah dnegan transpose, inverse, dsb.