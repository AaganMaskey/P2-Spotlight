from django.urls import path
from . import views
urlpatterns = [
    path('checkout/<pid>', views.InvestorCheckoutView, name="investor-checkout"),
]
