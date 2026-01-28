from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'pots'

urlpatterns = [
    path('pots/', views.pots, name="pots"),
    path('pots/pot/<str:name>/', views.pot, name="pot")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
