# library text processing
# string
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pickle
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from datetime import datetime
import argparse
import math
import re
test = 'dicoding'
print(test.upper())
print(test.lower())
print(test.title())
print(test.split('i'))
print(test.zfill(20))

# regex, mencari teks berdasarkan pola tertentu

pola = '^a...s$'
string_test = 'abyss'
hasil = re.match(pola, string_test)

if hasil:
    print('pencarian berhasil!')
else:
    print('tidak ditemukan')

# library matematika
print(math.sqrt(25))
print(math.pi)

# library parser, jika kita ingn membuat program atau skrip kecil  yang langsung menerima parameter pada saat pemanggilan program
# basic contoh
# parser = argparse.ArgumentParser()
# parser.add_argument('-o', '--output', action='store_true',
#                     help='tampilkan output')
# args = parser.parse_args()
# if args.output:
#     print('Halo, ini merupakan sebuah output dari panggildicoding')
# argumen bersifat wajib contoh

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True,
                    help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True,
                    help="Masukkan Tanggal Lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()

if args.tanggallahir:
    ttl_str = args.tanggallahir
    ttl = datetime.strptime(ttl_str, "%d-%m-%Y")
    hari_ini = datetime.today()

    usia = hari_ini.year - ttl.year - (
        (hari_ini.month, hari_ini.day) < (ttl.month, ttl.day)
    )

    if usia < 30:
        print("Terima kasih telah menggunakan panggildicoding.py, kakak "+args.nama)
    else:
        print("Terima kasih telah menggunakan panggildicoding.py, bapak "+args.nama)

    print("Usia anda saat ini adalah " + str(usia))

# Library pengolahan data
# pandas, adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.
# membuat dataframe dari dictionary
data = {
    'Nama': ['John', 'Emcy', 'Eva'],
    'Usia': [25, 22, 20],
    'Pekerjaan': ['Engineer', 'Teaher', 'House Wife']
}
df = pd.DataFrame(data)

# menampilkan dataframe
print(df)

# NumPy, adalah package fundamental yang sering digunakan untuk scientific computing pada Python. Library ini menyediakan objek array multidimensi, berbagai jenis objek lainnya, seperti masked array dan matrix, dan sebagainya.
matriks = numpy.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print(matriks)

# matplotlib, library untuk melakukan visualisasi data.
# data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 6, 7]
# membuat plot garis
plt.plot(x, y)
# menambahkan judul dan label sumbu
plt.title('Contoh plot garis')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu y')

# menampilkan plot
# plt.show()

# seaborn, termasuk jenis library dengan tujuan untuk visualisasi data sama seperti matplotlib. Bahkan library seaborn dibangun berdasarkan pada library matplotlib.
# contoh data
tips = sns.load_dataset('tips')  # membuat dataset tips dari seaborn

# contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram total bill')
plt.xlabel('total bill')
plt.ylabel('frequency')
# plt.show()

# library file management
# os,  berguna untuk fungsi-fungsi yang berkaitan dengan sistem operasi, misalnya open(), path(), getcwd(), dan fungsi lainnya. Modul ini memungkinkan Anda untuk memanfaatkan fungsi yang sama dan mengeksekusi fungsi terkait OS yang mungkin berbeda dalam setiap sistem operasi. Ada beberapa fitur yang hanya bekerja pada sistem operasi tertentu.
print(os.getcwd())  # mengembalikan direktory yang digunakan saat ini

# json, adalah format text yang ditujukan untuk serialization. Agar data dapat dengan mudah ditransmisikan antar berbagai sumber tanpa khawatir bentuknya kacau, menggunakan JSON adalah salah satu pilihan yang tepat.
# contoh json
x = '{"nama":"buchori", "umur":22, "kota":"new york"}'
# parse x
y = json.loads(x)
print(y['umur'])

# pickle, adalah istilah untuk mengubah objek menjadi byte stream, sedangkan unpickling adalah perlakuan sebaliknya.
contoh_dict = {1: "6", 2: "2", 3: "f"}

# menyimpan pada sebuah file
pickle_keluar = open("dict.pickle", "wb")
pickle.dump(contoh_dict, pickle_keluar)
pickle_keluar.close()

# mengekstrak dan menaruh isi pada variabel
pickle_masuk = open("dict.pickle", "rb")
contohDict = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDict)

# library web scrapping, adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. Proses ini disebut sebagai “web scraping” atau “web crawling”. Anda bisa menggunakan fungsi dan metode pada library ini untuk mengekstraksi informasi dari situs web dan menyimpannya dalam format yang dapat diakses dan digunakan dalam analisis atau aplikasi lainnya.
# beautifulsoup, adalah library untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan
# pengambilan conten
url = "http://himati.test/"
page = urlopen(url)
html = page.read().decode("utf-8")

# membuat objek beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# cetak judul halamam
# print(soup.body)

# urllib, adalah library bawaan dari Python yang bertujuan untuk scraping konten dari sebuah website
url = "http://himati.test/"
page = urlopen(url)
html = page.read().decode("utf-8")

# mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)

'''Library Machine Learning'''
# scikit-learn, menyediakan berbagai algoritma pemelajaran mesin siap pakai untuk membantu dalam pengembangan model pemelajaran mesin, pemrosesan data, dan evaluasi kinerja model.
# pip install -U scikit-learn

# tensorflow, library paling populer terkait machine learning. Dengan menggunakan TensorFlow, Anda bisa mengembangkan machine learning hingga tahap deployment.
# pip install tensorflow

# pytorch, library machine learning yang dikembangkan oleh Facebook’s AI Research lab (FAIR). PyTorch menyediakan alat dan kerangka kerja yang kuat untuk mengembangkan model pemelajaran mesin, terutama dalam konteks jaringan saraf tiruan (neural networks).
# pip install torch torchvision torchaudio

'''Library Web Development'''
# django, high-level Python web framework yang mendukung pengembangan secara cepat, bersih, serta pragmatis
# python -m pip install Django

# flask, adalah web framework dalam Python yang ditujukan untuk membangun aplikasi web. Flask dirancang dengan tujuan menjadi ringan, fleksibel, dan sederhana
# pip install Flask

# fast API, adalah web framework untuk Python yang tujuannya merancang dan membangun API dengan cepat, efisien, dan aman.
# pip install fastapi

