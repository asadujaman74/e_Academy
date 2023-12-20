from django.http import HttpResponse
from django.shortcuts import render,redirect
from iacademy.emailBackend import emailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from iacademy.models import CustomUser

def BASE(request):
    return render(request,'base.html')


def user_register (request):
    return render(request,'register.html')

def register_student(request):
    return render(request, 'register_student.html')

def register_staff(request):
    return render(request,'register_staff')


def LOGIN(request):
    return render(request, 'login.html')

def user_login(request):

    if request.method == "POST":
        user = emailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),
                                         
                                        )
        
        if user != None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return HttpResponse('This is Student page')
            else:
                #Message
                messages.error(request, 'email and password are invalid!')
                return redirect('login')
        else:
            #Message
            messages.error(request, 'email and password are invalid!')
            return redirect('login')


#Logout Function
def user_logout(request):
    logout(request)
    return redirect('login')




# Update Profile Session
@login_required(login_url='/')
def update_profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    user_info={
        "user": user,
    }
    return render(request, 'profile.html',user_info)

@login_required(login_url='/')
def profile_update(request):
    if request.method == 'POST':
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        # email= request.POST.get('email')
        # username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name  
            customuser.last_name = last_name  
            # customuser.username = username 

            if password != None and password != "":
                customuser.set_password(password)

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Info Updated Sucessfully !')
            return redirect('profile')

        except:
            messages.error(request,'Your Info Not Updated !')

    return render (request, 'profile.html')
        
    
