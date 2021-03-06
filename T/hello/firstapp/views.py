from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0},Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm(field_order=["age", "name"])
        return render(request, "firstapp/index.html", {"form": userform})

    #userform = UserForm()
    #return render(request, "firstapp/index.html",
                 # {"form": userform})

    #return render(request, "firstapp/index.html", context={"cat": cat})
    #data = {"header": "Передача параметров в шаблон Django",
    #        "message":
    #        "Загружен шаблон templates/index_app1.html"}
    #return render(request, "firstapp/index_app1.html", context=data)
    #header = "Персональные данные"
    #langs = ["Английский", "Немецкий", "Испанский"]
    #user = {"name": "Максим,", "age": 30}
    #addr = ("Виноградная", 23, 45)
    #data = {"header": header, "langs": langs, "user": user, "address": addr}
    #return render(request, "index.html", context=data)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)

def details(request):
    return HttpResponsePermanentRedirect("/")

# Create your views here.
