#71200574
#Daniel Adi Putranto
'''
Kita disuruh membuat program konversi, konversi tersebut nanti akan dimasukan beberapa angka
kemudian angka tersebut di konversi kemudian dibasi agar menjadi bilangan okta atau menjadi
angka atau heksa.Seperti contoh memasukan angka 432,2 untuk mengkoversi menjadi 432 bilangan biner
atau angka dengan basi 2. Dan 432,16 digunakan untuk mengkonversi angka 432 menjadi bilangan berbasi 16 atau heksa.
Buatlah program tersebut agar lebih meudah untuk dipakai semua orang.
'''

def toStr(n,base):  
    convertString = "0123456789ABCDEF"  
    if n < base:      
        return convertString[n]  
    else:      
        return toStr(n//base,base) + convertString[n%base]
print("silahkan masukkan angka dan basis yang kalian inginkan.")
angka = int(input("silahkan masukkan : "))
basis = int(input("masukkan basis : "))
print(toStr(angka,basis))
