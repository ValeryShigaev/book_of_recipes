from django.urls import path

from app_book.views import MainPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)