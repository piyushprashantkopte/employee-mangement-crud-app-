from django.shortcuts import redirect,render
from myapp.models import Employees

def index(request):
    emp=Employees.objects.all()
    data={
        'emp':emp
    }
    
    return render(request,"index.html",data)

def create(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        en=Employees(name=name,email=email,address=address,phone=phone)
        en.save()
        return redirect('home')
    
    return redirect('home')


def edit(request):
    emp=Employees.objects.all()
    data={
        'emp':emp
    }
    return redirect(request,'home',data)

def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        en=Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        en.save()
        return redirect('home')
    return redirect(request,"index.html")

def delete(request,id):
    emp=Employees.objects.filter(id=id)
    emp.delete()

    data={
        'emp':emp
    }
    return redirect('home')
