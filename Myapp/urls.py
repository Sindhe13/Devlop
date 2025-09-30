
from django.urls import path
from . import views

urlpatterns = [

    # path('', views.Page_1, name='home'),
   
    path('page1/', views.cloud, name='page1'),
    
    #agri page 
    path('Agri_1/', views.Agri_1,),
    path('Agri_2/', views.Agri_2, ),
 
    path('Agri_4/', views.Agri_4, ),
    path('Agri_5/', views.Agri_5, ),
   
   
   #edu 
   path('Edu_1/',views.Edu_1, name="edu"),
   
#    main
 path('',views.Land, name="land"),
 path('Land_1/',views.Land_1, ),
 path('Land_2/',views.Land_2, ),
 path('Land_3/',views.Land_3, ),
 path('Land_4/',views.Land_4, ),
   
]