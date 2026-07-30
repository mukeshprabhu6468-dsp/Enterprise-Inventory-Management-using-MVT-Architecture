from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required

def LoginForm(request):

    if request.user.is_authenticated:
        return redirect("all_customers")
    
    context = {'error': ''}

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if request.user.role == 2:
                return redirect('all_orders')
            else:
                return redirect('all_customers')
        else:
            context['error'] = 'Invalid username or password.'
            return render(request,'authentication/login.html', context)
    return render(request,'authentication/login.html', context)


def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/")
def Signup(request):
    context = {"error":""}
    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST["username"])
        print(user_check)
        if len(user_check) > 0:
            context = {
                "error":"User Already Exist"
            }
            return render(request,"authentication/signup.html",context)
        else:
            new_user = User(username = request.POST["username"],first_name = request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"],age = request.POST["age"],role=request.POST["role"])
            new_user.set_password(request.POST["password"])
            new_user.save()
            return redirect("/")

    return render(request,'authentication/signup.html',context)


# Create your views here.
