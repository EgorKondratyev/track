from django.urls import path

from home import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.track_search, name='track_search'),
    path('payment/', views.payment, name='payment'),
    path('my_track/', views.my_track, name='my_track')
]
