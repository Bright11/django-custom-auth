from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import EmailLoginForm, RegisterForm,ResetPasswordForm,NewPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.core.mail import EmailMessage
import uuid
from django.contrib import messages
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
            if user.is_superuser:
                return redirect('admindashboard')
            else:
                return redirect('user_dashboard')
          
    return render(request, 'cutomauthapp/login.html', {'form':form})



# Register 
def Register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password']) #hash password
        user.save()
        login(request, user) #Auto login after registeration
        if user.is_superuser:
            return redirect('admindashboard')
        else:
            return redirect('user_dashboard')
        
    context={'title':"Register page",'form':form}
    return render(request, 'cutomauthapp/register.html',context)

@login_required
def user_dashboard_view(request):
    if request.user.is_superuser:
        return redirect('admindashboard')
    return render(request,'cutomauthapp/user_dashboard.html')



@login_required
def dashboard_superuser(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    return render(request, 'cutomauthapp/dashboard.html')

def homepage(request):
    return render(request,'cutomauthapp/home.html')




@login_required
def admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    
    return render(request, 'cutomauthapp/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')



