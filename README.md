# Django Polls App (Part 1 - Part 8)

Mükemmeliyetle tasarlanmış ve resmi Django Tutorial'ının 8 bölümden oluşan yapısına tamamen sadık kalarak, ayrıca modern CSS dokunuşları ve Sivas bölgesi özel anket sorularıyla zenginleştirilmiş proje altyapısıdır.

## 🚀 Proje İçeriği

Bu depo, Django'nun 8 bölümden oluşan web uygulaması eğitimini barındırır. Her bir part kendi klasöründe tamamen bağımsız bir şekilde çalışır duruma getirilmiştir. Aklınıza gelen herhangi bir part'ı seçip, uygulamanın o evresindeki gelişimini anında görüntüleyebilirsiniz.

Özellikle **Part 8**, en güncel ve en mükemmel tasarıma (CSS ile geliştirilmiş "Glassmorphism" ve modern detaylar) sahip olup, Sivas test soruları ve **Django Debug Toolbar** ile donatılmıştır.

## 📥 Kurulum

1. Repoyu bilgisayarınıza indirin (clone):
   ```bash
   git clone https://github.com/ugurhancolak1012-ops/Django.git
   cd Django
   ```

2. Eğer sisteminizde Django yüklü değilse yüklediğinizden emin olun. Ayrıca 8. bölümdeki hata ayıklama araçları için gerekli kütüphaneyi kurun:
   ```bash
   pip install django django-debug-toolbar
   ```

## 🎯 Nasıl Çalıştırılır?

Tek tek dizinlere girip `manage.py runserver` komutunu çalıştırmanıza gerek yoktur! Hazırladığımız özel `baslatici.py` script'i tüm sistemi tek bir tıkla yönetmek için tasarlanmıştır.

1. Ana dizinde aşağıdaki kodu çalıştırın:
   ```bash
   python baslatici.py
   # veya
   python3 baslatici.py
   ```

2. Ekranda size 1'den 8'e kadar hangi part'ı çalıştırmak istediğiniz sorulacaktır.

3. Örneğin `8` yazarak enter'a basın ve sunucunun başlamasını bekleyin.

4. Tarayıcınızı açın ve aşağıdaki adresleri ziyaret edin:
     - **Anketleri Görüntülemek ve Oy Vermek İçin:** [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)
     - **Tüm Sistemi Yönetmek İçin (Admin):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

> **Not:** Bütün parçalardaki veritabanları (SQLite) verilerle (hazır anketler) doludur, böylece projeye direkt start verdiğiniz gibi sistemi test edebilirsiniz.
