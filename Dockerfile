# Docker imajın temel alinacak taban imaji
FROM python:3.10.12

# Uygulamanın çalışacağı çalışma dizisi
WORKDIR /home/aisankheiri/Desktop/acikkaynakodev2

# Uygulama bağımlılıklarin kopyasi
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Konteynerin hangi portu dinleyeceğini belirle
EXPOSE 5000

# Uygulamayı başlatmak için komutu belirle
CMD [ "python", "app.py" ]
