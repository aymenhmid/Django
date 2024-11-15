"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# djangoproject/urls.py (or yourapp/urls.py)

from django.contrib import admin
from django.urls import path
from djangoproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_post, name='create_post'),  # This handles /create/
    path('success/', views.success, name='success'),  # This handles /success/
    
    # Add a pattern for the root (empty path)
    path('', views.create_post, name='home'),  # This will now handle the root path /
]
