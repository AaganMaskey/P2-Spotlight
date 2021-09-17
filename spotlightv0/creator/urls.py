from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.Add_Creator, name="create"),
]