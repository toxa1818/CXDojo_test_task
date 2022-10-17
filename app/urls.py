from django.urls import path
from .views import index, upload_files

urlpatterns = [
    path('', index, name='index'),
    path('upload_files/', upload_files, name='upload'),
]
app_name = 'includes'
