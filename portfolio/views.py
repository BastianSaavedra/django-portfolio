from django.shortcuts import render, redirect
from .models import Home, CvDownload , Profile, Project, Category, Skills, Social, Certificates, Flag
import os
from django.conf import settings
from django.core.mail import send_mail

from django.contrib import messages

from django.http import HttpResponse

def contact(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message'] + " " + request.POST['email']
        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["bastiansaavedra55@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "El email ha sido enviado!")

        return redirect(to="index")
    
    return render(request, "portfolio/sent_mail.html",)

def index(request):
    # home
    home = Home.objects.latest('updated')

    # About
    profile = Profile.objects.latest('updated')
    socials = Social.objects.all()
    
    # CV Document
    file = CvDownload.objects.all()
    
    # My project
    projects = Project.objects.all()

    # Skills
    categories = Category.objects.all()

    # Certificates
    certificates = Certificates.objects.all()

    # Flags
    flags = Flag.objects.all()


    return render(
        request,
        'index.html',
        context={
            'home':home,
            'profile':profile,
            'file': file,
            'projects':projects,
            'socials':socials,
            'categories':categories,
            'certificates': certificates,
            'flags':flags,
        }
    )

def download(request, path, pk):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            files = ('application/cv_portfolio', 'applications/projects')
            response = HTTPResponse(fh.read(), content_type=files)
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response

    raise Http404
