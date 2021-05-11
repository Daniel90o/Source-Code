#Daniel Adi Putranto
#71200574

'''
Hizki seorang ketua dari anak-anak pramuka dan ingin mendata dari seluruh semua orang
dari semua orang 1 kelompok 2 orang. Lalu hizki ingin memastikan keseluruh anak-anak
membawa barang yang tidak sama, hingga hizki meminta tolong programrer untuk membuat
program yang bisa mendata keseluruhan siswanya dan dapat menampilkan jika ada yang berbeda
dari membawa keseluruhan barang-barang tersebut.
'''

a = int(input("masukkan keseluruhan barang yang dibawa anak pertama: "))
b = int(input("masukkan keseluruhan barang yang dibawa anak kedua: "))
set1 = set()
set2 = set()
e = "Masukkan barang-barang anak pertama: "
f = "Masukkan barang-barang anak kedua: "
print(e)
for i in range(a):
    c = str(input())
    set1.add(c)
print(f)
for i in range(b):
    d = str(input())
    set2.add(d)
perbedaan = set1.union(set2) - set1.intersection(set2)
print(perbedaan)
