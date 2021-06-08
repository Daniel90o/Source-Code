#71200574
#Daniel Adi Putranto

'''
Word Riani error sehingga setiap spasi ada yang hilang dan ada yang double. Dalam waktu yang
singkat ia harus memberikan laporan kepada atasannya total jumlah engagement twitter dan
Instagram perusahaan mereka.
Bantulah Riani menghitung angka (bil bulat) engagement dari setiap kalimat yang diberikan.
'''

import re
def hasil(a):
    b = re.findall('\d+',a)
    a = 0
    for i in b:
        a += int(i)
    print(a,'total engagement')

hasil('''3500orangmerepostpostingadiinstagramdan3000retweetditwitter'''
)
