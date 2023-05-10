# Dosya adı ve dosya yolu
filename = "Kisi_Bilgileri.txt"

# Yeni kullanıcı ekleme
def yeni_kullanici():
    kimlik_no = input("Kimlik numarası girin: ")
    ad = input("Ad girin: ")
    soyad = input("Soyad girin: ")
    yas = input("Doğum Yılı girin: ")
    cinsiyet = input("Cinsiyet girin")
    oncelik_durumu = input("Oncelik durumu girin: ")

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(f"{kimlik_no},{ad},{soyad},{yas},{cinsiyet},{oncelik_durumu}\n")

# Kullanıcının bilgilerini al
def kullanici_bilgileri(kimlik_no):
    with open(filename, 'r', encoding="utf-8") as f:
        for satir in f:
            bilgiler = satir.strip().split(',')
            if bilgiler[0] == kimlik_no:
                return bilgiler[1], bilgiler[2], bilgiler[3], bilgiler[4], bilgiler[5]

    return None

# Kullanıcının bilgilerini yazdır
def kullanici_bilgileri_yazdir():
    kimlik_no = input("Kimlik numaranızı girin: ")
    bilgiler = kullanici_bilgileri(kimlik_no)
    if bilgiler is None:
        print("Kimlik no hatalı.")
    else:
        print(f"{bilgiler[0]} {bilgiler[1]} lütfen bekleyiniz...")

# Ana menü
while True:
    print("\n1 - Yeni kullanıcı ekle")
    print("2 - Kullanıcının bilgilerini yazdır")
    print("3 - Çıkış")
    secim = input("Seçiminizi girin (1/2/3): ")

    if secim == '1':
        yeni_kullanici()
    elif secim == '2':
        kullanici_bilgileri_yazdir()
        break
    elif secim == '3':
        break
    else:
        print("Geçersiz seçim")
        
# --------------------------------------------
while True:
    print("Lütfen seçim yapınız:")
    print("1- Doktor Girişi")
    print("2- Hasta Girişi")
    print("3- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        parola = input("Şifre girin: ")
        if parola == "doktor":
            print("Giriş Yapılıyor. Lütfen Bekleyiniz...")
            # Doktor işlemlerini buraya yazıcaz @sara.
        else:
            print("Parola yanlış! Tekrar deneyin...")

    elif secim == "2":
        with open("Kisi_Bilgileri.txt", "r", encoding="utf-8") as dosya:
            kimlik_no = input("Kimlik numaranızı girin: ")
            bilgiler = kullanici_bilgileri(kimlik_no)
            if bilgiler is None:
                print("Kimlik numaranızı yanlış ya da hatalı girdiniz.")
            else:
                print(f"{bilgiler[0]} {bilgiler[1]} lütfen bekleyiniz...")
                print("")
                print("1 - Randevulu giriş")
                print("2 - Randevusuz giriş")
                print("3 - Acil Giriş")
                print("4 - Mevcut Hastane Kapasitesi")
                secim = input("Lütfen seçiminizi yapın: ")
                if secim == "1":
                    print("1 - Poliklinik İşlemleri")
                    print("2 - Rontgen/MR kontrol")
                    if secim == "1":
                        print("1 - Anestiyoloji")
                        print("2 - Beslenme ve Diyet")
                        print("3 - Beyin ve Sinir Cerrahisi")
                        print("4 - Endoskopi")
                        print("5 - Göğüs Hastalıkları ve Alarji")
                        print("6 - Nöroloji")
                        print("7 - Psikoloji")
                        print("8 - Üroloji")
                        print("9 - Genel Cerrahi")
                        print("10 - Göz Hastalıkları")
                        print("11 - Kadın Doğum")
                        print("12 - Kulak Burun Boğaz")
                        print("13 - Ortodonti")
                        print("14 - Radyoloji")
                        print("15 - Cildiye")
                        print("16 - İç Hastalıkları(Dahiliye)")
                        print("17 - Kadın Hastalıkları")
                        print("18 - Beslenme ve Diyet")
                        print("19 - Mevcut Hastane Kapasitesini Öğren")
                        secim = input("Lütfen seçim yapın: ")
                        if secim == "1":
                            
                    elif secim == "2":
                        with open("rontgen_mr_kontrol.txt", "a", encoding="utf-8") as rontgen_mr_kontrol:
                            siradaki = sum(1 for _ in rontgen_mr_kontrol) + 1
                            rontgen_mr_kontrol.write("Sıranız: {}\n".format(kimlik_no))
                            print("Sıranız: ", siradaki)
                elif secim == "2":
                    print("1 - Aşı")
                    print("2 - Yaralanma")
                    secim = input("Lütfen seçim yapın: ")
                    if secim == "1":
                        with open("asi.txt", "a", encoding="utf-8") as asi:
                           siradaki = sum(1 for _ in asi) + 1
                           asi.write("Sıranız: {}\n".format(kimlik_no))
                           print("Sıranız: ", siradaki)
                    elif secim == "2":
                        with open("yaralanma.txt", "a", encoding="utf-8") as yaralanma:
                           siradaki = sum(1 for _ in yaralanma) + 1
                           yaralanma.write("Sıranız: {}\n".format(kimlik_no))
                           print("Sıranız: ", siradaki)
                    else:
                        print("Geçersiz seçim. Tekrar deneyiniz!")
                elif secim == "3":
                    with open("acil_giris.txt", "a", encoding="utf-8") as acil_giris:
                        siradaki = sum(1 for _ in open("acil_giris.txt", "r", encoding="utf-8")) + 1
                        acil_giris.write("{}\n".format(kimlik_no))
                        print("Sıranız: ", siradaki)
                elif secim == "4": #hastane kapasitesi tüm txt toplam satırı
                   print("Mevcut Hastane Kapasitesi: ")
                else:
                     print("Geçersiz seçim! Lütfen tekrar deneyin.")
