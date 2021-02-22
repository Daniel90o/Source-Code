'''
Karyawan sebuah persuhaan dengan NIK 7280401901 dia akan menentukan 
kedudukan dalam pekerjaan yang di inginkan dengan ketentuan
gaji sebesar Rp 1.000.000 tetapi ada bonus yang akan diterima berdasarkan gol, 
jika gol Stela bonus yang akan diterima sebesar Rp 2.000.000
, gol B Rp 4.000.000 dan gol C Rp 5.500.000 namun demikian 
jika Stella menjadi karyawan Honor gaji yang akan ditermia sebesar Rp 750.000 dan juga
ada bonus yang akan diterima menurut gol juga jika 
gol A bonusnya sebesar Rp 150.000, gol B Rp 270.000 dan gol C Rp 480.000
'''

Nama= input('Nama Karyawan: ')
NIK= input('NIK Karyawan: ')
Status= input('Status (Staff/Honor): ')
Gol= input('Golongan (A/B/C): ')
if(Status=='Staff'):
    Gaji=1000000
    if(Gol=='A'):
        Bonus=2000000
    elif(Gol=='B'):
        Bonus=4000000
    elif(Gol=='C'):
        Bonus=5500000
elif(Status=='Honor'):
    Gaji=750000
    if(Gol=='A'):
        Bonus=150000
    elif(Gol=='B'):
        Bonus=270000
    elif(Gol=='C'):
        Bonus=480000
Gatot = Gaji + Bonus
print('Gaji : Rp.',Gaji)
print('Bonus : Rp.',Bonus)
print('Gaji Total : Rp.',Gatot)
