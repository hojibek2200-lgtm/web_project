from django.shortcuts import render


from django.http import HttpResponse
from .models import Yangiliklar
from rest_framework import generics
from .serializers import YangiliklarSerializer

def shahar_uchun(request):
    return HttpResponse("Termiz shahar")

def viloyat_uchun(request):
    return HttpResponse("Surxondaryo Viloyati")

def malakat_uchun(request):
    return HttpResponse("O'zbekiston Respublikasi")

def info_beruvchi(request):
    text = "Ism: Xojibek\nFamiliya: Amonturdiyev\nTel: +998952767642"
    return HttpResponse(text)

def all_news(request):
    news = Yangiliklar.objects.all()
    context = {
        'news':news
    }
    return render(request, 'all_news.html', context)


def detail(request, id):
    yangilik = Yangiliklar.objects.get(id=id)
    context = {
        'yangilik':yangilik
    }
    return render(request, 'detail.html', context)

class YangiliklarList(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
