from django.shortcuts import render
from .models import Office

# Create your views here.

def h(request):
    if request.method=="POST":
        n1=request.POST.get("n")
        n2=request.POST.get("d")
        info=Office()
        info.name=n1
        info.department=n2
        info.save()
        return render(request,"index.html",{'name':n1, 'dep':n2})



    
    return render(request,"index.html")
    