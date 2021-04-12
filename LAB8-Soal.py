'''
Ada suatu permasalahan dengan daftar belanja yang bernama yanti, dia selalu
lupa dalam meletakan daftar belanjanya karena bermain hp hingga dia meminta
bantuan untuk membuat program daftar belanja agar lebih mudah dan tidak kehilangan.
'''

def tambah_belanja(text):
    file = open('C:\\Users\\danie\\Videos\\PrakAlPro\\belanja.txt', 'a+')
    file.write('\n' + text)

def daftar_belanja():
    file = open('C:\\Users\\danie\\Videos\\PrakAlPro\\belanja.txt', 'a+')
    file.seek(0)
    text = file.read()
    print(text)

def tentang_program():
    tentang = open('C:\\Users\\danie\\Videos\\PrakAlPro\\about.txt', 'r')
    app = tentang.read()
    print(app)
 
def membaca_daftar_source_code():
    kode = open('C:\\Users\\danie\\Videos\\PrakAlPro\\source.txt', 'r')
    apps = kode.read()
    print(apps)
 
def tanya_pengguna():
    print('Silahkan Masukan Keperluan Belanja anda Ke daftar Belanja')
    print('====================== Daftar Belanja ===================')
    tambah_belanja(input('Mau Belanja Apa :  '))

 
loop = True
 
print('================== Menu ==============')
print('1. Tambah ke Daftar Belanja')
print('2. List Belanja')
print('3. Quit/ Keluar')
print('4. Tentang Apps')
print('5. Lihat code')
print('======================================')
while (loop):
    print('\n')
    menu = input('Masukan menu = ')
    if menu == "1":
        tanya_pengguna()
    elif menu == "2":
        daftar_belanja()
    elif menu == "3":
        quit()
    elif menu == "4":
        tentang_program()
    elif menu == "5":
        membaca_daftar_source_code()
    else:
        print("command not found")
