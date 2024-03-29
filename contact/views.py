from django.shortcuts import render, redirect
from. forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("Tipo de Petición:{}", format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffetiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ["kedfygo@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+'?OK')
            except:
                #Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')

      
    return render(request, "contact/contact.html", {'form': ContactForm})

