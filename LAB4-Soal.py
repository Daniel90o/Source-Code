'''
Warung Makan Warung Makan Berkah dengan tarif sebagi berikut:
1. Makanan: - Ayam Bakar dengna harga Rp.15_000
            - Ikan Bakar dengan harga Rp.10_000
            - kalau Sate harganya Rp.8_000
2. Minuman: - Kopi harganya Rp.4_000
            - Es teh harganya Rp.3_000
            - Jus Alpukat seharga Rp.8_000
Dari pilihan tersebut bisa memesan beberapa sesuai keinginan
'''

def menu ():
    print("Menu Pilihan")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Keluar")
def Makanan ():
    print("Makanan")
    print("1. ayam bakar")
    x= int(input("Jumlah pesasanan yang diinginkan : "))
    ayam= x*15000
    print("Jumlah :",ayam)
    print("2. Ikan bakar")
    y= int(input("Jumlah pesanan yang diinginkan : "))
    ikan= y*10000
    print("Jumlah :", ikan)
    print("3. Sate Ayam")
    z= int(input("Jumlah pesanan yang diinginkan : "))
    sate= z*8000
    print("Jumlah :",sate)
    print("Bayar")
    Bayar= ayam+ikan+sate
    print("Jumlah :",Bayar)
    ulang= str(input("Apakah ingin memesan lagi. [Ya/Tidak]? : "))
    if ulang =="Ya" or "Tidak":
        menu()
    else:
        exit()
def Minuman ():
    print ("Menu minuman")
    print ("1. Es teh")
    t= int(input("Jumlah pesanan yang diinginkan : "))
    teh= t*3000
    print ("Jumlah :",teh)
    print ("2.kopi")
    k= int(input("Jumlah pesanan yang diinginkan : "))
    kopi= k*4000
    print ("Jumlah :",kopi)
    print ("3. Jus Alpukat")
    j= int(input("Jumlah pesanan yang diinginkan : "))
    jus= j*8000
    print ("Jumlah :",jus)
    print ("Bayar")
    bayar= teh+kopi+jus
    print("Jumlah :",bayar)
    ulang= str(input("Apakah ingin memesan lagi. [Ya/Tidak]? : "))
    if ulang =="Ya" or "Tidak":
        menu ()
    else:
        exit()
print ("======== Warung Makan Berkah ========")
print 
menu ()
while 1:
    pilih = int(input("Pilihlah salah satu yang ada di menu : "))
    if pilih == 1:
        Makanan ()
    elif pilih == 2:
        Minuman ()
    elif pilih == 3:
        print ("\n")
        break
