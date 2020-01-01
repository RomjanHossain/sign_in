from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sup, name='sign_up'),
    path('home/', views.home, name='homee'),
]
urlpatterns += staticfiles_urlpatterns()
