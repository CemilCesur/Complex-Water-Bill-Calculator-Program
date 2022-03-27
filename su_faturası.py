devam = "e"

abone1=0
abone2=0
abone3=0
abone4=0
abone5=0

tuketim_1_no=0
tuketim_2_no=0
tuketim_3_no=0
tuketim_4_no=0
tuketim_5_no=0

kademe1_sayisi=0
kademe2_sayisi=0
kademe3_sayisi=0

kademe1_tuketim=0
kademe2_tuketim=0
kademe3_tuketim=0

elli_den_fazla = 0

zengin_hane =0

yuz_besyuz = 0

sgs_toplam = 0
e_toplam = 0

rekor_devlet_dairesi = 0
rekor_devlet_dairesi_abone_no = 0

rekor_tum_tuketim = 0
rekor_tum_abone_no = 0
rekor_tum_ucret = 0
rekor_tum_puan = 0

toplam_konut_su = 0
toplam_isyeri_su = 0
toplam_resmi_daire_su = 0
toplam_organize_sanayi_su = 0
toplam_ilce_tarim_su = 0
tum_toplam_su = 0

toplam_konut_para = 0
toplam_isyeri_para = 0
toplam_resmi_daire_para = 0
toplam_organize_sanayi_para = 0
toplam_ilce_tarim_para = 0
toplam_para = 0

izsu_toplam_para = 0
ilce_belediye_para = 0
buyuk_sehir_belediye_para = 0
devlet_para = 0


