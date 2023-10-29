#1
a =["B 1234 BAC","Civic","200cc","biru"]
print (a)
 
#2
a = a + ["Rp600.000.000","4"]
print (a)

a.insert(2,"Honda")
a.insert(3,"Matic")
print (a)

#3
def hitung_luas_bangun_datar(pilihan):
    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print("Luas persegi:", luas)
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = 3.14 * jari_jari * jari_jari
            print("Luas lingkaran:", luas)
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga:", luas)
        case _:
            print("Pilihan yang Anda masukkan salah!")

pilihan = int(input("Masukkan pilihan (1 untuk persegi, 2 untuk lingkaran, 3 untuk segitiga): "))
hitung_luas_bangun_datar(pilihan)