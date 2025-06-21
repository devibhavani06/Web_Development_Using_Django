from django.contrib import admin
from django.urls import path
from NewApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sta/',views.static_url,name='Static'), #static url

    path('dyn/<str:name>/<int:id>/',views.dynamic_url,name='Dynamic') #dynamic url
]