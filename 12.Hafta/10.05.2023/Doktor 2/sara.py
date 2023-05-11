import time
class Doktor:
    def alan_kayit(self,alan="Yok",kimlik_no="Yok"):
        kimlik_no = input("Lütfen kimlik numarasını girin: ")
        alan = input("Lütfen hastayı yönlendirmek istediginiz alanın adını giriniz.(Kırmızı/Yeşil/Sarı/Röntgen/)")
        with open("Kisi_Bilgileri.txt", "r" , encoding="utf-8") as kisi_bilgileri, open(f"{alan}_alan.txt", "a" , encoding="utf-8") as kirmizi_alan:
            kisi_bulundu = False  
            for satir in kisi_bilgileri:
                satir = satir.strip() 
                bilgiler = satir.split(",") 
                if bilgiler[0] == kimlik_no:
                    kirmizi_alan.write(satir +" ,Kayıt Tarihi : " + (time.ctime(time.time())) +"\n")
                    kisi_bulundu = True
                    break
            if not kisi_bulundu:
                print("Hatalı bir kimlik numarası girdiniz, yeni hasta ekle menüsünü kullanmaya ne dersiniz?")
    def yeni_kullanici(self):
        kimlik_no = input("Kimlik numarası girin: ")
        ad = input("Ad girin: ")
        soyad = input("Soyad girin: ")
        yas = input("Doğum Yılı girin: ")
        cinsiyet = input("Cinsiyet girin")
        oncelik_durumu = input("Oncelik durumu girin: ")
        with open("Kisi_Bilgileri.txt", 'a', encoding="utf-8") as kullaniciekle:
            kullaniciekle.write(f"{kimlik_no},{ad},{soyad},{yas},{cinsiyet},{oncelik_durumu}\n")
    def alan_kayit(self,alan="Yok",kimlik_no="Yok"):
        kimlik_no = input("Lütfen kimlik numarasını girin: ")
        alan = input("Lütfen hastayı yönlendirmek istediginiz alanın adını giriniz.(Kırmızı/Yeşil/Sarı/Röntgen/Enjeksiyon)")
        with open("Kisi_Bilgileri.txt", "r" , encoding="utf-8") as kisi_bilgileri, open(f"{alan}_alan.txt", "a" , encoding="utf-8") as kirmizi_alan:
            kisi_bulundu = False  
            for satir in kisi_bilgileri:
                satir = satir.strip() 
                bilgiler = satir.split(",") 
                if bilgiler[0] == kimlik_no:
                    kirmizi_alan.write(satir +" ,Kayıt Tarihi : " + (time.ctime(time.time())) +"\n")
                    kisi_bulundu = True
                    break
            if not kisi_bulundu:
                print("Hatalı bir kimlik numarası girdiniz, kullanıcı ekle fonksiyonunu kullanmaya ne dersiniz?")
               
    def hasta_bilgi_görüntüle(self):
        while 1:
            print("Bilgi görüntülemek için 1'e basınız.")
            print("Çıkmak için q'ya basınız.")
            secim = input("Seçiminiz: ")
            if secim =="1":
                with open(f"Kisi_Bilgileri.txt", "r" , encoding="utf-8") as file:
                    lines = file.readlines()
                search_term = input("Lütfen Bilgisini Görüntülemek İstediginiz Hastanın TC numarasını giriniz.")
                for i, line in enumerate(lines):
                    if search_term in line:
                        line_to_read = i
                        break
                print(line)
            elif secim == "q":
                break
            else:
                print("Yanlış bir seçim yaptınız lütfen tekrar deneyiniz.")
    def hasta_cıkıs(self):
        alan = input("Hangi alandan silmek istiyorsunuz? (Kırmızı/Yeşil/Sarı/Röntgen/Enjeksiyon/Acil Giriş)")
        with open(f"{alan}_alan.txt", "r" , encoding="utf-8") as file:
            lines = file.readlines()
        search_term = input("TC??")
        for i, line in enumerate(lines):
            if search_term in line:
                line_to_delete = i
                break
        del lines[line_to_delete]
        with open(f"{alan}_alan.txt", "w" , encoding="utf-8") as file:
            file.writelines(lines)
