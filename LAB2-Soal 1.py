'''
Adi adalah karyawan tetap sebuah perusahaan mempunyai tangungan seorang istri dan satu anak tunjangan istri 5%
tunjangan anak 2% dari gajinya, gaji dipotong untuk dana kesehatan sebesar 3% 
untuk pajak penghasilan 10% untuk dana pensiun 7%. Hitunglah gaji neto perbulan!
'''

'''
istri = 5%
anak = 2%
kesehatan = 3%
pajak = 10%
pensiun = 7%
'''
uang = int(input("Masukan gaji: "))
uang1 = uang * 4
uang2 = uang1 * 5/100
uang3 = uang1 * 2/100
uang4 = uang2+uang3+uang1
uang5 = uang4 * 3/100
uang6 = uang4 * 10/100
uang7 = uang4 * 7/100
hasil = uang4 - uang5 - uang6 - uang7


print("Gaji awal: Rp", uang1)
print("Tunjangan istri: Rp", uang2)
print("Tunjangan anak: Rp", uang3)
print("Tunjangan anak dan istri: ", uang4)
print("Dana Kesehatan: Rp", uang5)
print("Pajak penghasilan: Rp", uang6)
print("Dana pensiun: Rp", uang7)
print("Saldo bersih: Rp", hasil)
