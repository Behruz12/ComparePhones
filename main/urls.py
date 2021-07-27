from django.urls import path, include
from .views import MainIndex,PhoneCreateView, ComaprePhones, Compare_Phones, CompareOne


app_name = 'main'
urlpatterns = [
    path('', MainIndex.as_view(), name="index"),
    path('comapre_phone/', ComaprePhones, name="compare"),
    path('compare-phones/<int:i1>-<int:i2>/', Compare_Phones, name="compare-phones"),
    path('compare-one/<int:id>/', CompareOne.as_view(), name="compare-one"),
    path('post/', include([
        path('phones/', PhoneCreateView.as_view(), name='phone_create')
    ]))

]
