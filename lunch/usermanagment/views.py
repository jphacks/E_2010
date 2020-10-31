from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
def loginfunction(request):
    return render(request, 'index.html')

@api_view(["GET","POST"])
def login(request):
    if request.method =="GET":
        username = request.GET.get("username")
        pwd = request.GET.get("password")
    elif request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
    else:
        return render(request,template_name="error.html",context={"msg":"Error"})
    if username  is not None and pwd is not  None:
        if username =='admin'and pwd == "admin":
            return  render(request,"home.html",context={"username":username})
        else:
            return render(request, "error.html", context={"msg": "Input Error"})

    else:
        return  render(request,"error.html",context={"msg":"Need Name and Password"})