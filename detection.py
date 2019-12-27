#####################################################
#### Proje Sahibi   : Talha Can
#### Mail           : rampesna@gmail.com
#### Tarih          : 9 Aralık 2019
######################################################

#####################################################
#İlgili Kütüphaneleri Projemize Dahil Ediyoruz
import cv2 as openCv
import matplotlib.pyplot as plt
import cvlib as openCvLib
import numpy
from cvlib.object_detection import draw_bbox
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
    _X1, frameX1 = captureVideoFromUrlAxisX1.read()
    _X2, frameX2 = captureVideoFromUrlAxisX2.read()

    _Y1, frameY1 = captureVideoFromUrlAxisY1.read()
    _Y2, frameY2 = captureVideoFromUrlAxisY2.read()

##########################################################################################################
    # Görüntülerin Gelip Gelmediğine Dair Kontroller Ekliyoruz
    if frameX1 is not None and frameX2 is not None:
        if frameY1 is not None and frameY2 is not None:
            # X Ekseninde Bulunan Birinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            bBoxX1, labelX1, configX1 = openCvLib.detect_common_objects(frameX1)
            outputImageX1 = draw_bbox(frameX1, bBoxX1, labelX1, configX1)

            # X Ekseninde Bulunan İkinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            bBoxX2, labelX2, configX2 = openCvLib.detect_common_objects(frameX2)
            outputImageX2 = draw_bbox(frameX2, bBoxX2, labelX2, configX2)

            # Y Ekseninde Bulunan Birinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            bBoxY1, labelY1, configY1 = openCvLib.detect_common_objects(frameY1)
            outputImageY1 = draw_bbox(frameY1, bBoxY1, labelY1, configY1)

            # Y Ekseninde Bulunan İkinci Kameradan Alınan Görüntüyü Tensorflow İle İşleyip Sayımını Yapıyoruz
            bBoxY2, labelY2, configY2 = openCvLib.detect_common_objects(frameY2)
            outputImageY2 = draw_bbox(frameY2, bBoxY2, labelY2, configY2)

            # X ve Y Eksenlerinde Bulunan Toplam Araç Sayısını Hesaplıyoruz
            totalCarAxisX = labelX1.count('car') + labelX2.count('car')
            totalCarAxisY = labelY1.count('car') + labelY2.count('car')

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