from django.urls.conf import include
from . import views
from django.urls import path


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
