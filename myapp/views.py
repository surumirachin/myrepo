from unittest import loader
from django.shortcuts import render
from django.http import  Http404, HttpResponse
from . models import Question

# Create your views here.
# def index(request):
#     return HttpResponse('welcome to my Questions.')

def Question_list(request):
    questions = Question.objects.all() 
    return render(request,'myapp/question_list.html',{'questions':questions})

def Choice_list(request, pk):
   
    question = Question.objects.get(pk=pk)
    return render(request, 'myapp/choice_list.html', {'question': question})


