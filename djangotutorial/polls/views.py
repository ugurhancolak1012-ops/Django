from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.TemplateView):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # İlk soruyu bul ve context'e ekle
        first_question = Question.objects.order_by('id').first()
        context['first_question'] = first_question
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Tüm soru ID'lerini al
        all_questions = list(Question.objects.order_by('id').values_list('id', flat=True))
        current_id = self.object.id
        
        # Kaçıncı sorudayız?
        try:
            current_index = all_questions.index(current_id) + 1
        except ValueError:
            current_index = 0
            
        total_questions = len(all_questions)
        
        # Yüzde hesapla
        if total_questions > 0:
            progress_percentage = (current_index / total_questions) * 100
        else:
            progress_percentage = 0

        context['current_step'] = current_index
        context['total_steps'] = total_questions
        context['progress_percentage'] = int(progress_percentage)
        return context


class ResultsView(generic.ListView):
    template_name = "polls/results.html"
    context_object_name = "question_list"

    def get_queryset(self):
        # Tüm soruları getir
        return Question.objects.all().order_by('id')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Lütfen bir seçenek işaretleyin.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        
        # Sonraki soruyu bul (ID'si şu ankinden büyük olan ilk soru)
        next_question = Question.objects.filter(id__gt=question.id).order_by('id').first()
        
        if next_question:
            # Varsa bir sonrakine git
            return HttpResponseRedirect(reverse("polls:detail", args=(next_question.id,)))
        else:
            # Soru bittiyse sonuç ekranına git
            return HttpResponseRedirect(reverse("polls:results"))