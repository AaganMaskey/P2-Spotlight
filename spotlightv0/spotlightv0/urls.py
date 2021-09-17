from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
if settings.DEBUG:
    URLPattern = [static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)]

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from authentication import views
from creator import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('investor/', include("investor.urls")),
    path('creator/', include("creator.urls")),
    path('profile/', login_required(views.ProfileView.as_view()),name='profile'),

]
