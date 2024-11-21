from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from .forms import EquipmentForm
from .models import Equipment

# Create your views here.

def HomePage(request):

    return render(request, 'home.html')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')

        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken! Please choose another.")
            return redirect('signup')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
                return redirect('signup')


        if len(pass1) < 8:
                messages.error(request, "Password must be at least 8 characters long!")
                return redirect('signup')

        if not re.search(r'[A-Z]', pass1):
                messages.error(request, "Password must contain at least one uppercase letter!")
                return redirect('signup')

        if not re.search(r'[a-z]', pass1):
                messages.error(request, "Password must contain at least one lowercase letter!")
                return redirect('signup')

        if not re.search(r'[0-9]', pass1):
                messages.error(request, "Password must contain at least one digit!")
                return redirect('signup')

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
                messages.error(request, "Password must contain at least one special character!")
                return redirect('signup')

        # If all validations pass, create the user
        try:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, "An error occurred: " + str(e))
            return redirect('signup')

    return render(request, 'signup.html')



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect password or username")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
def list_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.user = request.user  # Assign the logged-in user
            equipment.save()
            return redirect('home')  # Redirect to the home page after submission
    else:
        form = EquipmentForm()
    return render(request, 'list_equipment.html', {'form': form})

def listings(request, category , ):
    # Filter equipment by the selected category

    equipment_list = Equipment.objects.filter(category=category)
    return render(request, 'listings.html', {
        'equipment_list': equipment_list,
        'category': category
    })

def product(request, product_id):
    equipment = get_object_or_404(Equipment, id=product_id)
    return render(request, 'product.html', {'equipment': equipment})
def contact(request) :
     return render(request , 'contact.html')