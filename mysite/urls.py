from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('polls/', include('polls.urls', namespace='polls')),
    path('admin/', admin.site.urls),
]