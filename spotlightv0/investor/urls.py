from django.urls import path
from . import views
urlpatterns = [
    path('checkout/<pid>', views.investor_checkout_view, name="investor-checkout"),
]
