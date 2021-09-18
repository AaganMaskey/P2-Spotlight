from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.Add_Creator, name="create"),
    path('display/', views.View_Projects, name="display"),
]