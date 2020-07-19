from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

