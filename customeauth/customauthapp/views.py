from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import EmailLoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.
from django.http import HttpResponseForbidden

def email_login_view(request):
    form=EmailLoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'cutomauthapp/login.html', {'form':form})



# Register 
def Register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password']) #hash password
        user.save()
        login(request, user) #Auto login after registeration
        return redirect('/')
    context={'title':"Register page",'form':form}
    return render(request, 'cutomauthapp/register.html',context)

@login_required
def dashboard_view(request):
    return render(request,'cutomauthapp/dashboard.html')



@login_required
def dashboard_superuser(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    return render(request, 'cutomauthapp/dashboard.html')

def homepage(request):
    return render(request,'cutomauthapp/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')
