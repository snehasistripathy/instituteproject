from django.shortcuts import render,redirect, HttpResponse
from .models import courses,feedbackData
from .forms import registationform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime as dt
date1=dt.datetime.now()
@login_required(login_url='login')
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='login')
def contactpage(request):
    return render(request,'contactpage.html')

@login_required(login_url='login')
def servicepage(request):
    cours =courses.objects.all()
    return render(request,'service.html',{'courses':cours})

@login_required(login_url='login')
def feedbackpage(request):
    if request.method == 'GET':
        feedbacks=feedbackData.objects.all().order_by('-id')
        return render(request,'feedback.html',{'feedbacks':feedbacks})
    else:
        feedbackData(
            content=request.POST['con'],
            date=date1
        ).save()
        feedbacks=feedbackData.objects.all().order_by('-id')
        return render(request,'feedback.html',{'feedbacks':feedbacks})
 
@login_required(login_url='login')
def gallerypage(request):
    return render(request,'gallery.html')
def loginpage(request):
    if request.method=='GET':
        return render(request,'loginpage.html')
    else:
        usernames = request.POST['user']
        password = request.POST['password']
        user=authenticate(username=usernames,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           return HttpResponse('invalid login')
def logoutpage(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    if request.method=='GET':
        form=registationform()
        return render(request,'registerpage.html',{'form':form})

    form= registationform(request.POST)
    if form.is_valid():
        user=form.save(commit=False)
        user=user.set_password(user.password)
        form.save()
        return redirect('login')
    else:
        return HttpResponse('invalid registration form')