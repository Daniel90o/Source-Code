'''
Sebuah usaha yang dilakukan dengan menyewakan hotel, semakin hari semakin banyak pengunjungnya, membuat pengusaha hotel "HOTEL BINTANG 5"
ini kewalahan dalam transaksinya, kenapa tidak, setiap tamu hadir dapat dipenuhi keinginnya seolah setiap jenis kamar tanpa ada batasnya, tidak pernah kehabisan,
kamar bisa disulap sesuai permintaan tamu, biasanya digunakan untuk menginapnya para wisudawan, dengan ketentuan sebagai berikut:
S mewakili single yaiu jenis kamar dengan harga permalam Rp 150.000 dan D mewakili double dengan harga Rp 350.000 dan F mewakili family dengan harga Rp 500.000 .
Jika sesudah memilih kamar dan melebihi Rp 2.000.000 akan mendaoatjan handuk hotel kalau tidak totebag.
'''

garispjg="-----------------------------------------------"
garispdk="---------------------------------------"
print("HOTEL BINTANG 5")
print(garispdk)
print("kode     Jenis Potong       Harga")
print(garispdk)
print("1=S        Single             Rp. 150.000")
print("2=D        Double             Rp. 358.000")
print("3=F        Family             Rp. 500.000")
print(garispdk)
data = int(input("\nMau sewa berapa jenis kamar? "))

#deklraasi variabel list
listKK = []
listBK = []


for x in range(data):
    print("\nData ke - ",x+1)
    kdk = input("Kode Kamar [S|D|F] : ")
    listKK.append(kdk)
    bkk = int(input("Banyak Kamar : "))
    listBK.append(bkk)
    print(garispdk)


print("HOTEL BINTANG 5")
print(garispjg)
print("No.  Jenis   Harga       Lama Inap   Jumlah")
print("     Kamar   per Malam   (Malam)     Harga")
print(garispjg)


tot=0
for a in range (data):
    if(listKK[a]=="S" or listKK[a]=="s"):
        jk="Single"
        harga = 150000
    elif(listKK[a]=="D" or listKK[a]=="d"):
        jk = "Double"
        harga = 350000
    elif(listKK[a]=="F" or listKK[a]=="f"):
        jk = "Family"
        harga = 500000
    else:
        jk = "......."
        harga = 0

    subtot = harga*listBK[a]
    tot = tot+subtot
    print(a+1, "    ",jk,"    ",harga,"    ",listBK[a], "   Rp. ",subtot)

if tot > 2000000:
    bonus = "Handuk"
else:
    bonus = "Totebag"
print(garispjg)
print("                         Total  : Rp. ",tot)
print("                         Bonus  : ",bonus)
