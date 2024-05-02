"# homework-5-may-open-source-code" 

Bu proje, Flask kullanarak bir Kitap API'si sunan bir Docker konteynerini başlatmayı amaçlamaktadır.

## Dosya Yapısı

- `app.py`: Flask uygulamasının ana dosyasıdır ve API rotalarını tanımlar.
- `openapi.yaml`: OpenAPI 3.0 belgesiyle API rotalarını ve şemalarını tanımlar.
- `Dockerfile`: Docker konteynerını oluşturmak için kullanılan dosyadır.

## Gereksinimler

Aşağıdaki yazılımların sisteminizde yüklü olduğundan emin olun:

- Python (versiyon 3.x)
- Docker

## Kurulum ve Çalıştırma

1. Bu depoyu bilgisayarınıza klonlayın:
git clone <repository-link>
2. Terminali açın ve proje dizinine gidin:
cd <project-directory>
3. Python bağımlılıklarını yükleyin:
pip install -r requirements.txt
4. Docker imajını oluşturun:
docker build -t <image-name> .
5. Docker konteynerını başlatın:
docker run -p <host-port>:5000 <image-name>
6. API'ye erişim sağlamak için aşağıdaki URL'yi kullanın:
http://localhost:<host-port>
7. API belgelerine erişmek için aşağıdaki URL'yi kullanabilirsiniz:
http://localhost:<host-port>/docs

## API Rotaları

- `GET /books`: Tüm kitapları listeler.
- `POST /books`: Yeni bir kitap oluşturur.
- `GET /books/{id}`: Belirli bir kitabı getirir.
- `PUT /books/{id}`: Belirli bir kitabı günceller.
- `DELETE /books/{id}`: Belirli bir kitabı siler.

Detaylı API belgeleri ve şemaları için OpenAPI belgesini inceleyebilirsiniz.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:
1. Bu depoyu forklayın.
2. Yeni bir özellik veya düzeltme yapmak için bir dal oluşturun:
git checkout -b feature/ozellik-adı
3. Değişikliklerinizi yapın ve bunları commit edin:
git commit -m "Açıklama"
4. Dalınızı ana depoya gönderin:
git push origin feature/ozellik-adı
5. Bir Pull Talebi (Pull Request) oluşturun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.