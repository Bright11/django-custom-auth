from django import forms 
from .models import CustomUser

class EmailLoginForm(forms.Form):
    email=forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)



# register form
class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','is_superuser','is_staff','is_active','password','confirm_password']

    # clean up email
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

    def clean(self):
       cleaned_data= super().clean()
       password=cleaned_data.get('password')
       confirm_password=cleaned_data.get('confirm_password')
       if password != confirm_password:
           raise forms.ValidationError('password do not match')
       return cleaned_data


class ResetPasswordForm(forms.Form):
    email=forms.EmailField()
    
    
class NewPasswordForm(forms.Form):
    newpassword=forms.EmailField(widget=forms.PasswordInput)
    confirm_password=forms.EmailField(widget=forms.PasswordInput)
    
    
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=200)
    message=forms.CharField(widget=forms.Textarea, max_length=500)
    
    
   