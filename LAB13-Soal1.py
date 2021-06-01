#71200574
#Daniel Adi Putranto
'''
Ada sebuah soal yang susah dikarenakan soal tersebut berpangkat semua,
hinggan meminta anak-anak informatika untuk membuatkan sebuah program agar bisa memangkatkan
seperti contoh 4 pangkat 4 hasilnya adalah 256. buatlah program tersebut menggunakan x dan y.
'''

def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))
