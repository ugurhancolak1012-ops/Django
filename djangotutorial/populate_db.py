import os
import django
import random
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question, Choice

def populate():
    print("Veritabanı temizleniyor ve yeni sorular ekleniyor...")
    
    # Optional: Clear existing data to avoid duplicates
    # Question.objects.all().delete()

    questions_data = [
        {
            "text": "Yazılım dünyasında favori dilin hangisi?",
            "choices": ["Python 🐍", "JavaScript 🟨", "Go 🐹", "Rust 🦀", "Java ☕"]
        },
        {
            "text": "Hafta sonu için ideal planın nedir?",
            "choices": ["Kod yazmak ve proje geliştirmek 💻", "Doğada kamp yapmak 🌲", "Netflix & Chill 🍿", "Arkadaşlarla dışarı çıkmak 🍻", "Sadece uyumak 😴"]
        },
        {
            "text": "Yapay zeka (AI) geleceği nasıl etkileyecek?",
            "choices": ["Hayatımızı cennete çevirecek 🚀", "Pek çok mesleği bitirecek 🤖", "İnsanlık ile birleşecek 🧠", "Terminator senaryosu gerçek olacak 💀"]
        },
        {
            "text": "Pizzada ananas olur mu?",
            "choices": ["Kesinlikle EVET! 🍍", "Asla, bu bir suçtur! 🚫", "Fark etmez, pizza pizzadır 🍕"]
        },
        {
            "text": "Bir süper gücün olsa hangisini seçerdin?",
            "choices": ["Uçmak 🦅", "Görünmezlik 👻", "Zihin okumak 🔮", "Işınlanmak ⚡", "Zamanı durdurmak ⏳"]
        },
        {
            "text": "Hangi çalışma ortamını tercih edersin?",
            "choices": ["Evden (Remote) 🏠", "Ofisten 🏢", "Hibrit 🔄", "Sahil kasabasından 🏖️"]
        },
        {
            "text": "Mutluluğun sırrı sence nedir?",
            "choices": ["Anı yaşamak ✨", "Sürekli gelişim 📈", "Sevgi ve bağlar ❤️", "Finansal özgürlük 💸"]
        }
    ]

    for q_data in questions_data:
        # Create Question
        q = Question.objects.create(
            question_text=q_data["text"],
            pub_date=timezone.now()
        )
        print(f"Soru eklendi: {q.question_text}")

        # Create Choices
        for choice_text in q_data["choices"]:
            # Add some random initial votes to make it look alive
            random_votes = random.randint(0, 15)
            Choice.objects.create(
                question=q,
                choice_text=choice_text,
                votes=random_votes
            )

    print("\n✅ Başarıyla tamamlandı! Harika sorular eklendi.")

if __name__ == '__main__':
    populate()
