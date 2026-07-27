# Python Professional Port Scanner

Python ile geliştirilmiş, TCP portlarını kontrol eden profesyonel
bir port tarama uygulamasıdır.

## Özellikler

- IP adresi veya alan adı ile hedef belirleme
- TCP port taraması
- Belirlenen port aralığını tarama
- Çoklu thread kullanımı
- Açık portları tespit etme
- Bilinen servis adlarını görüntüleme
- Tarama süresini hesaplama
- TXT formatında rapor oluşturma
- CSV formatında rapor oluşturma
- Kullanıcı girişlerini doğrulama
- Hatalı girişleri kontrol etme

## Kullanılan Teknolojiler

- Python
- Socket
- ThreadPoolExecutor
- CSV
- Dosya işlemleri

## Proje Yapısı

```text
PortScanner/
│
├── PortScanner.py
├── scanner.py
├── validators.py
├── reports.py
├── requirements.txt
├── README.md
└── results/