"""
URL configuration for projectName project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app01 import views as app01_views  # Alias for app01 views
from app02 import views as app02_views  # Alias for app02 views

from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_index),  # Default route to app01 index
    path('app01/', app01_views.app01_index),  # Include URLs from app01
    path('app02/', app02_views.app02_index),  # Include URLs from app02
]
