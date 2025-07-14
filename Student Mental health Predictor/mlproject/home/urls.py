from django.urls import path
from home import views

urlpatterns=[
    path('', views.index, name='home'),
    path('signup', views.signuppage, name='signup'),
    path('login/',views.loginpage, name='login'),
    path('about/', views.about, name='about'),
    path('prediction', views.prediction, name='about'),
    
]