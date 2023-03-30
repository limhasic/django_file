from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "upload"

urlpatterns = [
    path("", views.uploadFile, name = "uploadFile"),
    path('csv/<int:file_id>/', views.view_csv, name='view_csv'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )