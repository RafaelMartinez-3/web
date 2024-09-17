from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts  import get_object_or_404,render
from .models import Choice,Question
from django.db.models import F
from django.views import generic

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name ="lates_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name ="pollss/detail.html"

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"    
   
def vote (request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.Post["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question": question,"error_message":"no seleccionaste nada"})
    else:
        selected_choice=F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id)))
    


