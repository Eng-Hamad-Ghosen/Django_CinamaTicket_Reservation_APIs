"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from ticket import views

from rest_framework.routers import DefaultRouter

#Viewset
router=DefaultRouter()
router.register('guest',views.Viewsets_guest)

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/no_rest_no_model/',views.no_rest_no_model),
    #2
    path('django/no_rest_with_model/',views.no_rest_with_model),
    
    #3.1 FBV [GET , POST]
    path('rest/fbv/',views.FBV_list),
    #3.2 FBV [GET , PUT , DELETE] With pk
    path('rest/fbv/<int:pk>/',views.FBV_pk),
    
    #4.1 CBV [GET , POST]
    path('rest/cbv/',views.CBV_list.as_view()),
    #4.2 CBV [GET,PUST,DELETE] With pk
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    
    #5.1 Mixins [GET , POST]
    path('rest/mixin/',views.Mixins_list.as_view()),
    #5.2 Mixin [GET , PUT , DELETE] with pk
    path('rest/mixin/<int:pk>',views.Mixin_pk.as_view()),
    
    #6.1 Generics [GET , POST]
    path('rest/generic/',views.Generics_list.as_view()),
    #6.2 Generics [GET , PUT , DELETE] With pk
    path('rest/generic/<int:pk>',views.Generics_pk.as_view()),
    
    #7 Viewsets [GET,POST, PUT , DELETE] With pk and Without
    path('rest/viewset/',include(router.urls)),
]
