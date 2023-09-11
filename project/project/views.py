from django.shortcuts import render


def home(request):
    if request.method=="POST":
        n1=request.POST.get("n")
        n2=request.POST.get("d")
        return render(request,"index.html",{'name':n1,'dep':n2})



    
    return render(request,"index.html")
    