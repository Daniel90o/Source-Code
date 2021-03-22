#Daniel Adi Putranto
#71200574
'''
Ada suatu hari guru TK meminta tolong untuk membuatkan program huruf vokal tersebut 
diganti mengunakan huruf E karena guru tersebut agar lebih mudah mengajar anak-anak
dengan mudah saat pembelajaran jarak jauh ini.
'''
def masuk():
    masukkan = str(input("Masukkan Input : "))
    masukkan1 = masukkan.replace('a', 'e')
    masukkan2 = masukkan1.replace('i', 'e')
    masukkan3 = masukkan2.replace('u', 'e')
    masukkan4 = masukkan3.replace('e', 'e')
    masukkan5 = masukkan4.replace('o', 'e')

    print (masukkan5)
masuk()
