# class adalah cetakan (blueprint)
# object adalah perwujudan dari class
# method adalah tindakan yang dapat dilakukan object didalam class
# atribut adalah identitas dari object atau class
class Mobil:
    # pass
    warna = 'merah'  # atribut class


mobil_1 = Mobil()
mobil_1.warna = 'biru'
print(mobil_1.warna)

mobil_2 = Mobil
print(mobil_2.warna)

# dalam oop ada atribut kelas dan atribut object/instance
mobil_3 = Mobil
# mengubah atribut kelas
Mobil.warna = 'Green'
print(mobil_3.warna)

# membuat atribut instance perlu menggunakan constructor
# class constuctor


class Motor:
    # atribut object
    def __init__(self):
        self.warna = 'Merah'


motor_1 = Motor()
motor_2 = Motor()
print(motor_1.warna)
print(motor_2.warna)

# mengubah atribut instance
motor_1.warna = 'Hitam'
print(motor_1.warna)
print(motor_2.warna)


class Mobil:
    # atribut object tidak memiliki default, ini berarti pemanggilan harus menginisiasi argumen
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


mobil_1 = Mobil('Merah', 'DicodingCar', 150)
print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

# method, pada pembuatannya. sebenarnya kita mmebuat fungsi didalam kelas itu sendiri ('def). python membagi method menjadi tiga jenis
# 1. metode dari object (object method)
# 2. metode secara statis (static method) #konsep dekorator
# 3. metode dari class (class method) #konsep dekorator

# dekorator


def my_decorator(func):
    def wrapper():
        print('sebelum fungsi dieksekusi')
        func()
        print('sesudah fungsi dieksekusi')
    return wrapper
# dekorasi fungsi dengan dekorator


@my_decorator
def say_hello():
    print('Hello world!')


# memanggil fungsi yang sudah didekorasi
say_hello()

# method dari object


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


mobil_1 = Mobil('merah', 'dicodingcar', 160)
print('sebelum ditambahkan: ')
print(mobil_1.kecepatan)
# memanggil method tambah_kecepatan
mobil_1.tambah_kecepatan()
print('setelah ditambahkan: ')
print(mobil_1.kecepatan)
# object method adalah metode yang melekat terhadap objek dan menggunakan parameter self. jadi kita tidak bisa memanggil metode ini langsung melalui kelasnya.

# static method
# Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print('ini adalah metode dari kelas mobil')


Mobil.intro_mobil()
mobil_1 = Mobil('dicodingcar')
mobil_1.intro_mobil()

# method  dari class
# Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):  # parameter wajib dalam menggunakan dekorator @classmethod, untuk penamaan tidak harus cls, tapi berdasarkan kesepakatan bersama programmer
        print('ini adalah metode dari kelas mobil')


Mobil.intro_mobil()
mobil_1 = Mobil('dicodingcar')
mobil_1.intro_mobil()


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)


Mobil.intro_mobil()
mobil_1 = Mobil('dicodingcar')
mobil_1.intro_mobil()

# inheritance (pewarisan)


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


mobil_1 = Mobil('gray', 'bmw', 170)
print(mobil_1.kecepatan)

# membuat class baru yang mewarisi class mobil


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50


# kelas Mobil dasar
mobil_1 = Mobil('Merah', 'halley', 160)
print(mobil_1.kecepatan)
# kelas mobil sport
mobil_sport_1 = MobilSport('hitam', 'molle', 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

# override, ketika kita membuat metode baru di kelas turunan (kelas baru) dengan nama yang sama seperti metode di kelas induk, itu akan menyebabkan metode baru menimpa (override) metode dari kelas induk.


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        self.kecepatan += 20


# kelas mobil sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()  # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

# super, konsep ini untuk menghindari kode berulang dan memanfaatkan fungsi yang sudah ada pada kelas induk (super class)


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")


# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()  # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

# tugas kuis
print('KUIS CODING')


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    def deskripsi(self):
        print(
            f'{self.name} adalah kucing berjenis {self.species} yang berumur {self.age} tahun')
        # return f'{self.name} adalah kucing berjenis {self.species} yang berumur {self.age} tahun'

    def suara(self):
        print('meow!')
        # return 'meow!'


# instance
myCat = Cat('Neko', 3, 'Persian')
myCat.deskripsi()
myCat.suara()
