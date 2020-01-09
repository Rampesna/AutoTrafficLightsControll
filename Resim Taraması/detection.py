#####################################################
#### Proje Sahibi   : Talha Can
#### Mail           : rampesna@gmail.com
#### Tarih          : 9 Aralık 2019
######################################################

#####################################################
#İlgili Kütüphaneleri Projemize Dahil Ediyoruz
import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox
#####################################################

#####################################################
# İşleme Yapılacak Görüntüyü Seçiyoruz
image = cv2.imread('img1.png')

#####################################################
# Kütüphaneye Alınan Görseli Göndererek Tespit Etme ve Saydırma İşlemlerini Yaptırıp Sonuçları Geri Alıyoruz
carShowBoxes, carCountLabel, detectionConfig = cvlib.detect_common_objects(image)

#####################################################
# Aldığımız Görüntüyü Ekrana Basmak İçin Önce Tespit Edilen Araçları Kare İçerisine Alıyoruz
outputImage = draw_bbox(image, carShowBoxes, carCountLabel, detectionConfig)

#####################################################
# Matlab Kütüphaneleri İle Görüntüyü Monitöre Veriyoruz
plt.imshow(outputImage)
plt.show()
print('Görselde Tespit Edilen Araba Sayısı ' + str(carCountLabel.count('car')))
#####################################################