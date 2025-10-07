from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile

# 🧾 إنشاء حساب جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا.")
            return redirect("accounts:register")

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, phone=phone, address=address, city=city)

        messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك الآن تسجيل الدخول.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")


# 🔐 تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح.")
            return redirect("/")
        else:
            messages.error(request, "بيانات الدخول غير صحيحة.")
            return redirect("accounts:login")

    return render(request, "accounts/login.html")
