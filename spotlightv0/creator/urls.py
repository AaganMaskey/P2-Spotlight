from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.Add_Creator, name="create"),
    path('display/', views.View_Projects, name="display"),
    path('projects/',views.Projects_view,name = "projects"),
    path('project/<pid>', views.View_Projects_Details,name= 'project description')
]