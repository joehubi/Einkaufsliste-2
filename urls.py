"""
URL configuration for koop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from mylist.views import Koop_view_price

from mylist.views import Person_1_add
from mylist.views import Person_1_addSmart
from mylist.views import Person_1_delete
from mylist.views import Person_1_sum

from mylist.views import Person_2_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('koop_price/', Koop_view_price),
    path('Person_1/add/', Person_1_add),
    path('Person_1/delete/', Person_1_delete),
    path('Person_1/addSmart/', Person_1_addSmart),
    path('Person_1/sum/', Person_1_sum),
    path('Person_2/add/', Person_2_add),
]
