
from django.urls import path

# from config.urls import urlpatterns
from .views import shahar_uchun, viloyat_uchun, malakat_uchun, info_beruvchi

urlpatterns = [
    path('shahar_uchun/', shahar_uchun),
    path('viloyat_uchun/', viloyat_uchun),
    path('malakat_uchun/', malakat_uchun),
    path('info_beruvchi/', info_beruvchi)
]
