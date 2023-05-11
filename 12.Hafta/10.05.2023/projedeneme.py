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
                print("4 - Mevcut Hastane Kapasitesi Öğren")
                secim = input("Lütfen seçiminizi yapın: ")
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
                    secim = input("Lütfen seçim yapın: ")
                    if secim == "1":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "2":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "3":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "4":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "5":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "6":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "7":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "8":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "9":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "10":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "11":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "12":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "13":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "14":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "15":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "16":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "17":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz.")
                    if secim == "18":
                        print("Kaydınız gerçekleşti. Randevu saatinizde doktorunuzun odasına girebilirsiniz. ")
                elif secim == "2":
                    print("1 - Enjeksiyon")
                    secim = input("Lütfen seçim yapın: ")
                    if secim == "1":
                        with open("enjeksiyon.txt", "a", encoding="utf-8") as enjeksiyon:
                            siradaki = sum(1 for _ in open("enjeksiyon.txt", "r", encoding="utf-8")) + 1
                            enjeksiyon.write("{}\n".format(kimlik_no))
                            print("Sıranız: ", siradaki)
                    else:
                        print("Geçersiz seçim. Lütfen tekrar deneyin!")
                elif secim == "3":
                    with open("acil_giris.txt", "a", encoding="utf-8") as acil_giris:
                        siradaki = sum(1 for _ in open("acil_giris.txt", "r", encoding="utf-8")) + 1
                        acil_giris.write("{}\n".format(kimlik_no))
                        print("Sıranız: ", siradaki)
                elif secim == "4": #hastane kapasitesi tüm txt toplam satırı
                   print("1 - Enjeksiyon mevcut hasta sayısı")
                   secim = input("Lütfen seçim yapın.")
                   if secim == "1":
                       with open("enjeksiyon.txt", "r", encoding="utf-8") as enjeksiyon:
                           sira_sayisi = len(enjeksiyon.readlines())
                           print("Mevcut hasta sayısı: ", sira_sayisi)
                   else:
                       print("Geçersiz seçim. Lütfen tekrar deneyiniz!")
                else:
                     print("Geçersiz seçim. Lütfen tekrar deneyin!")
