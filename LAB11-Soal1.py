#Daniel Adi Putranto
#71200574
'''
ada sorang anak kecil yang gemar memakan berebgai jenis permen
dia orang yang suka juga dengan perhitungan hingga dia mencoba
untuk menghitung berbagai jenis peremen kemudian ada berapa jenis permen
dalam toples tersbut, buatlah dengan dengan source code python.
'''
def hitung(permen):
    listpermen = list(permen)
    sortir = set(sorted(permen))
    totalsatuan = 0
    nominal = 5
    totalpermen = 0
    for i in sortir:
        hitungpermen = permen.count(i)
        nominal1 = nominal*hitungpermen
        sortir = print(f'permen berbagai {i} sejumlah {nominal1} permen')
        totalsatuan += nominal1
        totalpermen += 5
    print('Total permen di dalam toples adalah : ',len(listpermen),'permen jenis buah')
permen = ("Rasa mangga","Rasa apel", "Rasa jeruk", "Rasa anggur", "Rasa durian", "Rasa leci", "Rasa lemon", "Rasa kopi", "Rasa green tea")
hitung(permen)
