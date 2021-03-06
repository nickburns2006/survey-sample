from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('surveys/', include('surveys.urls'), name="index"),
    path('admin/', admin.site.urls),
]
