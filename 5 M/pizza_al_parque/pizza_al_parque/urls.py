"""
URL configuration for pizza_al_parque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from menu import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.list_food, name="list_food"),
    path('charge_type/', views.charge_type, name="charge_type"),
    path('edit_type/<int:type_id>/', views.edit_type, name="edit_type"),
    path('delete_type/<int:type_id>/', views.delete_type, name="delete_type"),
    path('description/<int:type_id>/', views.description_types, name="description_types"),
    path('charge_food/<int:type_id>/', views.charge_food, name="charge_food"),
    path('delete_food/<int:food_id>/<int:type_id>/', views.delete_food, name="delete_food")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
