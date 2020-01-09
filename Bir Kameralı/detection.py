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

#####################################################

##########################################################################################################
while(True):
    # URL'den Gelen Görüntüyü Okuyoruz
    _, capturedSnapshot = captureVideoFromUrl.read()

##########################################################################################################
    # Görüntünün Gelip Gelmediğine Dair Kontroller Ekliyoruz
    if capturedSnapshot is not None and capturedSnapshot2 is not None:
            # Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            _, carCountLabel, _0 = openCvLib.detect_common_objects(capturedSnapshot)

            # Araç Sayısını Konsolda Gösteriyoruz
            print("Araç Sayısı -> " + str(carCountLabel.count('car')))
            
            # Q Tuşuna Basarak Sistemi İstediğimiz Zaman Sonlandırıyoruz
            if openCv.waitKey(22) & 0xFF == ord('q'):
                break
        
    else:
        break

##########################################################################################################

captureVideoFromUrl.release()
openCv.destroyAllWindows()