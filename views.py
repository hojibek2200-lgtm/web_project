from django.shortcuts import render


from django.http import HttpResponse

def shahar_uchun(request):
    return HttpResponse("Termiz shahar")

def viloyat_uchun(request):
    return HttpResponse("Surxondaryo Viloyati")

def malakat_uchun(request):
    return HttpResponse("O'zbekiston Respublikasi")

def info_beruvchi(request):
    text = "Ism: Xojibek\nFamiliya: Amonturdiyev\nTel: +998952767642"
    return HttpResponse(text)

