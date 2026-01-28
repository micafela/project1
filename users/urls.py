from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/register/', views.signup, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/home/', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
