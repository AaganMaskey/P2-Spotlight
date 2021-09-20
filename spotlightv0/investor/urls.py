from django.urls import path
from . import views
urlpatterns = [
    path('checkout/', views.investor_view, name="investor"),
]
