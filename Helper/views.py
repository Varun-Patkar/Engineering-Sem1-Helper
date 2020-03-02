from django.shortcuts import render,redirect
from django.contrib import messages
from .models import MCQ,PDF,Announcement,Feedback
from django.contrib.auth.decorators import login_required
# Create your views here.
def feedback(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        text=request.POST['message']
        messages.success(request,f'Your Feedback has been recieved!')
        return redirect("/")
    else:
        return render(request,'feed-back.html')
def aboutus(request):
    return render(request,'aboutus.html')
def home(request):
    return render(request,'home1.html',{'announcements':Announcement.objects.all()})
@login_required
def mcq(request):
    return render(request,'quiz.html',{'mcqs':MCQ.objects.all()})
@login_required
def maths(request):
    return render(request,'subjects/subjects_maths.html',{'iat1':PDF.objects.filter(subject='MATHS', types='IAT1'),'iat2':PDF.objects.filter(subject='MATHS', types='IAT2'),'uni':PDF.objects.filter(subject='MATHS', types='UNI'),'prelim':PDF.objects.filter(subject='MATHS', types='PRELIM'),'tut':PDF.objects.filter(subject='MATHS', types='TUTORIAL'),'tt':PDF.objects.filter(subject='MATHS', types='TT'),'subject':'MATHS','announcements':Announcement.objects.all()})
@login_required
def bee(request):
    return render(request,'subjects/subjects_bee.html',{'iat1':PDF.objects.filter(subject='BEE', types='IAT1'),'iat2':PDF.objects.filter(subject='BEE', types='IAT2'),'uni':PDF.objects.filter(subject='BEE', types='UNI'),'prelim':PDF.objects.filter(subject='BEE', types='PRELIM'),'tut':PDF.objects.filter(subject='BEE', types='TUTORIAL'),'tt':PDF.objects.filter(subject='BEE', types='TT'),'subject':'BEE','announcements':Announcement.objects.all()})
@login_required
def chemistry(request):
    return render(request,'subjects/subjects_chemistry.html',{'iat1':PDF.objects.filter(subject='CHEMISTRY', types='IAT1'),'iat2':PDF.objects.filter(subject='CHEMISTRY', types='IAT2'),'uni':PDF.objects.filter(subject='CHEMISTRY', types='UNI'),'prelim':PDF.objects.filter(subject='CHEMISTRY', types='PRELIM'),'tut':PDF.objects.filter(subject='CHEMISTYRY', types='TUTORIAL'),'tt':PDF.objects.filter(subject='CHEMISTRY', types='TT'),'subject':'CHEMISTRY','announcements':Announcement.objects.all()})
@login_required
def physics(request):
    return render(request,'subjects/subjects_physics.html',{'iat1':PDF.objects.filter(subject='PHYSICS', types='IAT1'),'iat2':PDF.objects.filter(subject='PHYSICS', types='IAT2'),'uni':PDF.objects.filter(subject='PHYSICS', types='UNI'),'prelim':PDF.objects.filter(subject='PHYSICS', types='PRELIM'),'tut':PDF.objects.filter(subject='PHYSICS', types='TUTORIAL'),'tt':PDF.objects.filter(subject='PHYSICS', types='TT'),'subject':'PHYSICS','announcements':Announcement.objects.all()})
@login_required
def mechanics(request):
    return render(request,'subjects/subjects_mechanics.html',{'iat1':PDF.objects.filter(subject='MECHANICS', types='IAT1'),'iat2':PDF.objects.filter(subject='MECHANICS', types='IAT2'),'uni':PDF.objects.filter(subject='MECHANICS', types='UNI'),'prelim':PDF.objects.filter(subject='MECHANICS', types='PRELIM'),'tut':PDF.objects.filter(subject='MECHANICS', types='TUTORIAL'),'tt':PDF.objects.filter(subject='MECHANICS', types='TT'),'subject':'MECHANICS','announcements':Announcement.objects.all()})
