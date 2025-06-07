#ubah ke uppercase
kata = 'dicoding'
kata = kata.upper()
print(kata)

#ubah ke lowercase
kata = 'DICODING'
kata = kata.lower()
print(kata)

#hapus whitespace pada akhir string
kata = 'Dicoding        '
kata = kata.rstrip()
print(kata)

#hapus whitespace pada awal string
kata = '      Dicoding'
kata = kata.lstrip()
print(kata)

#hapus whitespace pada awal dan akhir string
kata = '      Dicoding        '
kata = kata.strip()
print(kata)

#hapus karakter selain whitespace
kata = 'wahabDicodingwahab'
kata = kata.strip('wahab')
print(kata)

#menemukan suatu kata pada awal string
kata = 'wahab dicoding'
kata = kata.startswith('wahab')
print(kata)

#menemukan suatu kata pada akhir string
kata = 'wahab dicoding'
kata = kata.endswith('wahab')
print(kata)

#menggabungkan string
kata = ['Dicoding', 'Indonesia', 'Emcy']
kata = ' '.join(kata)
print(kata)

#memisahkan string
kata = 'Wahab Syahranie!'
kata = kata.split()
print(kata)

#memisahkan setiap baris pada multi baris
kata = '''Halo,
eva
hello'''
kata = kata.split('\n')
print(kata)

#mengganti nilai string
kata = 'Ayo belajar dicoding'
kata = kata.replace('Ayo', 'gass')
print(kata)

#pengecekan pada string
kata = 'ABDUL'
kata = kata.isupper()
print(kata)

kata = 'ABDUL'
kata = kata.islower()
print(kata)

#pengecekan semua karakter dalam nilai adalah semua huruf alfabet
kata = 'abdul'
kata = kata.isalpha()
print(kata)

#pengecekan semua karakter dalam nilai adalah senua huruf atau semua angka alfabet atau berisi keduanya
kata = 'abdul123'
kata = kata.isalnum()
print(kata)

#pengecekan karakter adalah angka/numerik
kata = '123'
kata = kata.isdecimal()
print(kata)

#pengecekan jika nilai hanya berisi whitespace
kata = '        '
kata = kata.isspace()
print(kata)

#pengecekan jika kapital disetiap kata
kata = 'Wahab Syahranie Eva'
kata = kata.istitle()
print(kata)

##formatting pada string
#memastikan bahwa sebuah nilai memiliki panjang tetap
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

#membuat teks menjadi rata kanan
teks1 = teks.rjust(20)
teks2 = teks.rjust(20, 'w')
print(teks1)
print(teks2)

#membuat teks menjadi rata kiri
teks3 = teks.ljust(20)
print(teks3)

#membuat teks menjadi rata tengah
teks4 = teks.center(20)
print(teks4)

##String literals, quote didalam quote
st1 = "jum'at"
print(st1)
##quote didalam quote tetapi ada quote maka gunakan \
st2 = 'jum\'at'
print(st2)

#whitespace
st3 = 'yo hallo anjay \t slebew'
print(st3)

#backslash
st4 = 'yo hallo anjay \\ slebew'
print(st4)

#raw string mencetak sesuai apapun nilai mengabaikan formating
st5 = r'halo \\ gw emcy'
print(st5)


#operasi pada list, set, dan string
#list
contohList = [1,2,3,4,5,6]
print(contohList)
print(len(contohList))
#set
contohList = set([1,3,3,4,4,5])
print(contohList)
print(len(contohList))
#string
contohList = "Belajar Python"
print(contohList)
print(len(contohList))

#min dan max
angka = [13, 7, 24, 5,96]
print(min(angka))
print(max(angka))

#count
count = [2,4,4,5,5,5,5]
print(count.count(5))
string = "wahab eva wahab eva"
substring = "eva"
print(string.count(substring))

#in dan not in (mengembalikan boolean)
kalimat = "Belajar python di dicoding sangat menyenangkan"
print('dicoding' in kalimat)
print('tidak' in kalimat)
print('dicoding' not in kalimat)
print('tidak' not in kalimat)

#inisiasi nilai dari list/tuple ke dalam variabel (jumlah variabel harus sama dengan jumlah nilai)
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

#sort (mengurutkan secara ascending)
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
#sort (mengurutkan secara descending)
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)
##metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus didalamnya
##metode sort mengurutkan secara urutan ASCII (kapital akan duluan daripada huruf kecil)

var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

panjang = len(var_list)
maksimal = max(var_list)
minimal = min(var_list)
banyak = var_list.count(605132)

print(panjang)
print(maksimal)
print(minimal)
print(banyak)
