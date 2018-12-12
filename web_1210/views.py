from django.http import HttpResponse
from django.shortcuts import render

def root(request):
    name = request.GET.get("name", "guest")
    return HttpResponse("hi, {}".format(name))

def hello(request, name):
    return HttpResponse("hi,{}".format(name))

def s(request, number):
    return HttpResponse(number **2)

def l(request, num1, num2):
    # if num1 < num2:
    #     _list = range(num1, num2+1)
    # else:
    #     _list = reversed(range(num2, num1+1))

    _list = range(10, 0, -1)

    step = -1 if num1>num2 else 1
    _list = range(num1, num2+step, step)
    
    return render(request, "h.html", {"list": _list})

