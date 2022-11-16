from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('group/<slug:slug>/', include('posts.urls')),
    path('about/', include('about.urls', namespace='about')),
]
