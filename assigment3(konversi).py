def konversiSuhu(temperatur, satuan): #membuat fungsi konversiSuhu
    if satuan == 'C' or satuan == 'c': #pengondisian satuan celcius
        return (temperatur * 9/5) + 32
    elif satuan == 'F' or satuan == 'f': #pengondisian satuan farenheit
        return (temperatur - 32) * 5/9
    else:
        return "satuan tidak dikenali." 
   
temperatur = float(input("Masukkan temperatur : ")) #membuat variabel input temperatur
satuan = input("Masukkan satuan (C/F) : ") #membuat variabel input satuan

konversi_suhu = konversiSuhu(temperatur, satuan) #variabel untuk menampilkan hasil dari fungsi konversiSuhu
if satuan == 'C' or satuan == 'c':
    print(f"{temperatur}°C is {konversi_suhu}°F")
elif satuan == 'F' or satuan == 'f': 
    print(f"{temperatur}°F is {konversi_suhu}°C")
else :
    print("Input tidak valid")

