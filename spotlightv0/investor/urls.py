from django.urls import path
from . import views
urlpatterns = [
    path('investor/', views.investor_view, name="investor"),
]