doktor1 = Doktor()
while True:
    print ("- ANA MENÜ - ")
    print("Lütfen seçim yapınız:")
    print("1- Doktor Girişi")
    print("2- Hasta Girişi")
    print("3- Çıkış")

    secim = input("Ana Menü Seçiminiz: ")

    if secim == "1":
        print("Lütfen parolanızı giriniz.")
        parola = input("Doktor parolasını girin: ")
        if parola == "1":
            print("Giriş Yapılıyor. Lütfen Bekleyiniz...")
            while True:
                print("- DOKTOR MENÜSÜ -")
                print("1 - Hasta Bilgi - İşlem")
                print("2 - Alan İşlemleri")
                print("3 - Hasta Çıkışı")
                print("4 - Ana Menüye Dönme")
                secim = input("Doktor Menüsü Seçiminiz: ")
                if secim == "1":
                        print(" - HASTA BİLGİ İŞLEM -")
                        print("1 - Yeni Hasta Ekleme: ")
                        print("2 - Mevcut Hasta Bilgi Görüntüleme: ")
                        print("3 - Ana Menüye Dönme")
                        secim = input("Hasta Bilgi İşlem Menüsü Seçiminiz: ")
                        if secim == "1":
                            doktor1.yeni_kullanici()
                        elif secim == "2":
                            doktor1.hasta_bilgi_görüntüle()
                        elif secim == "3":
                            break
                        else:
                            print("Yanlış bir seçim yaptınız lütfen tekrar deneyiniz.")
                if secim == "2":
                    print (" - ALAN İŞLEMLERİ - ")
                    print("1 - Alan Kayıt İşlemleri: ")
                    print("2 - Yeni Hasta ekle")
                    print("3 - Çıkış")
                    secim = input("Seciminiz: ")
                    if secim == "1":
                        doktor1.alan_kayit()
                    if secim == "2":
                        doktor1.yeni_kullanici()
                    if secim == "3":
                        break   
                
                if secim == "3":
                    print("- HASTA ÇIKIŞ - ")
                    print("1 - Hasta Çıkış: ")
                    print("2 - Çıkış: ")
                    secim = input("Hasta Çıkış Menüsü Seçiminiz: ")
                    if secim == "1":
                        doktor1.hasta_cıkıs()
                    if secim == "2":
                        break
                    else:
                        print("Yanlış Bir Tuşlama yaptınız lütfen tekrar deneyin.")
                if secim == "4":
                    print("Ana Menüye Yönlendiriliyorsunuz...")
                    time.sleep(0.75)
                    break
        else:
            print("Parola yanlış! Tekrar deneyin...")
    
    if secim == "2":
        filename = "Kisi_Bilgileri.txt"
        def kullanici_bilgileri(kimlik_no):
            with open(filename, 'r', encoding="utf-8") as f:
                for satir in f:
                    bilgiler = satir.strip().split(',')
                    if bilgiler[0] == kimlik_no:
                        return bilgiler[1], bilgiler[2], bilgiler[3], bilgiler[4], bilgiler[5]
            return None
        try:
            kimlik_no = input("Kimlik numaranızı giriniz: ")
            if len(kimlik_no) != 11:
                raise ValueError("Eksik ya da hatalı kimlik numarası girdiniz!")
            with open("Kisi_Bilgileri.txt", "r", encoding="utf-8") as f:
                kimlikler = [line.strip().split(",")[0] for line in f]
                if kimlik_no not in kimlikler:
                   raise ValueError("Eksik ya da hatalı kimlik numarası girdiniz!")
            bilgiler = kullanici_bilgileri(kimlik_no)
            print(f"{bilgiler[0]} {bilgiler[1]} lütfen bekleyiniz...")
            print("- HASTA ANA MENÜSÜ - ")
            print("1 - Randevulu giriş")
            print("2 - Randevusuz giriş")
            print("3 - Acil Giriş")
            print("4 - Mevcut Hastane Kapasitesi Öğren")
            secim = input("Lütfen hasta ana menüsü seçiminizi yapınız: ")
            if secim == "1":
                print("- POLİKİNLİK ANA MENÜSÜ -")
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
                secim = input("Lütfen Polikinlik seçimi yapın: ")
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
                print("- RANDEVUSUZ HASTA MENÜSÜ -")
                print("1 - Enjeksiyon Sıra Al")
                secim = input("Lütfen Randevusuz Menü seçimi yapınız: ")
                if secim == "1":
                    with open("enjeksiyon.txt", "a", encoding="utf-8") as enjeksiyon:
                        siradaki = sum(1 for _ in open("Aşı_alan.txt", "r", encoding="utf-8")) + 1
                        enjeksiyon.write("{}\n".format(kimlik_no))
                        print("Sıranız: ", siradaki)
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyin!")
            elif secim == "3":
                with open("acil_giris.txt", "a", encoding="utf-8") as acil_giris:
                    siradaki = sum(1 for _ in open("acil_giris.txt", "r", encoding="utf-8")) + 1
                    acil_giris.write("{}\n".format(kimlik_no))
                    print("Sıranız: ", siradaki)
            elif secim == "4":
               print("*" * 25)
               print("1 - Enjeksiyon mevcut hasta sayısı")
               secim = input("Hastane Kapasitesi Menüsü seçimi yapınız: ")
               if secim == "1":
                   with open("Aşı_alan.txt", "r", encoding="utf-8") as enjeksiyon:
                       sira_sayisi = len(enjeksiyon.readlines())
                       print("Mevcut hasta sayısı: ", sira_sayisi)
               else:
                   print("Geçersiz seçim. Lütfen tekrar deneyiniz!")
            else:
                 print("Geçersiz seçim. Lütfen tekrar deneyin!")
        except ValueError as e:
            print(e)
    if secim == "3":
        break