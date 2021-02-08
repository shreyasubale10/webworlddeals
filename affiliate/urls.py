from django.urls import path
from . import views

urlpatterns = [
    path('',views.affiliate,name='affiliate'),
    path('menswear',views.menswear,name="menswear"),
    path('womens',views.womens,name="womens"),
    path('grocerry',views.grocerry,name="grocerry"),
    path('mobile',views.mobile,name="mobile"),
    path('electronic',views.electronic,name="electronic"),
    path('cosmetics',views.cosmetics,name="cosmetics"),
    path('homeappliance',views.homeappliance,name="homeappliance"),
    path('interior',views.interior,name="interior"),
    path('sports',views.sports,name="sports"),
    path('gym',views.gym,name="gym"),
]
