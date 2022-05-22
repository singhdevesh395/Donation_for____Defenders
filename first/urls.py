from django.urls import path

from . import views
# from marketing.views import email_list_signup
urlpatterns=[
 
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('donate',views.donate,name='donate'),
    path('about',views.about,name='about'),
    path('feedback',views.feedback,name='feedback'),
    path('news',views.news,name='news'),
    path('participate',views.participate,name='participate'),
    path('events',views.events,name='events'),
    # path('suscribe',email_list_signup,name='suscribe'),
    path('don',views.don,name='don'),
    path('fund',views.fund,name='fund'),
]

