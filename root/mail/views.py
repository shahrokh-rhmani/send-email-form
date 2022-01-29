from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings

def sendmail(request):
    message_sent = False

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'send an email'
            message = cd['message']
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            message_sent = True

    else:
        form = EmailForm()

    context = {
        'form': form,
        'messageSent':message_sent,
    }

    return render(request, 'index.html', context)
