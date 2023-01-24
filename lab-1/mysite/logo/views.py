from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h3>Здравствуйте, мы рады сотрудничеству! Для одобрения заказа позвоните по номеру: 8 905 035 41-**</h3>")

def first(request):
    return render(request, "logo/firstpage.html")

def contact(request):
    return render(request, "logo/contact.html", {'content': [' Здравствуйте, мы рады сотрудничеству! Для одобрения заказа позвоните по номеру: 8 905 035 41-**']})