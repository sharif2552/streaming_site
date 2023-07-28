# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/<int:id>', views.details, name='details'),
    path('',views.home),
    path('category/<int:category_id>/', views.category_template, name='category_template'),
    # Other URL patterns...
]

# Add these lines to include the static and media URLs
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
