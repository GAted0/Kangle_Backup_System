from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('front.urls')),
    path('captcha/', include('captcha.urls')),
    path('djadmin/', admin.site.urls)
]
