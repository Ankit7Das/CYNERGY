from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Serviceinfo
# Create your views here.



def redirect(request):
    return render(request,'serviceman/redirect.html')



def otp(request):
    name = request.POST.get('user_name')
    email = request.POST.get('e_mail')
    p_work = request.POST.get('primary_work')
    s_work = request.POST.get('Secondary_work')
    password = request.POST.get('password')
    phone = request.POST.get('phone_no')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    global A
    A = [name,email,password,phone,address,city,state,p_work,s_work]
    email1 = A[1]
    B = list(Serviceinfo.objects.filter(email = email1))
    if len(B)>0:
        return HttpResponse("you allready have a account")
    else:  
        return render(request, 'serviceman/otp.html')   

def status(request):
      
    otp1 = request.POST.get('otp')
    if otp1 == "1234":
        person = Serviceinfo(name=A[0],email = A[1],phone_no=A[3],password = A[2],sign_up_date = timezone.now(),city=A[5],state=A[6],addres = A[4],primary_work = A[7],secondary_work= A[8])
        person.save()
        return render(request, 'serviceman/succes.html')
    else:
        return render(request, 'serviceman/failed.html')





def login(request):
    return render(request, 'serviceman/login.html') 

def profile_serviceman(request):
    email1 = request.POST.get('email')
    password1 = request.POST.get('passwd')
    B = list(Serviceinfo.objects.filter(email = email1))
    if len(B) >0:
        C = Serviceinfo.objects.get(email = email1)
        if password1 == C.password:
            return render(request, 'serviceman/serviceman_home.html')
        else:
            
            return HttpResponse("<script>window.location = '/serviceman/login'</script>")
    else:
        return HttpResponse("no accout with this email id , please check your email or creat one ")   
