from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf.urls.static import static
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from app1.models import Contact
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail
from django.contrib import messages
def home(request):
    return render(request,'course_details.html')
def fc(request):
    return render(request,'freecourse.html')
def eb(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        query=Contact(name=name,email=email,message=message)
        query.save()
         
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {name}',f'UserEmail : {email}\nUserPhoneNumber :\n\n\n QUERY : {message}',from_email,['evabirami17@gmail.com','evabirami17@gmail.com'],connection=connection)
        email_client=mail.EmailMessage('ExpressEat ','Thanks For Reaching us',from_email,[email],connection=connection)

        connection.send_messages([email_message,email_client])
        connection.close()
        messages.info(request,"Thanks for Contacting Us")
        return redirect("Ebook.html")
    return render(request,'Ebook.html')
def eb1(request):
    return render(request,'index.html')
def eb2(request):
    return render(request,'program_details.html')
def eb3(request):
    return render(request,'programminghub.html')
def eb4(request):
    if request.method=="POST":
        username=request.POST.get("username")  
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmPassword")
        if password !=confirmpassword:
           messages.warning(request,"Password is Incorrect")
           return redirect("signup.html")
        try:
            if User.objects.get(username=username):
                messages.info(request,"Username is Taken")
                return redirect("signup.html")
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is Taken")
                return redirect("signup.html")
        except:
            pass
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"signup success Please Login")
        return redirect("login.html")
    return render(request,'signup.html')
def eb5(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            
            messages.success(request,"Login Success")
            return redirect("/Tech-World/index.html")
        else:
            messages.error(request,"Invalid Credintials")
            return redirect("/Tech-World/login.html")
    return render(request,'login.html')