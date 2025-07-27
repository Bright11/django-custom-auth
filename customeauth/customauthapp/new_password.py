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



def new_password(request, unique_id, email, pk):
    form=NewPasswordForm()
    User = get_user_model()
    try:
        user = User.objects.get(uniqueId=unique_id, email=email, pk=pk)
    except User.DoesNotExist:
        messages.error(request, 'Invalid reset link.')
        return redirect('password_reset')

    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            # form.add_error(None, 'Passwords do not match.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        

        user.set_password(new_password)
        user.uniqueId ="" # uuid.uuid4()  # Reset uniqueId after password change
        user.save()
        messages.success(request, 'Your password has been successfully reset.')
        return redirect('login')

    return render(request, 'cutomauthapp/new_password.html', {'user': user,'form':form})