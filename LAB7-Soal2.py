#Daniel Adi Putranto
#71200574
'''
Gina adalah seorang mahasiswi dia mempunyai tugas yaitu mengetik dengan banyak
namun, dalam mengetik keyboard Gina rusak dan kadang-kadang menjadi huruf kecil menerus-nerus
dalam tugas tersebut dengan syarat harus huruf kapital semua.
'''
kata_awal = input("masukan kata: ")
kata_baru = ""
for kar in kata_awal:
    if kar.isupper():
        karbaru = kar.lower()
    elif kar.islower():
        karbaru=kar.upper()
    else:
        karbaru=kar
    kata_baru=kata_baru+karbaru
print(kata_baru)
