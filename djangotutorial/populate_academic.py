import os
import django
import random
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question, Choice

def populate():
    print("Veritabanı akademik anket için hazırlanıyor...")
    
    # Mevcut soruları temizle (Sıfırdan kurulum)
    Question.objects.all().delete()
    print("Eski veriler temizlendi.")

    questions_data = [
        {
            "text": "Vize haftasında uyku düzenin nasıl değişiyor?",
            "choices": ["Değişmiyor, düzenli uyurum 😴", "Günde 3-4 saate düşüyor ☕", "Hiç uyumuyorum, zombiye dönüyorum 🧟", "Sadece sınavdan sonra uyuyorum 🛌"]
        },
        {
            "text": "Kampüste ders aralarında en çok ne yapıyorsun?",
            "choices": ["Kütüphanede ders çalışıyorum 📚", "Kantin/Kafe muhabbeti ☕", "Çimlerde yatış 🌳", "Kulüp odasında takılmaca 🎸"]
        },
        {
            "text": "Sabah 8:30 dersine yaklaşımın nedir?",
            "choices": ["Asla kaçırmam, en ön sıradayım 🤓", "Alarmı erteleyip geç kalırım ⏰", "Gitmeyi denerim ama uyanamam 💤", "O saatte ders mi olur? Gitmem. 🚫"]
        },
        {
            "text": "Öğrenci evinde/yurdunda en büyük kriz nedir?",
            "choices": ["Bulaşık sırası 🍽️", "İnternetin yavaşlaması 📶", "Gürültü yapan oda arkadaşı 🔊", "Ay sonu paranın bitmesi 💸"]
        },
        {
            "text": "Hangi ders türü seni daha çok zorlar?",
            "choices": ["Ezbere dayalı teorik dersler 📖", "Proje ve sunum odaklı dersler 📽️", "Matematiksel/İşlem ağırlıklı dersler 🧮", "Sabahın köründeki lab dersleri 🧪"]
        },
        {
            "text": "Okul bittikten sonraki kariyer planın ne?",
            "choices": ["Kurumsal bir şirkette çalışmak 🏢", "Kendi girişimimi kurmak 🚀", "Akademisyen olarak kalmak 🎓", "Dünyayı gezmek, plan yok 🌍"]
        },
        {
            "text": "Üniversite yemekhanesi hakkında düşüncen?",
            "choices": ["Fiyat/Performans harikası 🍲", "Sadece mecbur kalınca yiyorum 😐", "Asla yemem, dışarıdan söylerim 🍔", "Çıkan yemeğe göre değişir 🎰"]
        },
        {
            "text": "Ders notlarını nasıl tutarsın?",
            "choices": ["Kağıt kalemle düzenli not alırım 📝", "Tablet/Laptop kullanırım 💻", "Sadece fotoğraf çekerim 📸", "Arkadaştan fotokopi alırım 🖨️"]
        },
        {
            "text": "Erasmus veya değişim programı düşünüyor musun?",
            "choices": ["Kesinlikle, bavulum hazır! ✈️", "Kararsızım, ortalamam yetmeyebilir 🤔", "Hayır, okulu uzatmak istemem 🏠", "Zaten gittim geldim, harikaydı 🌟"]
        },
        {
            "text": "Üniversite hayatını tek kelimeyle özetle?",
            "choices": ["Efsane 🎉", "Yorucu 😫", "Öğretici 💡", "Bitse de gitsek ⏳"]
        }
    ]

    for q_data in questions_data:
        q = Question.objects.create(
            question_text=q_data["text"],
            pub_date=timezone.now()
        )
        print(f"Eklendi: {q.question_text}")

        for choice_text in q_data["choices"]:
            Choice.objects.create(
                question=q,
                choice_text=choice_text,
                votes=0  # Sıfır oyla başlatıyoruz
            )

    print("\n✅ Akademik anket veritabanı hazır!")

if __name__ == '__main__':
    populate()