while devam=="e" or devam=="E":

    abone_no = input("Abone no giriniz:")

    abone_tipi_kodu = int(input("1 ile 5 arası abone tipi kodunu giriniz:"))
    while 1>abone_tipi_kodu or 5<abone_tipi_kodu:
        abone_tipi_kodu = int(input("Yanlış değer girdiniz, 1 ile 5 arası abone tipi kodunu tekrar giriniz:"))

    if abone_tipi_kodu == 1:

        hane_sayisi = int(input("Hane sayısını giriniz:"))
        abone1 += hane_sayisi

        while hane_sayisi < 1:
            hane_sayisi = int(input("Yanlış değer girdiniz, hane sayısını 1 yada 1'den büyük olarak giriniz:"))

        toplam_ucret = 0
        toplam_1 = 0
        toplam_2 = 0
        kademe1su = 2.89
        kademe1atik = 1.44
        kademe2su = 3.13
        kademe2atik = 1.56
        kademe3su = 6.43
        kademe3atik = 3.22

        if hane_sayisi == 1:
            print("İndirim durumu kısaltmaları;")
            print("Yok = Y/y")
            print("Şehit = Ş/ş")
            print("Gazi = G/g")
            print("Sporcu = S/s")
            print("Engelli = E/e")
            indirim_durumu = input("İndirim durumunu kısaltma olarak giriniz:")
            while indirim_durumu not in ["Y", "y", "Ş", "ş", "G", "g", "S", "s", "E", "e"]:
                indirim_durumu = input(
                    "Yanlış kısaltma girdiniz, indirim durumunu belirtilen kısaltmalardan giriniz:")

            onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
            while 0 > onceki_sayac:
                onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

            simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
            while simdiki_sayac < onceki_sayac:
                simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

            sayac_gunu = int(input("Sayaç gününü giriniz:"))
            while sayac_gunu <= 0:
                sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))

            if indirim_durumu in ["Ş", "ş", "G", "g", "S", "s"]:

                sgs_toplam += 1

                kademe1su = 2.89 * (1 / 2)
                kademe1atik = 1.44 * (1 / 2)
                kademe2su = 3.13 * (1 / 2)
                kademe2atik = 1.56 * (1 / 2)
                kademe3su = 6.43 * (1 / 2)
                kademe3atik = 3.22 * (1 / 2)

            elif indirim_durumu in ["E", "e"]:

                e_toplam += 1

                kademe1su = 2.89 * (1 / 2)
                kademe1atik = 1.44 * (1 / 2)
                kademe2su = 3.13 * (1 / 2)
                kademe2atik = 1.56 * (1 / 2)

            tuketim = (simdiki_sayac - onceki_sayac)

            if tuketim <= 13 * sayac_gunu / 30:
                ucret1 = tuketim * kademe1su
                ucret2 = tuketim * kademe1atik

                kademe1_sayisi += 1
                kademe1_tuketim += tuketim

            elif tuketim <= (20 * sayac_gunu / 30) and tuketim > (13 * sayac_gunu / 30):

                ucret1 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su)
                ucret2 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik)

                kademe1_sayisi += 1
                kademe2_sayisi += 1

                kademe1_tuketim += 13 * sayac_gunu / 30
                kademe2_tuketim += tuketim - 13 * sayac_gunu / 30

            elif tuketim > 20 * sayac_gunu / 30:
                tuketim2 = tuketim - (20 * sayac_gunu / 30)
                ucret1 = ((tuketim2 * kademe3su) + (7 * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su))
                ucret2 = ((tuketim2 * kademe3atik) + (7 * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik))

                kademe1_sayisi += 1
                kademe2_sayisi += 1
                kademe3_sayisi += 1

                kademe1_tuketim += 13 * sayac_gunu / 30
                kademe2_tuketim += 7
                kademe3_tuketim += tuketim - 20 * sayac_gunu / 30

            toplam_ucret += ucret1 + ucret2
            toplam_1 += ucret1
            toplam_2 += ucret2
            if tuketim > 100 or toplam_ucret > 500:
                zengin_hane += 1


        elif hane_sayisi>1:
            sehit_gazi_sporcu = int(input("Şehit, gazi veya sporcu sayısını giriniz:"))
            while not 0<=sehit_gazi_sporcu<=hane_sayisi:
                sehit_gazi_sporcu = int(input("Yanlış değer girdiniz. Şehit, gazi veya sporcu sayısını 0 ve hane sayısı arasında bir değer giriniz:"))
            sgs_toplam += sehit_gazi_sporcu

            engelli = int(input("Engelli sayısını giriniz:"))
            while not 0<= engelli <=hane_sayisi:
                engelli = int(input("Yanlış değer  girdiniz. Engelli sayısını 0 ve hane sayısı arasında bir değer giriniz:"))
            e_toplam += engelli

            toplam_engel = sehit_gazi_sporcu + engelli
            while toplam_engel>hane_sayisi:
                print("Yanlış değerler girilmiş, indirim durumlarını tekrar giriniz.")
                sehit_gazi_sporcu = int(input("Şehit, gazi veya sporcu sayısını giriniz:"))
                while not 0 <= sehit_gazi_sporcu <= hane_sayisi:
                    sehit_gazi_sporcu = int(input("Yanlış değer girdiniz. Şehit, gazi veya sporcu sayısını 0 ve hane sayısı arasında bir değer giriniz:"))

                engelli = int(input("Engelli sayısını giriniz:"))
                while not 0 <= engelli <= hane_sayisi:
                    engelli = int(input("Yanlış değer  girdiniz. Engelli sayısını 0 ve hane sayısı arasında bir değer giriniz:"))

                toplam_engel = sehit_gazi_sporcu + engelli

            onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
            while 0>onceki_sayac:
                  onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

            simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
            while simdiki_sayac<onceki_sayac:
                  simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

            sayac_gunu = int(input("Sayaç gününü giriniz:"))
            while sayac_gunu<=0:
                  sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))

            toplam_ucret=0
            toplam_1=0
            toplam_2=0


            for i in range(engelli):

               kademe1su = 2.89 * (1/2)
               kademe1atik = 1.44 * (1/2)
               kademe2su = 3.13 * (1/2)
               kademe2atik = 1.56 * (1/2)

               tuketim = (simdiki_sayac - onceki_sayac)/hane_sayisi

               if tuketim<=13 * sayac_gunu / 30:
                  ucret1 = tuketim * kademe1su
                  ucret2 = tuketim * kademe1atik

                  kademe1_sayisi += 1

                  kademe1_tuketim += tuketim


               elif tuketim<=20 * sayac_gunu / 30 and tuketim>13 * sayac_gunu / 30:
                    ucret1 = ((tuketim-(13 * sayac_gunu / 30))*kademe2su) + ((13 * sayac_gunu / 30)*kademe1su)
                    ucret2 = ((tuketim-(13 * sayac_gunu / 30))*kademe2atik) + ((13 * sayac_gunu / 30)*kademe1atik)

                    kademe1_sayisi += 1
                    kademe2_sayisi += 1

                    kademe1_tuketim += 13*sayac_gunu/30
                    kademe2_tuketim += tuketim - 13*sayac_gunu/30


               elif tuketim>20 * sayac_gunu  / 30:
                    tuketim2=tuketim- (20 * sayac_gunu / 30)
                    ucret1 = ((tuketim2*kademe3su) + (7*kademe2su) + ((13 * sayac_gunu / 30)*kademe1su))
                    ucret2 = ((tuketim2 * kademe3atik) + (7 * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik))

                    kademe1_sayisi += 1
                    kademe2_sayisi += 1
                    kademe3_sayisi += 1

                    kademe1_tuketim += 13*sayac_gunu/30
                    kademe2_tuketim += 7
                    kademe3_tuketim += tuketim - 20*sayac_gunu/30



               toplam_ucret += ucret1+ucret2
               toplam_1 += ucret1
               toplam_2 += ucret2
               if tuketim > 100 or toplam_ucret > 500:
                   zengin_hane += 1


            for i in range(sehit_gazi_sporcu):

                 kademe1su = 2.89 * (1 / 2)
                 kademe1atik = 1.44 * (1 / 2)
                 kademe2su = 3.13 * (1 / 2)
                 kademe2atik = 1.56 * (1 / 2)
                 kademe3su = 6.43 * (1 / 2)
                 kademe3atik = 3.22 * (1 / 2)

                 tuketim = (simdiki_sayac - onceki_sayac) / hane_sayisi

                 if tuketim <= 13 * sayac_gunu / 30:
                    ucret1 = tuketim * kademe1su
                    ucret2 = tuketim * kademe1atik

                    kademe1_sayisi += 1

                    kademe1_tuketim += tuketim


                 elif tuketim <= 20 * sayac_gunu / 30 and tuketim > 13 * sayac_gunu / 30:
                      ucret1 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su)
                      ucret2 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik)

                      kademe1_sayisi += 1
                      kademe2_sayisi += 1

                      kademe1_tuketim += 13*sayac_gunu/30
                      kademe2_tuketim += tuketim - 13*sayac_gunu/30


                 elif tuketim > 20 * sayac_gunu / 30:
                      tuketim2 = tuketim - (20 * sayac_gunu / 30)
                      ucret1 = ((tuketim2 * kademe3su) + (7 * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su))
                      ucret2 = ((tuketim2 * kademe3atik) + (7 * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik))

                      kademe1_sayisi += 1
                      kademe2_sayisi += 1
                      kademe3_sayisi += 1

                      kademe1_tuketim += 13*sayac_gunu/30
                      kademe2_tuketim += 7
                      kademe3_tuketim += tuketim - 20*sayac_gunu/30

                 toplam_ucret += ucret1 + ucret2
                 toplam_1 += ucret1
                 toplam_2 += ucret2
            if tuketim > 100 or toplam_ucret > 500:
                zengin_hane += 1

            for i in range(hane_sayisi-sehit_gazi_sporcu-engelli):
               kademe1su = 2.89
               kademe1atik = 1.44
               kademe2su = 3.13
               kademe2atik = 1.56
               kademe3su = 6.43
               kademe3atik = 3.22

               tuketim = (simdiki_sayac - onceki_sayac) / hane_sayisi

               if tuketim <= 13 * sayac_gunu / 30:
                  ucret1 = tuketim * kademe1su
                  ucret2 = tuketim * kademe1atik

                  kademe1_sayisi += 1

                  kademe1_tuketim += tuketim

               elif tuketim <= 20 * sayac_gunu / 30 and tuketim >13 * sayac_gunu / 30:
                    ucret1 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su)
                    ucret2 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik)

                    kademe1_sayisi += 1
                    kademe2_sayisi += 1

                    kademe1_tuketim += 13*sayac_gunu/30
                    kademe2_tuketim += tuketim - 13*sayac_gunu/30


               elif tuketim > 20 * sayac_gunu / 30:
                    tuketim2 = tuketim - (20 * sayac_gunu / 30)
                    ucret1 = ((tuketim2 * kademe3su) + (7 * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su))
                    ucret2 = ((tuketim2 * kademe3atik) + (7 * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik))

                    kademe1_sayisi += 1
                    kademe2_sayisi += 1
                    kademe3_sayisi += 1

                    kademe1_tuketim += 13*sayac_gunu/30
                    kademe2_tuketim += 7
                    kademe3_tuketim += tuketim - 20*sayac_gunu/30

               toplam_ucret += ucret1 + ucret2
               toplam_1 += ucret1
               toplam_2 += ucret2
               if tuketim > 100 or toplam_ucret > 500:
                   zengin_hane += 1


        print("Abone no =", abone_no)
        print("Abone tipi adı = 1-Konut")
        print("Dönemlik su tüketim miktarı =", tuketim*hane_sayisi)
        print("Dönemlik su tüketim ücreti =", format(toplam_1, ".2f"))
        print("Dönemlik atık su ücreti =", format(toplam_2, ".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücreti =", format(toplam_ucret, ".2f"))
        ctv = (simdiki_sayac-onceki_sayac)*0.39
        print("Dönemlik ÇTV tutarı =", format(ctv, ".2f"))
        kati_atik = hane_sayisi*13
        print("Dönemlik katı atık toplama ücret =", kati_atik)
        kati_atik_bertaraf = hane_sayisi*2.54
        print("Dönemlik katı atık bertaraf ücreti =", kati_atik_bertaraf)
        kdv = (toplam_ucret+kati_atik+kati_atik_bertaraf)*0.08
        print("Dönemlik toplam fatura tutarı =", format(toplam_ucret + kdv + ctv + kati_atik_bertaraf + kati_atik, ".2f"))
        print("Dönemlik devlete aktarılacak KDV tutarı =", format(kdv, ".2f"))
        print("Dönemlik ilçe belediyesine aktarılacak tutar =", format(ctv + kati_atik, ".2f"))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar =", kati_atik_bertaraf)
        print("Dönemlik İZSU payı =", format(toplam_ucret, ".2f"))
        tuketim_1_no += (simdiki_sayac - onceki_sayac)
        toplam_konut_para += toplam_1
        toplam_para += toplam_1
        toplam_konut_su += tuketim
        tum_toplam_su += tuketim
        izsu_toplam_para += toplam_ucret
        ilce_belediye_para += ctv+kati_atik
        buyuk_sehir_belediye_para += kati_atik_bertaraf
        devlet_para += kdv

    if abone_tipi_kodu==2:
        abone2 += 1
        toplam_ucret = 0
        toplam_1 = 0
        toplam_2 = 0
        su = 7.38
        atik = 3.68
        onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
        while 0 > onceki_sayac:
            onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

        simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
        while simdiki_sayac < onceki_sayac:
            simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

        sayac_gunu = int(input("Sayaç gününü giriniz:"))
        while sayac_gunu <= 0:
            sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))
        tuketim = (simdiki_sayac - onceki_sayac)
        toplam_1 = su*tuketim
        toplam_2 = atik*tuketim
        toplam_ucret= toplam_1+toplam_2
        print("Abone no =", abone_no)
        print("Abone tipi adı = 2-İşyeri")
        print("Dönemlik su tüketim miktarı =", tuketim)
        print("Dönemlik su tüketim ücreti =", format(toplam_1, ".2f"))
        print("Dönemlik atık su ücreti =", format(toplam_2, ".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücreti =", format(toplam_ucret, ".2f"))
        ctv = (simdiki_sayac - onceki_sayac) * 0.39
        print("Dönemlik ÇTV tutarı =", format(ctv, ".2f"))
        kati_atik =  13
        print("Dönemlik katı atık toplama ücret =", kati_atik)
        kati_atik_bertaraf =  2.54
        print("Dönemlik katı atık bertaraf ücreti =", kati_atik_bertaraf)
        kdv = (toplam_ucret + kati_atik + kati_atik_bertaraf) * 0.08
        print("Dönemlik toplam fatura tutarı =", format(toplam_ucret + kdv + ctv + kati_atik_bertaraf + kati_atik, ".2f"))
        print("Dönemlik devlete aktarılacak KDV tutarı =", format(kdv, ".2f"))
        print("Dönemlik ilçe belediyesine aktarılacak tutar =", format(ctv + kati_atik, ".2f"))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar =", kati_atik_bertaraf)
        print("Dönemlik İZSU payı =", format(toplam_ucret, ".2f"))
        tuketim_2_no += (simdiki_sayac - onceki_sayac)
        if tuketim>100 or toplam_ucret>500:
            yuz_besyuz += 1
        if rekor_tum_ucret<toplam_ucret:
            rekor_tum_abone_no = abone_no
            rekor_tum_tuketim = tuketim
            rekor_tum_ucret = toplam_ucret
            rekor_tum_puan = 2
        toplam_isyeri_para += toplam_1
        toplam_para += toplam_1
        toplam_isyeri_su += tuketim
        tum_toplam_su += tuketim
        izsu_toplam_para += toplam_ucret
        ilce_belediye_para += ctv + kati_atik
        buyuk_sehir_belediye_para += kati_atik_bertaraf
        devlet_para += kdv

    if abone_tipi_kodu==3:

        abone3 += 1
        toplam_ucret = 0
        toplam_1 = 0
        toplam_2 = 0
        su = 4.34
        atik = 2.16
        onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
        while 0 > onceki_sayac:
            onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

        simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
        while simdiki_sayac < onceki_sayac:
            simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

        sayac_gunu = int(input("Sayaç gününü giriniz:"))
        while sayac_gunu <= 0:
            sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))
        tuketim = (simdiki_sayac - onceki_sayac)
        toplam_1 = su*tuketim
        toplam_2 = atik*tuketim
        toplam_ucret = toplam_1 + toplam_2
        print("Abone no =", abone_no)
        print("Abone tipi adı = 3-Resmi Daire")
        print("Dönemlik su tüketim miktarı =", tuketim)
        print("Dönemlik su tüketim ücreti =", format(toplam_1, ".2f"))
        print("Dönemlik atık su ücreti =", format(toplam_2, ".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücreti =", format(toplam_ucret, ".2f"))
        ctv = (simdiki_sayac - onceki_sayac) * 0.39
        print("Dönemlik ÇTV tutarı =", format(ctv, ".2f"))
        kati_atik = 13
        print("Dönemlik katı atık toplama ücret =", kati_atik)
        kati_atik_bertaraf = 2.54
        print("Dönemlik katı atık bertaraf ücreti =", kati_atik_bertaraf)
        kdv = (toplam_ucret + kati_atik + kati_atik_bertaraf) * 0.08
        print("Dönemlik toplam fatura tutarı =", format(toplam_ucret + kdv + ctv + kati_atik_bertaraf + kati_atik, ".2f"))
        print("Dönemlik devlete aktarılacak KDV tutarı =",format(kdv, ".2f"))
        print("Dönemlik ilçe belediyesine aktarılacak tutar =", format(ctv + kati_atik, ".2f"))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar =", kati_atik_bertaraf)
        print("Dönemlik İZSU payı =", format(toplam_ucret, ".2f"))
        tuketim_3_no += (simdiki_sayac - onceki_sayac)
        if tuketim>100 or toplam_ucret>500:
            yuz_besyuz += 1
        if tuketim > rekor_devlet_dairesi:
            rekor_devlet_dairesi = tuketim
            rekor_devlet_dairesi_abone_no = abone_no
        if rekor_tum_ucret<toplam_ucret:
            rekor_tum_abone_no = abone_no
            rekor_tum_tuketim = tuketim
            rekor_tum_ucret = toplam_ucret
            rekor_tum_puan = 3
        toplam_resmi_daire_para += toplam_1
        toplam_para += toplam_1
        toplam_resmi_daire_su += tuketim
        tum_toplam_su += tuketim
        izsu_toplam_para += toplam_ucret
        ilce_belediye_para += ctv + kati_atik
        buyuk_sehir_belediye_para += kati_atik_bertaraf
        devlet_para += kdv

    if abone_tipi_kodu==4:
        abone4 += 1
        toplam_ucret = 0
        toplam_1 = 0
        toplam_2 = 0
        su =5
        atik =2.5
        onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
        while 0 > onceki_sayac:
            onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

        simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
        while simdiki_sayac < onceki_sayac:
            simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

        sayac_gunu = int(input("Sayaç gününü giriniz:"))
        while sayac_gunu <= 0:
            sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))
        tuketim = (simdiki_sayac - onceki_sayac)
        toplam_1 = su*tuketim
        toplam_2 = atik*tuketim
        toplam_ucret = toplam_2 + toplam_1
        print("Abone no =", abone_no)
        print("Abone tipi adı = 4-Organize Sanayi")
        print("Dönemlik su tüketim miktarı =", tuketim)
        print("Dönemlik su tüketim ücreti =", format(toplam_1, ".2f"))
        print("Dönemlik atık su ücreti =", format(toplam_2, ".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücreti =", format(toplam_ucret, ".2f"))
        ctv = (simdiki_sayac - onceki_sayac) * 0.39
        print("Dönemlik ÇTV tutarı =", format(ctv, ".2f"))
        kati_atik =  13
        print("Dönemlik katı atık toplama ücret =", kati_atik)
        kati_atik_bertaraf = 2.54
        print("Dönemlik katı atık bertaraf ücreti =", kati_atik_bertaraf)
        kdv = (toplam_ucret + kati_atik + kati_atik_bertaraf) * 0.08
        print("Dönemlik toplam fatura tutarı =", format(toplam_ucret + kdv + ctv + kati_atik_bertaraf + kati_atik, ".2f"))
        print("Dönemlik devlete aktarılacak KDV tutarı =", format(kdv, ".2f"))
        print("Dönemlik ilçe belediyesine aktarılacak tutar =", format(ctv + kati_atik, ".2f"))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar =", kati_atik_bertaraf)
        print("Dönemlik İZSU payı =", format(toplam_ucret, ".2f"))
        tuketim_4_no += (simdiki_sayac - onceki_sayac)
        if tuketim>100 or toplam_ucret>500:
            yuz_besyuz += 1
        if rekor_tum_ucret<toplam_ucret:
            rekor_tum_abone_no = abone_no
            rekor_tum_tuketim = tuketim
            rekor_tum_ucret = toplam_ucret
            rekor_tum_puan = 4
        toplam_organize_sanayi_para += toplam_1
        toplam_para += toplam_1
        toplam_organize_sanayi_su += tuketim
        tum_toplam_su += tuketim
        izsu_toplam_para += toplam_ucret
        ilce_belediye_para += ctv + kati_atik
        buyuk_sehir_belediye_para += kati_atik_bertaraf
        devlet_para += kdv

    if abone_tipi_kodu==5:
        abone5 += 1
        toplam_ucret = 0
        toplam_1 = 0
        toplam_2 = 0
        kademe1su = 1.45
        kademe1atik = 0.72
        kademe2su = 2.89
        kademe2atik = 1.44
        kademe3su = 6.43
        kademe3atik = 3.22

        onceki_sayac = int(input("Önceki sayaç değerini giriniz:"))
        while 0 > onceki_sayac:
            onceki_sayac = int(input("Önceki sayaç değerini 0 veya 0'dan büyük olarak giriniz:"))

        simdiki_sayac = int(input("Şimdiki sayaç değerini giriniz:"))
        while simdiki_sayac < onceki_sayac:
             simdiki_sayac = int(input("Yanlış değer girdiniz, şimdiki sayaç değerini doğru giriniz:"))

        sayac_gunu = int(input("Sayaç gününü giriniz:"))
        while sayac_gunu <= 0:
            sayac_gunu = int(input("Yanlış değer girdiniz, sayaç gününü 0'dan büyük giriniz:"))
        tuketim = (simdiki_sayac-onceki_sayac)
        if tuketim>50:
            elli_den_fazla +=1
        if tuketim <= 13 * sayac_gunu / 30:
            ucret1 = tuketim * kademe1su
            ucret2 = tuketim * kademe1atik

        elif tuketim <= 20 * sayac_gunu / 30 and tuketim > 13 * sayac_gunu / 30:
            ucret1 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su)
            ucret2 = ((tuketim - (13 * sayac_gunu / 30)) * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik)

        elif tuketim > 20 * sayac_gunu / 30:
            tuketim2 = tuketim - (20 * sayac_gunu / 30)
            ucret1 = ((tuketim2 * kademe3su) + (7 * kademe2su) + ((13 * sayac_gunu / 30) * kademe1su))
            ucret2 = ((tuketim2 * kademe3atik) + (7 * kademe2atik) + ((13 * sayac_gunu / 30) * kademe1atik))

        toplam_ucret += ucret1 + ucret2
        toplam_1 += ucret1
        toplam_2 += ucret2
        print("Abone no =", abone_no)
        print("Abone tipi adı = 5-İlçe Tarımsal ve Hayvan Sulama")
        print("Dönemlik su tüketim miktarı =", tuketim)
        print("Dönemlik su tüketim ücreti =", format(toplam_1, ".2f"))
        print("Dönemlik atık su ücreti =", format(toplam_2, ".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücreti =", format(toplam_ucret, ".2f"))
        ctv = (simdiki_sayac - onceki_sayac) * 0.39
        print("Dönemlik ÇTV tutarı =", format(ctv, ".2f"))
        kati_atik = 13
        print("Dönemlik katı atık toplama ücret =", kati_atik)
        kati_atik_bertaraf = 2.54
        print("Dönemlik katı atık bertaraf ücreti =", kati_atik_bertaraf)
        kdv = (toplam_ucret + kati_atik + kati_atik_bertaraf) * 0.08
        print("Dönemlik toplam fatura tutarı =", format(toplam_ucret + kdv + ctv + kati_atik_bertaraf + kati_atik, ".2f"))
        print("Dönemlik devlete aktarılacak KDV tutarı =", format(kdv, ".2f"))
        print("Dönemlik ilçe belediyesine aktarılacak tutar =", format(ctv + kati_atik, ".2f"))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar =", kati_atik_bertaraf)
        print("Dönemlik İZSU payı =", format(toplam_ucret, ".2f"))
        tuketim_5_no += (simdiki_sayac - onceki_sayac)
        if tuketim>100 or toplam_ucret>500:
            yuz_besyuz += 1
        if rekor_tum_ucret<toplam_ucret:
            rekor_tum_abone_no = abone_no
            rekor_tum_tuketim = tuketim
            rekor_tum_ucret = toplam_ucret
            rekor_tum_puan = 5
        toplam_ilce_tarim_para += toplam_1
        toplam_para += toplam_1
        toplam_ilce_tarim_su += tuketim
        tum_toplam_su += tuketim
        izsu_toplam_para += toplam_ucret
        ilce_belediye_para += ctv + kati_atik
        buyuk_sehir_belediye_para += kati_atik_bertaraf
        devlet_para += kdv



    devam = input("Başka abone var mı? (e/E/h/H karakterleri):")
    while devam not in ["e","E","h","H"]:
        devam = input(" Hatalı giriş! Başka abone var mı? (e/E/h/H karakterleri):")

yuz_besyuz += zengin_hane

if rekor_tum_puan==2:
    rekor_tum_adi = "İşyeri"
elif rekor_tum_puan==3:
    rekor_tum_adi = "Resmi Daire"
elif rekor_tum_puan==4:
    rekor_tum_adi = "Organize Sanayi"
elif rekor_tum_puan==5:
    rekor_tum_adi = "Tarımsal ve Hayvan Sulama"


if abone1 > 0:
    print("1-Konut tipi abone(hane) sayısı =", abone1)
    print("1-Konut tipi abone(hane) yüzdesi = %", format((abone1*100)/(abone1+abone2+abone3+abone4+abone5),'.0f'))
    print("1-Konut tipi abonenin(hane) aylık ortalama su tüketim miktarı =", format(tuketim_1_no/30,'.2f'))
    print("1-Konut tipine ait kademe 1'deki abone(hane) sayısı =", kademe1_sayisi)
    print("1-Konut tipine ait kademe 2'deki abone(hane) sayısı =", kademe2_sayisi)
    print("1-Konut tipine ait kademe 3'deki abone(hane) sayısı =", kademe3_sayisi)
    print("1-Konut tipine ait kademe 1'deki abonelerin(hane) yüzdesi = %", format(kademe1_sayisi * 100/ abone1,'.0f'))
    print("1-Konut tipine ait kademe 2'deki abonelerin(hane) yüzdesi = %", format(kademe2_sayisi * 100 / abone1,'.0f'))
    print("1-Konut tipine ait kademe 3'deki abonelerin(hane) yüzdesi = %", format(kademe3_sayisi * 100 / abone1,'.0f'))
    print("1-Konut tipine ait kademe 1'deki abonelerin(hane) aylık ortalama su tüketim miktarı =",  format(kademe1_tuketim / 30,'.2f'))
    print("1-Konut tipine ait kademe 2'deki abonelerin(hane) aylık ortalama su tüketim miktarı =", format(kademe2_tuketim / 30,'.2f'))
    print("1-Konut tipine ait kademe 3'deki abonelerin(hane) aylık ortalama su tüketim miktarı =", format(kademe3_tuketim / 30,'.2f'))




if abone2 > 0:
    print("2-İşyeri tipi abone sayısı =", abone2)
    print("2-İşyeri tipi abone yüzdesi = %", format((abone2*100)/(abone1+abone2+abone3+abone4+abone5),'.0f'))
    print("2-İşyeri tipi abonenin aylık ortalama su tüketim miktarı =", format(tuketim_2_no/30,'.2f'))



if abone3 > 0:
    print("3-Resmi Daire tipi abone sayısı =", abone3)
    print("3-Resmi Daire abone yüzdesi = %", format((abone3*100)/(abone1+abone2+abone3+abone4+abone5),'.0f'))
    print("3-Resmi Daire abonenin aylık ortalama su tüketim miktarı =", format(tuketim_3_no/30,'.2f'))



if abone4 > 0:
    print("4-Organize Sanayi tipi abone sayısı =", abone4)
    print("4-Organize Sanayi tipi abone yüzdesi = %", format((abone4*100)/(abone1+abone2+abone3+abone4+abone5),'.0f'))
    print("4-Organize Sanayi tipi abonenin aylık ortalama su tüketim miktarı =", format(tuketim_4_no/30,'.2f'))



if abone5 > 0:
    print("5-İlçe Tarımsal ve Hayvan Sulama tipi abone sayısı =", abone5)
    print("5-İlçe Tarımsal ve Hayvan Sulama tipi abone yüzdesi = %", format((abone5*100)/(abone1+abone2+abone3+abone4+abone5),'.0f'))
    print("5-İlçe Tarımsal ve Hayvan Sulama tipi abonenin aylık ortalama su tüketim miktarı =", format(tuketim_5_no/30,'.2f'))
    print("5-İlçe Tarımsal ve Hayvan Sulama tipi abonenin aylık su tüketim miktarı 50 tondan fazla olan abone sayısı =", elli_den_fazla)
    print("5-İlçe Tarımsal ve Hayvan Sulama tipi abonenin aylık su tüketim miktarı 50 tondan fazla olan abonelerin yüzdesi = %", format(elli_den_fazla*100/abone5,'.0f'))

print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı =", yuz_besyuz)

if abone1 > 0:
    print("Şehit, gazi veya devlet sporcusu olan konut tipi abonelerin (hanelerin) sayısı =", sgs_toplam)
    print("Engelli olan konut tipi abonelerin (hanelerin) sayısı =", e_toplam)
    print("Şehit, gazi veya devlet sporcusu olan konut tipi abonelerin (hanelerin) yüzdeleri = %", format(sgs_toplam*100/abone1,'.0f'))
    print("Engelli olan konut tipi abonelerin (hanelerin) yüzdesi = %", format(e_toplam*100/abone1,'.0f'))


if abone3 > 0:
    print("3-Resmi daire tipli aylık su tüketim miktarı en yüksek olan abonenin abone no’su =", rekor_devlet_dairesi_abone_no)
    print("3-Resmi daire tipli aylık su tüketim miktarı en yüksek olan abonenin aylık su tüketim miktarı =", format(rekor_devlet_dairesi,'.2f'))


if abone2>0 or abone3>0 or abone4>0 or abone5>0:
    print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su =", rekor_tum_abone_no)
    print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin tip adı =", rekor_tum_adi)
    print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin aylık su tüketim miktarı =", format(rekor_tum_tuketim,'.2f'))
    print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin su tüketim ücreti =", format(rekor_tum_ucret,'.2f'))


if abone1>0:
    print("1-Konut tipine ait  abonelerin(hane) aylık toplam su tüketim miktarı =", format(toplam_konut_su,'.2f'))
    print("1-Konut tipine ait  abonelerin(hane) Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi = %", format(toplam_konut_su*100/tum_toplam_su,'.0f'))
if abone2>0:
    print("2-İsyeri tipine ait  abonelerin aylık toplam su tüketim miktarı =", format(toplam_isyeri_su,'.2f'))
    print("2-İsyeri tipine ait  abonelerin Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi = %", format(toplam_isyeri_su*100/tum_toplam_su,'.0f'))
if abone3>0:
    print("3-Resmi Daire tipine ait  abonelerin aylık toplam su tüketim miktarı=", format(toplam_resmi_daire_su,'.2f'))
    print("3-Resmi Daire tipine ait  abonelerin Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi = %", format(toplam_resmi_daire_su*100/tum_toplam_su,'.0f'))
if abone4>0:
    print("4-Organize Sanayi tipine ait  abonelerin aylık toplam su tüketim miktarı=", format(toplam_organize_sanayi_su,'.2f'))
    print("4-Organize Sanayi tipine ait  abonelerin Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi = %", format(toplam_organize_sanayi_su*100/tum_toplam_su,'.0f'))
if abone5>0:
    print("5-İlce Tarımsal ve Hayvan Sulama tipine ait  abonelerin aylık toplam su tüketim miktarı=", format(toplam_ilce_tarim_su,'.2f'))
    print("5-İlce Tarımsal ve Hayvan Sulama tipine ait  abonelerin Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi = %", format(toplam_ilce_tarim_su*100/tum_toplam_su,'.0f'))
print("Bornova’nın aylık toplam su tüketim miktarı =", format(tum_toplam_su,'.2f'))

if abone1>0:
    print("1-Konut tipine ait  abonelerin(hane) aylık toplam su tüketim ücreti  =", format(toplam_konut_para,'.2f'))
if abone2>0:
    print("2-İsyeri tipine ait  abonelerin aylık toplam su tüketim ücreti  =",format(toplam_isyeri_para,'.2f'))
if abone3>0:
    print("3-Resmi Daire ait  abonelerin aylık toplam su tüketim ücreti  =",format(toplam_resmi_daire_para,'.2f'))
if abone4>0:
    print("4-Organize Sanayi tipine ait  abonelerin aylık toplam su tüketim ücreti  =",format(toplam_organize_sanayi_para,'.2f'))
if abone5>0:
    print("5-İlce Tarımsal ve Hayvan Sulama tipine ait  abonelerin aylık toplam su tüketim ücreti  =",format(toplam_ilce_tarim_para,'.2f'))
print("Tüm abonelerden elde edilen aylık toplam su tüketim ücreti =",format(toplam_para,'.2f'))

print("İlgili dönemde su faturalarından İZSU’nun elde ettiği gelir tutarı =", format(izsu_toplam_para,'.2f'))
print("İlgili dönemde su faturalarından ilçe belediyesinin elde ettiği gelir tutarı =", format(ilce_belediye_para,'.2f'))
print("İlgili dönemde su faturalarından büyükşehir belediyesinin elde ettiği gelir tutarı =", format(buyuk_sehir_belediye_para,'.2f'))
print("İlgili dönemde su faturalarından devletin elde ettiği gelir tutarı =", format(devlet_para,'.2f'))