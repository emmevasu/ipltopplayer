from django.contrib import admin
from django.urls import path
from .views import IplTopScorer

urlpatterns = [
    # path('',views.Input),
    path('<int:num>',IplTopScorer),
]