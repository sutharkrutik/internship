from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models


# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],
                                 password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'dashboard.html')
        else:
            return HttpResponse("invalid username")
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])
                User.objects.get(first_name=request.POST['first_name'])
                User.objects.get(last_name=request.POST['last_name'])
                User.objects.get(email=request.POST['email'])


                return render(request,'register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                first_name=request.POST.get('first_name'),
                                                last_name=request.POST.get('last_name'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'))

                auth.login(request,user)
                return HttpResponse("Registered")
        else:
                return render(request,'register.html',{'error':'password not match'})

    else:
        return render(request,'register.html')

def reg_edit(request,id):
    abc = models.reg_insert.objects.get(id=id)
    return render(request,'register.html',{'object': abc})

def reg_update(request,id):
    xyz = models.reg_insert.objects.get(id=id)
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    xyz.username = username
    xyz.first_name = first_name
    xyz.last_name = last_name
    xyz.email = email
    xyz.password1 = password1
    xyz.password2 = password2

    xyz.save()
    return redirect(profile)

def forgotpass(request):
    return render(request,'forgotpass.html')

def newpassOTP(request):
    return render(request,'newpassOTP.html')

def newpass(request):
    return render(request,'newpass.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')

def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')


def income(request):
        if request.method == "POST":
            if request.POST.get('date') and request.POST.get('category') and request.POST.get('item') and \
                    request.POST.get('price'):
                a = models.addincome()
                a.date = request.POST.get('date')
                a.category = request.POST.get('category')
                a.item = request.POST.get('item')
                a.price = request.POST.get('price')
                a.user = request.user


                a.save()
                return HttpResponse("Income is added")
            else:
                return HttpResponse("<h1>Error</h1>")
        else:
            return render(request,'income.html')

def expense(request):
    if request.method == "POST":
        if request.POST.get('date') and request.POST.get('category') and request.POST.get('item') and \
                request.POST.get('price'):
            b = models.addexpense()
            b.date = request.POST.get('date')
            b.category = request.POST.get('category')
            b.item = request.POST.get('item')
            b.price = request.POST.get('price')
            b.user = request.user

            b.save()
            return HttpResponse("Expense is added")
        else:
            return HttpResponse("<h1>Error</h1>")
    else:
        return render(request,'expense.html')

def manage_income(request):
    data = models.addincome.objects.filter(user=request.user)
    return render(request,'manage_income.html',{'M_I':data})

def manage_expense(request):
    data1 = models.addexpense.objects.filter(user=request.user)
    return render(request,'manage_expense.html',{'M_E':data1})

def edit_income(request,id):
    i = models.addincome.objects.get(id=id)
    return render(request,'income_edit.html',{'object':i})

def update_income(request,id):
    i = models.addincome.objects.get(id=id)
    date = request.POST['date']
    category = request.POST['category']
    item = request.POST['item']
    price = request.POST['price']

    i.date = date
    i.category = category
    i.item = item
    i.price = price

    i.save()
    return redirect(manage_income)

def delete_income(request,pk):
    models.addincome.objects.filter(id=pk).delete()
    return redirect(manage_income)


def edit_expense(request,id):
    e = models.addexpense.objects.get(id=id)
    return render(request,'expense_edit.html',{'object':e})

def update_expense(request,id):
    e = models.addexpense.objects.get(id=id)
    date = request.POST['date']
    category = request.POST['category']
    item = request.POST['item']
    price = request.POST['price']

    e.date = date
    e.category = category
    e.item = item
    e.price = price

    e.save()
    return redirect(manage_expense)

def delete_expense(request,pk):
    models.addexpense.objects.filter(id=pk).delete()
    return redirect(manage_expense)

def logout(request):
    auth.logout(request)
    return redirect(home)