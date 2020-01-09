#####################################################
#### Proje Sahibi   : Talha Can
#### Mail           : rampesna@gmail.com
#### Tarih          : 9 Aralık 2019
######################################################

#####################################################
#İlgili Kütüphaneleri Projemize Dahil Ediyoruz
import cv2 as openCv
import cvlib as openCvLib
import numpy

#####################################################
# Görüntünün Alınacağı Url Adresini Ayarlıyoruz
captureVideoFromUrl = openCv.VideoCapture('http://192.168.1.44:8081/video')
captureVideoFromUrl2 = openCv.VideoCapture('http://192.168.1.45:8081/video')

#####################################################

##########################################################################################################
while(True):
    # URL'den Gelen Görüntüleri Okuyoruz
    _01, capturedSnapshot = captureVideoFromUrl.read()
    _02, capturedSnapshot2 = captureVideoFromUrl2.read()

##########################################################################################################
    # Görüntülerin Gelip Gelmediğine Dair Kontroller Ekliyoruz
    if capturedSnapshot is not None and capturedSnapshot2 is not None:
            # Kameralardan Alınan Görüntüleri Tensorflow İle İşleyip Sayımını Yapıyoruz
            _11, carCountLabel, _21 = openCvLib.detect_common_objects(capturedSnapshot)
            _12, carCountLabel2, _22 = openCvLib.detect_common_objects(capturedSnapshot2)

            # Araç Sayılarını Konsolda Gösteriyoruz
            print("Kamera1 Araç Sayısı -> " + str(carCountLabel.count('car')) + " | " + "Kamera2 Araç Sayısı -> " + str(carCountLabel2.count('car')))
            
            # Eğer İki Tarafta'da Araç Yoksa İki Tarafa Da Kırmızı Işık Yaktırıyoruz
            if carCountLabel.count('car') == 0 and carCountLabel2.count('car') == 0:
                print("X ve Y Ekseninde Kırmızı Işık Yanıyor")
            else:
                # Araç Sayısının Fazla Olduğu Tarafa Yeşil Işık Yaktırıyoruz
                if carCountLabel.count('car') > carCountLabel2.count('car'):
                    print("X Ekseninde Yeşil Işık, Y Ekseninde Kırmızı Işık Yanıyor")
                else:
                    print("Y Ekseninde Yeşil Işık, X Ekseninde Kırmızı Işık Yanıyor")
            
            # Q Tuşuna Basarak Sistemi İstediğimiz Zaman Sonlandırıyoruz
            if openCv.waitKey(22) & 0xFF == ord('q'):
                break
        
    else:
        break

##########################################################################################################

captureVideoFromUrl.release()
captureVideoFromUrl2.release()
openCv.destroyAllWindows()