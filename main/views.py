from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

from main.models import News, Gallery, Gallery_Category, News_Category
from main.decorators import check_recaptcha
from main.forms import ContactForm

def index(request):

    latest_news = News.objects.filter(status=1).order_by('-updated_on')
    
    context = {
        'latest_news':latest_news 
    }

    return render(request, "main/index.html", context)

def about(request):
    return render(request, "main/about.html")

def admissions(request):
    return render(request, "main/admissions.html")

def academics(request):
    return render(request, "main/academics.html")

def gallery(request):
    
    items = Gallery.objects.filter(status=1).order_by('-updated_on')
    categories = Gallery_Category.objects.all()

    context = {
        'items': items,
        'categories':categories
    }

    return render(request, "main/gallery.html", context)

class NewsView(ListView):
    model = News
    queryset = News.objects.filter(status=1).order_by('-updated_on')
    context_object_name = 'news'
    template_name = 'main/news.html'
    paginate_by = 12

@check_recaptcha
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid() and request.recaptcha_is_valid:
            subject = "Webstite Enquiry"
            body = {
            'full_name': 'Name: ' + contact_form.cleaned_data['full_name'],
			'subject': 'Subject: ' + contact_form.cleaned_data['subject'],
            'email_address': 'Email Address: ' + contact_form.cleaned_data['email_address'],
			'message':'Message: ' + contact_form.cleaned_data['message'],
			}
            from_email = contact_form.cleaned_data['email_address']
            message = "\n".join(body.values())
            recipents = ['aislome@hotmail.com']
            try:
                send_mail(subject, message, from_email, recipents, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Thanks, We will get back to you Shortly..")
            return redirect("contact")
        else:
            messages.error(request, "Message was not sent, Please Try Again Later!")
            return redirect("contact")
            
    contact_form = ContactForm()
    site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    context = {
        'form': contact_form,
        'site_key': site_key,
    }

    return render(request, "main/contact.html", context)

def news_single(request, pk, slug):

    categories = News_Category.objects.all()
    news = News.objects.get(pk=pk, slug=slug)
    related_news = news.tags.similar_objects()

    context = {
        'news':news,
        'related_news':related_news,
        'categories':categories,
    }

    return render(request, "main/single.html", context)