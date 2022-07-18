from django.shortcuts import render, redirect
from .forms import contact_us_name, contact_us_email, contact_us_subject, contact_us_message
from django.contrib import messages
from blog.models import Link



def contact(request):
    if request.method == 'POST':
        form_name = contact_us_name(request.POST)
        form_email = contact_us_email(request.POST)
        form_subject = contact_us_subject(request.POST)
        form_message = contact_us_message(request.POST)
        if form_name.is_valid and form_email.is_valid and form_subject.is_valid and form_message.is_valid():
            form_name.save()
            form_email.save()
            form_subject.save()
            form_message.save()
            
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your message has been sent successfully, we\'ll get back to you asap with the info provided. Thanks !')
            return redirect('contact')
    else:
        form_name = contact_us_name()
        form_email = contact_us_email()
        form_subject = contact_us_subject()
        form_message = contact_us_message()
    
    form_context = {
        'title': 'Contact',
        'form_name': form_name,
        'form_email': form_email,
        'form_subject': form_subject,
        'form_message': form_message,
        'links': Link.objects.all()
    }
    return render(request, 'contact/contact.html', form_context)

def about_us(request):
    form_context = {
        'title': 'About Us',
        'links': Link.objects.all()
    }
    return render(request, 'contact/about.html', form_context)