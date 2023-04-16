from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            messages.success(request, "you have been logged in")
            return redirect('home')
        else:
            messages.success(request, "there was an error logging you in, please try again ")
            return redirect('home')
    else:
        return render(request, "students/index.html",)



def logout_user(request):
    logout(request)
    messages.success(request, "you are logged out")
    return redirect('home')
