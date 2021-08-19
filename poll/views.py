from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    obj_list = Question.objects.all()
    context = {}
    context['title'] = 'poll'
    context['questions'] = obj_list
    return render(request,"poll/index.html" , context)

def details(request,id=None):
    print("iddd" , id)
    context = {}
    try:
        obj_list = Question.objects.get(id=id)
    except:
        raise Http404
    context['title'] = 'poll'
    context['question'] = obj_list
    print("objjjj" , obj_list)
    return render(request,"poll/details.html" , context)

def poll(request,id=None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request,"poll/poll.html",context)
    elif request.method == "POST":
        user_id = 1
        data = request.POST
        rel = Answer.objects.create( user_id=user_id , choice_id=data['choice'])
        if rel:
            return HttpResponse("your vote is done successfully")
        else:
            return HttpResponse("your vote is not done")
