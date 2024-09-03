from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item,Driver
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DriverRegistrationForm
from django.contrib import messages




def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def home(request):
    return render(request, "home.html")



def edit_item(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, "edit.html", {"items": items})


@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.price = request.POST.get("price")
        item.save()
        return redirect("home2")
    return render(request, "update.html", {"item": item})

def add_item(request):
    user = request.user.username
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        created_by = User.objects.get(username=user)
        if Item.objects.filter(name=name).exists():
            messages.error(request, "Item already exists")
        else:
            item = Item.objects.create(name=name, description=description, price=price, created_by=created_by)
            item.save()
            return redirect("home2")
    return render(request, "add.html")

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("edit")



def driver(request):
    return render(request,"driver2.html")   

def vehicle(request):
    return render(request,"vehicle.html")   

def category(request):
    return render(request,"category.html")   

def trip(request):
    return render(request,"trip.html")   

def point(request):
    return render(request,"creditpoint.html")   

def password(request):
    return render(request,"password.html")  

def home2(request):
   items = Item.objects.all()
   return render(request, "home2.html", {"items": items}) 
   
# List all drivers
def add_d(request):
    return render(request,"driver_table.html")

def driver_registration(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver registered successfully.')
            return redirect('home')  # Redirect to a success page or home page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DriverRegistrationForm()

    return render(request,'driver_table.html', {'form': form})
    