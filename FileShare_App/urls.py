from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # This makes it the default/home route
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.upload_success, name='upload_success'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

