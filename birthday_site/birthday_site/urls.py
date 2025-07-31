from django.contrib import admin
from django.urls import path
from greeting.views import birthday_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', birthday_page),
]
