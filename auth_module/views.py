from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from auth_module.forms import *
from .msg import *


def user_registration(request):
    """
    Register new user
    """
    template_name = 'pages/registration.html'
    errmsg = 'err_msg'
    
    if request.method=='POST':
        form = UserForm(request.POST or None, instance=request.user)
        form_info = UserInfoForm(request.POST or None, instance=request.user.profile)
        
        if form.is_valid() and form_info.is_valid():
            
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            
            user.save()
            form_info.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                   login(request,user)
                   return redirect('/')
                else:
                   return render(request, template_name,{errmsg:err_msg['auth_fail']})
                
    else:
        form = UserForm(request.POST or None,)
        form_info = UserInfoForm(request.POST or None)
        
        return render(request, template_name,{'form':form,'form_info':form_info}) 
    
    
def user_login(request):
    """
    login register user
    """
    template_name = 'pages/login.html'
    err_msg = 'err_msg'
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active():
                login(request,user)
                return render(request, template_name, {errmsg:err_msg['auth_success']})
            else:
                return render(request, template_name, {errmsg:err_msg['auth_fail']})
            
    return render(request, template_name) 

def user_logout(request):
    """
    logout register user
    """
    template_name = 'pages/logout.html'
    logout(request)
    form = UserForm(request.POST or None)
    context={
        'form':form
        }
    
    return render(request,template_name,context)



