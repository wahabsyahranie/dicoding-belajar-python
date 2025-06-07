#Subprogram adalah serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Subprogram yang sering digunakan terdiri dari dua jenis, yakni berikut. terdapat dua jenis yaitu Fungsi dan Prosedur.

#fungsi adalah subprogram, dimana kita dapat menggunakannya berulang kali
def hitung_luas(panjang, lebar):
  luas = panjang * lebar
  return luas

persegi_pertama = hitung_luas(5,10)
print(persegi_pertama)
persegi_kedua = hitung_luas(4,15)
print(persegi_kedua)


# Docstring
'''Untuk membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring. Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.'''
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.
    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

#argumen dan parameter itu berbedam, parameter itu tempat menampung nilai, argumen adalah nilai yang kita berikan.
#keyword argumen, digunakan agar lebih spesifik, jadi data tidak akan tertukar jika programmer lupa.
def mencari_luas_persegi_panjang(panjang,lebar):
    pembagian = panjang/lebar
    return pembagian
persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)
print(persegi_panjang_pertama)
#positional argumen, tidak perlu menuliskan spesifik, tapi urutan argumen harus sesuai parameter
def mencari_luas_persegi_panjang(panjang,lebar):
    pembagian = panjang/lebar
    return pembagian
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

##parameter
#positional-or-keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))
#positional-only
def penjumlahan(a, b, /):
    return a + b
print(penjumlahan(8, 50))
#keyword-only
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan
print(greeting(pesan="Selamat sore!",nama="Dicoding"))
#var-positional(variadic positional parameter)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total
print(hitung_total(1, 2, 3))
#var-keyword (variadic keyword parameter)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

#Fungsi Anonim (lambda expression) (membuat fungsi tanpa menyebutkan def dan bisa diasumsikan one-liner)
#lambda digunakan bertujuan untuk operasi sederhana
luas_persegi = lambda panjang, lebar: panjang * lebar
print(luas_persegi(5,10))

#lokal
#variabel global dan lokal (scope variable)
def add(a, b):
    lokal_var = 5 #variabel lokal
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

#global
a = 10 #variabel global
def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

#menulis modul pada python
#buat file hello.py dan deklarasikan fungsi disana
import hello
#memanggil fungsi
persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5,10)
print('ini import modul')
print(persegi_panjang_pertama)

#memanggil variabel
print(hello.nama)

# from hello import mencari_luas_persegi_panjang, nama
# alternatif lain kita mengimpor variabel dan fungsi lain, dengan begitu kita tidak perlu secara spesifik menulis hello. pada setiap fungsi atau variabel.

def minimal(a,b):
    if a == b:
        return a
    else:
        return min(a,b)

print(minimal(5,10))

#prosedur berbeda dengan fungsi, karena prosedur tidak mengharuskan adanya paramter, dan dapat dipandang sebagai fungsi yang tidak menghasilkan nilai
#prosedur dengan parameter
def greeting(name):
    print("Hello " + name + ", Selamat datang!")
    return #bisa menambahkan return tapi tidak menyertakan value
greeting('Dicoding indonesia')
#prosedur tanpa parameter
def greeting():
    print("Hallo selamat datang")
    return
greeting()