from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Donate
from .models import Fund
from .models import Feedback
from .models import Don
from marketing.forms import EmailSignupForm
from .models import Total_Donate

def index(request) :
    #  q=Total_Donate.objects.all()
     sum=0
    #  for q1 in q :
    #      sum+=q1.amount
     form=EmailSignupForm()
     context={
         'form':form,
         'sum':sum
     }
     return render(request,'index.html',context)


def login(request) :
     if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
          # by writing this we are checking whether the entered username and password are of the same user or not 
         user = auth.authenticate(username=username,password=password)
         if user is not None :
             request.session['member_id'] = user.id
             auth.login(request,user)
             return redirect('/')
         else :
             messages.info(request,'invalid credentials')
             return redirect('login')
            
     else :
         return render(request,"login.html")



def logout(request) :
    auth.logout(request)
    request.session['member_id'] = 0
    return redirect('/')



def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # by writing this condition we are checking that if password1 and password2 are equal or not 
        if password1==password2 :
            # by writing this condition we are checking that if this username is already registered or not
            if User.objects.filter(username=username).exists() :
               messages.info(request,'Username Taken')
               return redirect('register')
            # by writing this condition we are checking that if this email is already registered or not
            elif User.objects.filter(email=email).exists() :
               messages.info(request,'email taken already')
               return redirect('register')
            else :
                user =User.objects.create_user(username=username,email=email,password=password1)
                # by writing this only we are hitting the database to store the information
                user.save()
                print('user created')
                return redirect('login') 
        else :
            messages.info(request,'password not matching')
            return redirect('register')
        return('/')  
    else :
        return render(request,'reg.html')


def donate(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        organization= request.POST['organization']
        email = request.POST['email']
        phonenumber= request.POST['phonenumber']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        amount=request.POST['amount']
        comments=request.POST['comments']
        donation = Donate(fname=fname,lname=lname,organization=organization,email=email,phonenumber=phonenumber,address1=address1,address2=address2,city=city,state=state,amount=amount,comments=comments)
        donation.save()
        total_donate=Total_Donate(amount=amount)
        total_donate.save()
        return redirect('/')
    return render(request,"form.html")

# this function booking is to connect our app first to the file about.html
def about(request) :
    return render(request,"about.html")  
@login_required(login_url='login')
def news(request) :
    return render(request,"newsAndParticipate.html")  

# by writing we are applying the condition that if user is logged in then only call feedback function
@login_required(login_url='login')
def feedback(request) :
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    feed = Feedback(name=name,email=email,subject=subject,message=message)
    # by writing this only we are hitting the database to store the information
    feed.save() 
    return redirect('index')


@login_required(login_url='login')
def participate(request):
    return render(request,'participate.html')


@login_required(login_url='login')
def events(request):
    return render(request,'events.html')


def don(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phn= request.POST['phn']
        city=request.POST['city']
        state=request.POST['state']
        zp=request.POST['zp']
        dono = Don(name=name,email=email,phn=phn,address=address,city=city,state=state,zp=zp)
        dono.save()
        return redirect('/')
    return render(request,'monthlyDonationForm.html')


@login_required(login_url='login')
def fund(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phn= request.POST['phn']
        city=request.POST['city']
        state=request.POST['state']
        zp=request.POST['zp']
        fundation = Fund(name=name,email=email,phn=phn,address=address,city=city,state=state,zp=zp)
        fundation.save()
        return redirect('/')
    return render(request,'fundraiserForm.html')