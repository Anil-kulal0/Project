
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('logout', views.logout, name='logout'),
     path('signup/', views.register, name='register'),
    
    path('accounts/', include('django.contrib.auth.urls')),
]