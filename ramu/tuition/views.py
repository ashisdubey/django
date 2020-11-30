from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import NewFeedbackForm, NewEnquiryForm
from . models import Feedback,Enquiry

#from .models import Flight, Passenger

# Create your views here.
def index(request):
    #return HttpResponse("Flights");
    if request.user.is_authenticated:
        context={
            "loggedin":True
        }
    else:
        context={
        "loggedin":False
        }
    return render(request, "tuition/index.html")

def curriculum(request):
    return render(request,"tuition/curriculum.html")

def methodology(request):
    return render(request,"tuition/methodology.html")

def about(request):
    return render(request,"tuition/about.html")

def mission(request):
    return render(request,"tuition/mission.html")

def feedback(request):
    return render(request,"tuition/feedback.html")

def enquiry(request):
    return render(request,"tuition/enquiry.html")

def post_feedback(request):
    if request.method == 'POST':
        form = NewFeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback()
            feedback.name = form.cleaned_data['name']
            feedback.phone = form.cleaned_data['phone']
            feedback.email = form.cleaned_data['email']
            feedback.feedback = form.cleaned_data['feedback']
            feedback.save()
    return render(request,"tuition/feedback.html",{"message":"Feedback submitted successfully!"})

def post_enquiry(request):
    if request.method == 'POST':
        form = NewEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = Enquiry()
            enquiry.name = form.cleaned_data['name']
            enquiry.phone = form.cleaned_data['phone']
            enquiry.email = form.cleaned_data['email']
            enquiry.enquiry = form.cleaned_data['enquiry']
            enquiry.save()
    return render(request,"tuition/enquiry.html",{"message":"Enquiry submitted successfully. We will get back soon!"})

# def logout(request):
#     return render(request,"tuition/enquiry.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
        if user is not None:
            form = LoginForm()
            login(request, user)
    return render(request,"tuition/login.html")

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'tuition/index.html')
    context['form']=form
    return render(request,'tuition/sign_up.html',context)
