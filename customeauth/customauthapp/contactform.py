from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from .forms import ContactForm

def contactform_view(request):
    form=ContactForm(request.POST or None)
    
    if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message=form.cleaned_data['message']
        # Process the contact form data
        html_message = render_to_string('cutomauthapp/contact_email.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })
        plain_message = strip_tags(html_message)
        # send the email
        try:
            email_message =EmailMessage(
                subject=subject,
                body=html_message,
                from_email='chikanwazuo@gmail.com',
                to=[email]
            )
            email_message.content_subtype='html' #send as HTML
            email_message.send()
            messages.success(request, "Thank you for your message, we will respond to you as soon as possible")
        except Exception as e:
            messages.error(request, "Something went wrong while sending your message")
            return redirect(request.META.get('HTTP_REFERER', '/'))
   
       
    return render(request, 'cutomauthapp/contact_form.html', {'form': form})
    