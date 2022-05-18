from django.urls import path
from .import views

urlpatterns = [
    path('<filename>/', views.file),
    path('', views.file),
    # path('file1/', views.file1),
    # path('file2/', views.file2),
    # path('file3/', views.file3),
    # path('file4/', views.file4),
]