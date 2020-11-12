"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views as kilo_views

urlpatterns = [
    path('login/', kilo_views.login, name='login'),
    path('recover/', kilo_views.recover, name='recover'),
    path('register/<atype>/', kilo_views.register, name='register'),

    # path('register/cooperative/', kilo_views.register_coopperative, name='register_coopperative'),
    # path('register/factory/', kilo_views.register_factory, name='register_factory'),
    # path('register/officer/', kilo_views.register_fro, name='register_fro'),
    # path('register/farmer/', kilo_views.register_farmer, name='register_farmer'),

    # path(r'^settings/<atype>/<int:theid>$', kilo_views.data_settings, name='data_settings'),

    path('settings/<atype>/<int:theid>/', kilo_views.data_settings, name='data_settings'),

    # path('settings/cooperative/<int:pk>/', kilo_views.settings_coopperative, name='settings_coopperative'),
    # path('settings/factory/<int:pk>/', kilo_views.settings_factory, name='settings_factory'),
    # path('settings/officer/<int:pk>/', kilo_views.settings_fro, name='settings_fro'),
    # path('settings/farmer/<int:pk>/', kilo_views.settings_farmer, name='settings_farmer'),

    path('home/', kilo_views.home, name='home'),
    path('farmers/', kilo_views.farmers, name='farmers'),
    path('factories/', kilo_views.factories, name='factories'),
    path('transactions/', kilo_views.transactions, name='transactions'),
    path('fro/', kilo_views.fro, name='fro'),
    path('devices/', kilo_views.devices, name='devices'),
    path('products/', kilo_views.products, name='products'),
    path('404/', kilo_views.page_not_found, name='page_not_found'),
]
