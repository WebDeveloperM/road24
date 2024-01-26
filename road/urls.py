from django.urls import path
from .views import *
urlpatterns = [
     path("" ,main , name='main'),
     path("avtorizatsiya/" ,avtorizatsiya , name='avtorizatsiya'),
     path("sms/<str:phone>/<str:dis_id>/" ,sms , name='sms'),
     path("verification-sms/" ,verification_sms , name='verification_sms'),
     path("shtraf/" ,shtraf , name='shtraf'),
     path("create/" ,create , name='create'),
     path("is_payment_true/" ,is_payment_true , name='is_payment_true'),
     path("is_payment_false/" ,is_payment_false , name='is_payment_false'),

     path("fine/<int:pk>" ,fine , name='fine'),
     path("to_pay/<int:pk>" ,to_pay , name='to_pay'),

     path("addCart/" ,addCart , name='addCart'),

     path("radar/<int:pk>" ,radar , name='radar'),
     path('delete_car_item/<int:pk>', delete_car_item, name='delete_car_item'),
     path('delete_card_item/<int:pk>', delete_card_item, name='delete_card_item'),







   

]
