import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r #Mendefinisikan sebuah fungsi anonim menggunakan lambda. 
#Fungsi ini menerima satu parameter (r) yang merupakan jari-jari lingkaran.

jari_jari = float(input("Masukkan jari-jari : ")) #input nilai dari pengguna
luas = luas_lingkaran(jari_jari) #Memanggil fungsi luas_lingkaran dengan argumen jari_jari (nilai jari-jari yang dimasukkan oleh pengguna).
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}") #cetak hasil perhitungan