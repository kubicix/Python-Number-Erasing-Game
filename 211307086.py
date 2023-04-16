import numpy as np
import random

def sayi_yok_etme_oyunu(satirlar, sutunlar):
    #puan hesabı için recursive fibonacci 
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    #en önemli komşuları kontrol fonksiyonumuz
    def komsu_kontrol(satir_no, sutun_no, deger, sayac):
        satirlar, sutunlar = nptahta.shape
        nptahta[satir_no, sutun_no] = -1
        sayac += 1

        for i, j in [(satir_no+1, sutun_no), (satir_no-1, sutun_no), (satir_no, sutun_no+1), (satir_no, sutun_no-1)]:
            if i < 0 or i >= satirlar or j < 0 or j >= sutunlar or nptahta[i,j] != deger:
                continue
                
            nptahta[i,j] = -1
            sayac = komsu_kontrol(i, j, deger, sayac)

        # sütunları kontrol etme
        for j in range(sutunlar):
            if np.all(nptahta[:, j] == -1):
                # sütun elemanlarını kaydırma
                nptahta[:, j:sutunlar-1] = nptahta[:, j+1:]
                # en sağdaki sütunun elemanlarını -1 yapma
                nptahta[:, sutunlar-1] = -1

        return sayac

    tahta = []
    puan = 0
    # tahtayı oluşturma
    
    for i in range(satirlar):
        row = []
        for j in range(sutunlar):
            # rastgele sayılar ekleme
            row.append(random.randint(0,9))
        tahta.append(row)

    nptahta = np.array(tahta)
    
    # tahtayı girdi.txt dosyasına yazma
    
    with open("girdi.txt", "w") as f:
        for row in nptahta:
            f.write(' '.join(map(str, row)) + '\n')

    print("Matris:")
    print(nptahta)
    print("Puan: ",puan)
    while(True):
        # kullanıcının satır ve sütun seçimi
        satir_no = int(input("Hangi satırı seçmek istersiniz (1-{}): ".format(satirlar)))-1
        sutun_no = int(input("Hangi sütunu seçmek istersiniz (1-{}): ".format(sutunlar)))-1
        
        #seçilen değer satır,sğtun boyutu dışındaysa döngü tekrarlıyor
        if satir_no >= satirlar or sutun_no >= sutunlar:
            print("Lütfen geçerli bir satır ve sütun numarası giriniz.")
            continue
    
        deger = nptahta[satir_no, sutun_no]
        
        #seçilen değer önceden yok edilmişse döngü tekrarlıyor
        if deger==-1:
            print("Lütfen geçerli bir değer girin.")
            continue
        
        sayac = 0
        sayac = komsu_kontrol(satir_no, sutun_no, deger, sayac)
        if(sayac<=1):
            print("Seçtiğiniz elemanın etrafında bir komşusu yok.")
            print("Lütfen tekrar deneyin.")
            continue
        adim_puan=deger*fibonacci(sayac)
        puan+=adim_puan
        #print("{} eleman silindi.".format(sayac))
        print("Puan: ",puan)
        
        

        # silinen elemanların yerine üstündeki elemanların kaydırılması
        for i in range(satirlar-1, 0, -1):
            for j in range(sutunlar):
                if nptahta[i, j] == -1:
                    for k in range(i-1, -1, -1):
                        if nptahta[k, j] != -1:
                            nptahta[i, j], nptahta[k, j] = nptahta[k, j], nptahta[i, j]
                            break
                            
        # silinen elemanlar yerine boşluk karakteri yazdırma
        nptahta_str = np.where(nptahta == -1, ' ', nptahta.astype(str))
        for row in nptahta_str:
            row_str = ' '.join(row)
            print(row_str)
            
        # oyunun son halinin cikti.txt adlı dosyaya yazdırılması
        with open("cikti.txt", "w") as f:
            for row in nptahta_str:
                f.write(' '.join(map(str, row)) + '\n')

#parametre olarak matrisin yani oyun tahtamızın boyutunu alıyor
#6 satır / 10 sutun verdim her değere göre çalışıyor
sayi_yok_etme_oyunu(6,10)