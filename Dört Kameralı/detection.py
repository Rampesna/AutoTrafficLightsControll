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

#####################################################
# Değişkenleri Tanımlıyoruz
totalCarAxisX = 0
totalCarAxisY = 0
xAxisLight = 0
yAxisLight = 0
#####################################################

#####################################################
# Görüntülerin Alınacağı Url Adreslerini Ayarlıyoruz
captureVideoFromUrlAxisX1 = openCv.VideoCapture('http://192.168.1.41:8081/video')
captureVideoFromUrlAxisX2 = openCv.VideoCapture('http://192.168.1.42:8081/video')

captureVideoFromUrlAxisY1 = openCv.VideoCapture('http://192.168.1.43:8081/video')
captureVideoFromUrlAxisY2 = openCv.VideoCapture('http://192.168.1.44:8081/video')
#####################################################

##########################################################################################################
while(True):
    # URL'den Gelen Görüntüleri Okuyoruz
    _, capturedSnapshotX1 = captureVideoFromUrlAxisX1.read()
    _, capturedSnapshotX2 = captureVideoFromUrlAxisX2.read()

    _, capturedSnapshotY1 = captureVideoFromUrlAxisY1.read()
    _, capturedSnapshotY2 = captureVideoFromUrlAxisY2.read()

##########################################################################################################
    # Görüntülerin Gelip Gelmediğine Dair Kontroller Ekliyoruz
    if capturedSnapshotX1 is not None and capturedSnapshotX2 is not None:
        if capturedSnapshotY1 is not None and capturedSnapshotY2 is not None:
            # X Ekseninde Bulunan Birinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            _, carCountLabelX1, _0 = openCvLib.detect_common_objects(capturedSnapshotX1)

            # X Ekseninde Bulunan İkinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            _, carCountLabelX2, _0 = openCvLib.detect_common_objects(capturedSnapshotX2)

            # Y Ekseninde Bulunan Birinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            _, carCountLabelY1, _0 = openCvLib.detect_common_objects(capturedSnapshotY1)

            # Y Ekseninde Bulunan İkinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            _, carCountLabelY2, _0 = openCvLib.detect_common_objects(capturedSnapshotY2)

            # X ve Y Eksenlerinde Bulunan Toplam Araç Sayısını Hesaplıyoruz
            totalCarAxisX = carCountLabelX1.count('car') + carCountLabelX2.count('car')
            totalCarAxisY = carCountLabelY1.count('car') + carCountLabelY2.count('car')

            # Araç Sayısının Fazla Olduğu Tarafa Yeşil Işık Yaktırıp Diğer Tarafa Kırmızı Yaktırıyoruz
            if totalCarAxisX > totalCarAxisY:
                xAxisLight = 1
                yAxisLight = 0
            else:
                xAxisLight = 0
                yAxisLight = 1

            if openCv.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            break
    else:
        break

##########################################################################################################

captureVideoFromUrlAxisX1.release()
captureVideoFromUrlAxisX2.release()
captureVideoFromUrlAxisY1.release()
captureVideoFromUrlAxisY2.release()
openCv.destroyAllWindows()