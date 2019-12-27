# AutoTrafficLightsControll

OpenCV ve Tensorflow Kütüphanelerini Kullanarak Kameralardan Alınan Görüntüler İle Trafik Işıklarının Otomatik Kontrolünü Sağlıyoruz. Açıklamalar `detection.py` Dosyasında Belirtilmiştir.
## Tensorflow Modelleri

Obje Tanımlaması İçin Kullanılacak Tensorflow Modellerini Aşağıdan Bulabilirsiniz,

[TensorFlow Modelleri](https://github.com/tensorflow/models)

## Ortam Değişkenlerinin Yüklenmesi

Öncelikle [Anaconda](https://www.anaconda.com/distribution/)'nın Sitesine Giderek İlgili İşletim Sistemine Göre Python 3.7 Sürümlü Anaconda'yı İndirmeniz Gerekmektedir.

Yükleme İşlemi Bittikten Sonra Yeni Ortam Değişkeni Oluşturuyoruz

	conda create -n env python=3.7
	
Daha Sonra Oluşturduğumuz Ortam Değişkenini Kullanabilmek İçin Aktif Hale Getiriyoruz
	
	source activate myenv

## Kütüphanelerin Kurulumu

Projede İhtiyaç Duyulan Kütüphanelerin Ortam Değişkenlerine Yüklenmesi Gerekmektedir.

Numpy Kütüphanesinin Kurulumu

	pip install numpy
	
Matplotlib Kütüphanesinin Kurulumu

	pip install matplotlib

Cvlib Kütüphanesinin Kurulumu

	pip install cvlib
	
OpenCv Kütüphanesinin Kurulumu

	pip install opencv-python
	
Tensorflow Kütüphanesinin Kurulumu

	pip install tensorflow
	


Tensorflow Nesne Algılama Kurulum Kılavuzu Aşağıdaki Bağlantıda Verilmiştir. Kurulumda Her Adımın İşlendiğinden Emin Olmalısınız.

[Tensorflow - Nesne Algılama Kurulum Kılavuzu](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)

## Projeyi Çalıştırma

Komut Ekranında Projenin Olduğu Klasöre Giderek Ortam Değişkenlerini Aktif Ediyoruz

	cd C:\Users\Documents\ProjectName
	conda activate env
	
Daha Sonra Projemizdeki `detection.py` dosyasını çalıştırıyoruz.

    py detection.py