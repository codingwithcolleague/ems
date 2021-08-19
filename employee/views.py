from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,HttpResponse,HttpResponseRedirect
from django.urls import reverse 
from .forms import UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url= "/login/")
def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employee'
    return render(request,"employee/index.html", context)

@login_required(login_url= "/login/")
def employee_details(request,id=None):
    context = {}
    context['users'] = User.objects.get(id=id)
    context['title'] = 'Employee'
    return render(request,"employee/detail.html", context)

@login_required(login_url= "/login/")
def employee_add(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("employee:list"))
        else:
            return render(request,"employee/add.html",{"user_form": user_form })
    else:
        user_form = UserForm()
        return render(request, "employee/add.html" , { "user_form" : user_form })

@login_required(login_url= "/login/")
def employee_edit(request,id=None):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect( reverse("employee:list") )
    else:
        user_form = UserForm(instance=user)
        return render(request , "employee/edit.html" , {"user_form" : user_form } )

@login_required(login_url= "/login/")
def employee_delete(request,id=None):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect( reverse("employee:list") )
    else:
        context = {}
        context["user"] = user
        return render(request, "employee/delete.html" , context )
    
    
def user_login(request):
    conetxt = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.GET.get('next' , None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse("success"))
        else:
            conetxt["error"] = "Provide valid credential"
            return render(request,"auth/login.html",conetxt)
    else:
        return render(request,"auth/login.html",conetxt)
    
    
def user_success(request):
    context = {}
    context["request"] = request
    return render(request,"auth/success.html", context)

    
def user_logout(request):
    if request.method == "POST":
        logout(request)
    return HttpResponse("User logout successfull")