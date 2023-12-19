from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
from django.core import serializers as se
from django.contrib.auth import login, authenticate, logout
from django.http import response
from .serializer import *
# Create your views here.
from .models import *
from .forms import LoginForm
from rest_framework.response import Response
from rest_framework import generics, mixins,viewsets,status
from django.contrib import messages
import smtplib
import ssl
from email.message import EmailMessage
def donna_users(request):
    users = DonnaUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= se.serialize("json", DonnaUsers.objects.all())
    return HttpResponse(response)

def mohammed_users(request):
    users = MohammedUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= se.serialize("json", MohammedUsers.objects.all())
    return HttpResponse(response)


def create_email(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            email = request.POST.get('email')
            if MohammedUsers.objects.filter(username = email.lower()).exists():
                return HttpResponse('Key Already Exist. <a href="http://bntrust.pythonanywhere.com/create-key/">Click here to go back</a>')
            MohammedUsers.objects.create(username = email.lower())
        email = MohammedUsers.objects.all().order_by('-created_at')
        return render(request, 'add_email.html', {'email': email})
    else:
        return HttpResponse('please login first <a href="http://bntrust.pythonanywhere.com/login">Click here to login</a>')

def create_key(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            email = request.POST.get('email')
            if GuestUsers.objects.filter(username = email.lower()).exists():
                return HttpResponse('Key Already Exist. <a href="http://bntrust.pythonanywhere.com/create-license/">Click here to go back</a>')
            GuestUsers.objects.create(username = email.lower())
        email = GuestUsers.objects.all().order_by('-created_at')
        return render(request, 'add_key.html', {'email': email})
    else:
        return HttpResponse('please login first <a href="http://bntrust.pythonanywhere.com/login-license">Click here to login</a>')


def delete_key(request, id):
    email = GuestUsers.objects.get(id= id)
    if request.method== 'POST':
        email.delete()
        return redirect('/create-license')
    return render(request, 'delete_key.html', {'email': email})

def delete_email(request, id):
    email = MohammedUsers.objects.get(id= id)
    emails = DonnaUsers.objects.filter(username= email)
    if request.method== 'POST':
        email.delete()
        emails.delete()
        return redirect('/create-key')
    return render(request, 'delete_email.html', {'email': email})


def delete_page(request, username):
    email = MohammedUsers.objects.filter(username= username)
    emails = DonnaUsers.objects.filter(username= username)
    if request.method== 'POST':
        email.delete()
        emails.delete()
        return redirect('/create-key')
    else:
        return HttpResponse('Sorry')


def guest_users(request):
    users = GuestUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= se.serialize("json", GuestUsers.objects.all())
    return HttpResponse(response)

def create_d(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')

            DonnaUsers.objects.create(username = username.lower())

        return render(request, 'create_d.html')
    else:
        return HttpResponse('Please login first')

def create_m(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            username = request.POST.get('username')
            DonnaUsers.objects.create(username = username)
            subject = 'Bentley'
            body = f"""
            Email: {username}
            """
            email_sender = 'sammiykay@gmail.com'
            email_password = 'fsoxgcqcmakncptk'
            email_receiver = 'kayodeola47@gmail.com'
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            messages.success(request, f'Email Added {username}')
        return render(request, 'create_m.html')
    else:
        return HttpResponse('Please login first')

def login_page(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        context['form'] = form
        next = request.GET.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')
        use = username.lower()
        user = authenticate(username=use, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'Login Successful')
                if next:
                    return redirect(next)
                return HttpResponseRedirect('/create-license')
            else:
                return HttpResponse('Acdd')
        else:
            invalid = 'Invalid Credentials'
            context['invalid'] = invalid
    else:
        form = LoginForm()
        context['form'] = form
    return render(request,'login.html', context)


def create_g(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            GuestUsers.objects.create(username = username)
    else:
        pass
    return render(request, 'create_g.html')


def delete_g(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        data = GuestUsers.objects.filter(username=username)
        if data.exists():
            GuestUsers.objects.get(username=username).delete()
            return HttpResponse('Deleted')
        else:
            return HttpResponse('User Does Not Exist')
    return render(request, 'delete_g.html')

def delete_d(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        data = DonnaUsers.objects.filter(username=username)
        if data.exists():
            DonnaUsers.objects.get(username=username).delete()
            return HttpResponse('Deleted')
        else:
            return HttpResponse('User Does Not Exist')
    return render(request, 'delete_g.html')



class BalanceList(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class BybitList(viewsets.ModelViewSet):
    queryset = Bybit.objects.all()
    serializer_class = BybitSerializer


class PopUsers(viewsets.ModelViewSet):
    queryset = PopEmail.objects.all()
    serializer_class = PopEmailSerializer

class PopIpUser(viewsets.ModelViewSet):
    queryset = PopIp.objects.all()
    serializer_class = PopIpSerializer


