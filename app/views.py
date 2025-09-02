from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Doctor, Patient
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_page(request):
    return render(request,'login.html')

CustomUser = get_user_model()

def register_user(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("puser")
        password = request.POST.get("ppassword")
        confirm_password = request.POST.get("cpass")
        address = request.POST.get("paddress")
        role = request.POST.get("role")   
        profile_picture = request.FILES.get("pimage")


        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect(login_page)

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect(login_page)

     
        user = CustomUser.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password,
            role=role,
            address=address,
            profile_picture=profile_picture
        )
        if role == "patient":
            Patient.objects.create(user=user)
        elif role == "doctor":
            Doctor.objects.create(user=user)

        messages.success(request, f"{role.capitalize()} account created successfully!")
        return redirect(login_page)   


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == "patient":
                return redirect("patient_dashboard")
            elif user.role == "doctor":
                return redirect("doctor_dashboard")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login_page")

    return render(request, "login.html")

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
     return render(request, 'doctor_dashbaord.html')

def logout_user(request):
    logout(request)
    return redirect('login_page')

