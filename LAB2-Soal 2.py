'''
Canny merupakan anak kost. Dia memiliki total saldo uang bulanan yang diberikan oleh orang tuannya. 
Setiap bulan ada saja pengeluaran yang dikeluarkan olehnya. 
Cari cara untuk membantu Canny menghitung sisa saldo uang bulananya setelah mengeluarkan beberapa uang yang dikeluarkan.
Note: -1 untuk keluar/selesai

'''
awal = int(input("Masukan saldo awal:"))
sisa = awal 
while(True):
    pengluaran = int(input("Masukan pengluaran hari ini(-0 untuk keluar): "))
    if pengluaran ==-0: 
        print("Sisa saldo =", sisa) 
        break
    sisa = sisa - pengluaran
    if sisa<0:
        print("Saldo tidak cukup")
        print("Sisa saldo ",sisa+pengluaran)
        break