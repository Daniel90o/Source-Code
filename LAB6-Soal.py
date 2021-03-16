#Daniel Adi Putranto
#71200574
'''
Hitunglah perkalian 2 buah matrix A dan B dengan sebagai berikut
A= [8, 4] [3, 2] dan B= [11, 3] [8, 9] 
Buatlah program seperti kalkulator
'''

def BagianMatrix (x,y):
    matriks=[]
    for i in range (x) :
        kol=[]
        for j in range (y):
            i= str(i)
            j= str(j)
            data=int(input("matriks["+i+","+j+"]"))
            kol.append(data)
        matriks.append(kol)
    return matriks
def PerkalianMatrix (a,b):
    matrik=[]
    for i in range(len(a)):
        kol=[]
        for j in range(len(b)):
            tambah=0
            for k in range(len(a)):
                tambah=tambah+(a[i][k]*b[k][j])
            kol.append(tambah)
        matrik.append(kol)
    return matrik
mat1 = BagianMatrix(2,2)
print ("Matriks 1 :",mat1)
mat2 = BagianMatrix(2,2)
print("Matriks 2 :",mat2)
kali = PerkalianMatrix(mat1,mat2)
print('Hasil',kali)
