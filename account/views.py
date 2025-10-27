from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.



def user_panel(request):

    user = request.user

    context = {
        "user":user
    }

    return render(request,'user_core/editprofile.html',context)


def login_user(request):

    if request.user.is_authenticated:
        print(request.user)
        return redirect("/")

    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        print(username)
        print(password)

        # logout(request)


        user = authenticate(request,username=username,password=password)
        # print(user)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/account/regester")


    return render(request,'login.html',{})



def regesete_user(request):

    if request.POST:
        # print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        # password_2 =  request.POST.get("password_2")
        # if password_1 == password_2:
        #     return True

        user = authenticate(request,username=username,password=password)
        # print(user.password)
        # user = User.objects.filter(username=username).exists()

        if user is None:
            User.objects.create_user(username=username,password=password)
            # print(request.user)
            # login(user)
            return redirect("/account/login")

    return render(request,"regester.html",{})



def user_log_out(request):
   
    logout(request)

    return redirect("/")
    
   