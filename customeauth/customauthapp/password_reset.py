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


def password_reset(request):
    form = ResetPasswordForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        User = get_user_model()

        try:
            user = User.objects.get(email=email)

            # Assign a new UUID for reset
            user.uniqueId = uuid.uuid4()
            user.save()
            print(user.pk)
            # Compose reset link and email
            reset_link = f"http://127.0.0.1:8000/new-password/{user.uniqueId}/user/{user.email}/user_is/{user.pk}"
            subject = "Reset Your Password"
            html_content = f"""
                <p>Hello {user.first_name},</p>
                <p>You requested a password reset. Click the link below:</p>
                <p><a href="{reset_link}">Reset Password</a></p>
                <p>If this wasn't you, just ignore this email.</p>
            """

        except User.DoesNotExist:
            # form.add_error('email', 'No user with this email exists.')
            messages.error(request, 'No user with this email exists.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        try:
            email_message = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="chikanwazuo.com",
                to=[email],
            )
            email_message.content_subtype = "html"
            email_message.send()
            
            # Redirect to a success page or render a success message
            messages.success(request, 'A password reset link has been sent to your email.')
            return redirect('password_reset')
        except Exception as e:
            messages.error(request, 'Failed to send password reset email. Please try again later.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'cutomauthapp/password_reset.html', {"form": form})
