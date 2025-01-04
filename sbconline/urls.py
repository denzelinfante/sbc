from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sbc/', include('sbc.urls')),  # Includes the SBC app's URLs
    path('', lambda request: redirect('login')),  # Redirect root URL to 'login' view
]
    