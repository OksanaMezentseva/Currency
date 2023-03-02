"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from currency.views import (
    contact_list, list_rates, rates_create, rates_update, rates_delete, rate_details,
    list_sources, sources_create, sources_update, sources_delete, source_details
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/list', contact_list),
    path('rate/create/', rates_create),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
    path('rate/details/<int:pk>/', rate_details),
    path('rate/list/', list_rates),
    path('source/list/', list_sources),
    path('source/create/', sources_create),
    path('source/update/<int:pk>/', sources_update),
    path('source/delete/<int:pk>/', sources_delete),
    path('source/details/<int:pk>/', source_details),
]
