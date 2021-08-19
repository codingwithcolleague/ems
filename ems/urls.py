"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from employee.views import user_login,user_success,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("poll/" , include(("poll.urls" , "poll") , namespace="poll")  ),
    path("employee/" , include(("employee.urls" , "employee") , namespace="employee")  ),

    path("login/", user_login, name="user_login"),
    path("success/", user_success , name="success"),
    path("logout/", user_logout , name="logout")

]
