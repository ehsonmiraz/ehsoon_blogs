from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup_view(request):

    if(request.method=='POST'):
        form = UserCreationForm(data=request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form': form});

def login_view(request):
    if request.user.is_authenticated :
        return redirect('articles:list')

    if request.method=='POST' :
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            user = form.get_user()
            login(request, user)
            if request.POST.get('next') :
                return redirect(request.POST.get('next'))
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form})

def logout_view(request):

    if(request.method=='POST'):
        logout(request)

    return redirect('articles:list')


