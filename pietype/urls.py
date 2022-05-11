from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('about/', views.about, name='about'),
    path('<int:attempt_id>/', views.attempt, name='attempt')
]