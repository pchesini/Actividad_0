from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
#def index(request):
 #   latest_question_list = Question.objects.order_by("-pub_date")[:5]
  #  template = loader.get_template("polls/index.html")
   # context = {
    #    "latest_question_list": latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
#def index(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

#def index(request):
   # return HttpResponse("Hola Mundo. Estás en el índice de encuestas.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

#def detail(request, question_id):
   # return HttpResponse("Estas viendo la pregunta %s." % question_id)


def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Estás votando por la pregunta. %s." % question_id)