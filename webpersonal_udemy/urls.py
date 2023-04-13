from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contact/', views.contact, name = 'contact')
]

# Servir imgs en modo debug (fase desarrollo)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)