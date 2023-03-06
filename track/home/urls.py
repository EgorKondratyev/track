from django.urls import path

from home import views

urlpatterns = [
    path('', views.main_page, name='main_page')
]
