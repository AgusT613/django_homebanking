from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(f"/clientes/{user.pk}")
    else:
        return render(request, "login/index.html")


def logoutPage(request):
    logout(request)
    return redirect("/login")
