from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def login_request(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"] 

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect("Home")

        else: 
            return render(request,"account/login.html",{"error":"error"})

    return render(request,"account/login.html")


def register_request(request):
    
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password == repassword :
            if User.objects.filter(username = username).exists():
                return render(request,"account/register.html",{"error":"error"})

            else:
                if User.objects.filter(email = email).exists():
                    return render(request,"account/register.html",{"error":"error"})

                else:
                    user = User.objects.create_user(username=username, password=password, firstname=firstname, 
                    lastname=lastname, email=email)

                    user.save()

                    return redirect("Login")

        else:
            return render(request, "account/register.html",{"error":"error"})

    return render(request,"account/register.html")


def logout_request(request):

    logout(request)
    return render("Home")




