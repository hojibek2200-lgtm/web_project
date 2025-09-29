
from django.urls import path

# from config.urls import urlpatterns
from .views import shahar_uchun, viloyat_uchun, malakat_uchun, info_beruvchi, all_news, detail, YangiliklarList

urlpatterns = [
    path('yangiliklar_list/', YangiliklarList.as_view(), name='yangiliklar-list'),
    path('shahar_uchun/', shahar_uchun),
    path('viloyat_uchun/', viloyat_uchun),
    path('malakat_uchun/', malakat_uchun),
    path('info_beruvchi/', info_beruvchi),
    path('all_news/', all_news, name='news'),
    path('detail/<int:id>/', detail, name='detail'),


]
# urlpatterns += [
#     path('yangiliklar-list/', YangiliklarList.as_view(), name='yangiliklar-list')
# ]
