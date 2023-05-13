from django.contrib import messages
from django.shortcuts import render, redirect
from subscription.forms import ContactForm


def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
                # Başarılı bir şekilde gönderildiğinde bir mesaj göstermek isterseniz:
                messages.success(request, 'Mesajınız başarıyla gönderildi')
            except Exception as E:
                messages.error(request, E)
    return render(request, 'contact.html', {'form': form})
