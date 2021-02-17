from django.urls import path , re_path
from . import views

urlpatterns = [
    path('', views.news , name='news' ),
    path('news/', views.news , name='news' ),
    path('business/', views.business , name='business' ),
    path('sport/', views.sport , name='sport' ),
    path('entertainment/', views.entertainment , name='entertainment' ),
    path('lifestyle/', views.lifestyle , name='lifestyle' ),

    path('news/<content>', views.content , name='content' ),

]