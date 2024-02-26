from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('event/',views.myevent),
    path('imagegallery/',views.igallery),
    path('videogallery/',views.vgallery),
    path('viewdetails/',views.viewdetails),
    path('logout/',views.logout),
    path('booking/',views.booking),
    path('mytickets/',views.myticket),
    path('myprofile/',views.myprofile),

]

