import os
import django
from django.utils import timezone
from polls.models import Question, Choice

q1 = Question(question_text="Sivas'ın en sevdiğin ilçesi neresidir?", pub_date=timezone.now())
q1.save()
q1.choice_set.create(choice_text="Şarkışla", votes=0)
q1.choice_set.create(choice_text="Divriği", votes=0)
q1.choice_set.create(choice_text="Kangal", votes=0)
q1.choice_set.create(choice_text="Zara", votes=0)

q2 = Question(question_text="Sivas'ta en çok neyin olmasını istersin?", pub_date=timezone.now())
q2.save()
q2.choice_set.create(choice_text="Deniz", votes=0)
q2.choice_set.create(choice_text="Daha çok yeşil alan", votes=0)
q2.choice_set.create(choice_text="Daha fazla festival", votes=0)
q2.choice_set.create(choice_text="Metro", votes=0)

q3 = Question(question_text="Meşhur Sivas köftesini en iyi nerede yersin?", pub_date=timezone.now())
q3.save()
q3.choice_set.create(choice_text="Kirli Ahmet", votes=0)
q3.choice_set.create(choice_text="Meydan'daki herhangi bir yer", votes=0)
q3.choice_set.create(choice_text="Asıl Sivas köftesi evde yapılır", votes=0)

print("Sivas soruları başarıyla eklendi!")
