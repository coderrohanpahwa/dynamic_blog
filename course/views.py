from django.shortcuts import render
from .forms import Contact,PostForm
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from .forms import SignUp,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Post
def index(request):
    ob=Post.objects.all()
    return render(request,'course/index.html',{'posts':ob})
def about(request):
    return render(request,'course/about.html')
def contact(request):
    if request.method=="POST":
        fm=Contact(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'We will reply you as soon as possible')
    else:
        fm=Contact()
    return render(request,'course/contact.html',{'forms':fm})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect("/dashboard/")
            else:
               messages.error(request,"You have written wrong credentials")
        fm=LoginForm()
        return render(request,'course/login.html',{'forms':fm})
    else :
        return HttpResponseRedirect('/dashboard/')
def user_signup(request):
    if request.method=="POST":
        fm=SignUp(request.POST)
        if fm.is_valid():
            user=fm.save()
            messages.success(request,"You have successfully signed up . You can login now")
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        fm=SignUp()
    return render(request,'course/signup.html',{'forms':fm})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def dashboard(request):
    if request.user.is_authenticated:
        obj=Post.objects.all()

        return render(request,'course/dashboard.html', {'name':request.user,'data':obj})
    else:
        return HttpResponseRedirect('/login')
def add(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Your post has been successfully uploaded.")
                fm=PostForm()
        else:
            fm=PostForm()
        return render(request,'course/add.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')
def delete(request,my_id):
    if request.user.is_authenticated:
            obj=Post.objects.get(pk=my_id)
            obj.delete()
            return HttpResponseRedirect('/dashboard/')

    else:
        return HttpResponseRedirect('/login/')
def update(request,my_id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=my_id)
            fm=PostForm(request.POST,instance=pi)

            if fm.is_valid():
                fm.save()
                messages.success(request,"You have successfully updated Post")
        else:
            pi=Post.objects.get(pk=my_id)
            fm=PostForm(instance=pi)
        return render(request,'course/update.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')
