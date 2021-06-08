#71200574
#Daniel Adi Putranto

'''
Jeje sedang membantu memulihkan akun medsos pacarnya yang lupa password. Setelah berhasil 
pulih, ia pun ingin membuatkan password generator kepada pacarnya agar walaupun password-nya 
sederhana tetapi aman.
Bantulah Jeje membuat password generator dengan ketentuan sebagai berikut, lalu golongkan atas 2 
jenis tingkat keamanan.
- Kuat jika terdiri atas huruf besar, huruf kecil, angka, karakter spesial/symbol.
- Lemah jika tidak memenuhi salah satu kriteria di jenis tingkat keamanan kuat.
- Tidak valid jika:
1. length password kurang dari 6 dan melebihi 20 digit,
2. Ada whitespace
'''

import re 
def password(a):
    x = re.findall('\s',a)
    z = re.findall('\w\W',a)
    if (x) or len(a) < 6 or len(a) > 20:
        print('Password invalid, cek ketentuan ya')
    else:
        if z:
            print('password kuat, mantap!')
        else:
            print('password masih lemah sayang')
         


a = input('Masukkan Password: ')
password(a)
