from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Serviceinfo
from customer.models import Contact,Custom_order,Customer_random,Feedback
import datetime
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
        return HttpResponse('<script>window.location = "/serviceman/login";window.alert("You already have a account , please login from that");</script>')
    else:  
        return render(request, 'serviceman/otp.html')   

def status(request):
      
    otp1 = request.POST.get('otp')
    if otp1 == "1234":
        person = Serviceinfo(name=A[0],email = A[1],phone_no=A[3],password = A[2],sign_up_date = timezone.now(),city=A[5],state=A[6],addres = A[4],primary_work = A[7],secondary_work= A[8])
        person.save()
        return render(request, 'serviceman/succes.html')
    else:
        return HttpResponse('<script>window.location = "/";window.alert("You entered a wrong otp");</script>')




def login(request):
    return render(request, 'serviceman/login.html') 

def profile_serviceman(request):
    email1 = request.POST.get('email')
    password1 = request.POST.get('passwd')
    global K 
    K = [email1,password1]
    B = list(Serviceinfo.objects.filter(email = email1))
    if len(B) >0:
        C = Serviceinfo.objects.get(email = email1)
        if password1 == C.password:
            C.loginstate = "yes"
            C.save()
            return HttpResponse("<script>window.location = '/serviceman/login/loggedin/services'</script>")
        else:
            
            return HttpResponse("<script>window.location = '/serviceman/login';window.alert('Your Password is wrong' );</script>")
    else:
        return HttpResponse("no accout with this email id , please check your email or creat one ")   

def services(request):
    B = Serviceinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        L = [B.carpenter=="None",B.cleaning=="None",B.plumber=="None",B.electrecian=="None",B.technecian=="None",B.kitchen=="None"]
        
        return render(request, 'serviceman/worker-service-list.html',{"len":l,"a":L[0],"b":L[1],"c":L[2],"d":L[3],"e":L[4],"f":L[5]})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")


def servicelist_update(request):
    carpenter1 = request.POST.get('carpenter')
    electrecian1= request.POST.get('electrician')
    plumber1 = request.POST.get('plumber')
    kitchen1 = request.POST.get('kitchen')
    cleaning1 = request.POST.get('cleaning')
    technecian1 = request.POST.get('technecian')
    data = [carpenter1,electrecian1,plumber1,kitchen1,cleaning1,technecian1]
    B = Serviceinfo.objects.get(email = K[0])
    B.carpenter = str(carpenter1)
    B.kitchen = str(kitchen1)
    B.technecian = str(technecian1)
    B.electrecian = str(electrecian1)
    B.plumber = str(plumber1)
    B.cleaning = str(cleaning1)
    B.save()
    return HttpResponse("<script>window.location = '/serviceman/login/loggedin/services'</script>")

def aboutus(request):
    B = Serviceinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        return render(request, 'serviceman/about_us.html',{"len":l})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")
#*************************************contact us***************************
def contactus(request):
    B = Serviceinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        return render(request, 'serviceman/contact_us.html',{"len":l})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")

def contact_submit(request):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    subject2 = request.POST.get('subject1')
    comment2 = request.POST.get('comment1')
    comment = Contact(name = name2, email = email2, subject = subject2, comment = comment2,date = timezone.now())
    comment.save()
    return HttpResponse("<script>window.location = '/serviceman/login/loggedin/services'</script>")

#****************************profil part****************************
def profile(request):
    B =Serviceinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        A = Feedback.objects.filter(serviceman_email=K[0])
        lst = []
        for i in A:
            lst.append(i.rating)
        if len(lst) == 0:
            avr_rating = "No Rating "
        else:
            avr_rating = sum(lst)/len(lst)    
        data = {"name":B.name,"rating":avr_rating,"gender":B.gender,"date":B.sign_up_date,"len":l,"primaryjob":B.primary_work,"secondaryjob":B.secondary_work,"email":B.email,"phoneno":B.phone_no,"address":B.addres,"city":B.city,"state":B.state,"password":B.password}
        return render(request,'serviceman/service-profile.html',data)
        
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")
   

def profile_update(request):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    password2 = request.POST.get('password1')
    phone2 = request.POST.get('phoneno1')
    address2 = request.POST.get('address1')
    city2 = request.POST.get('city1')
    state2 = request.POST.get('state1')
    gender2 = request.POST.get('gender1')
    primaryjob2 = request.POST.get('primaryjob')
    secondaryjob2 = request.POST.get('secondaryjob')

    B = Serviceinfo.objects.get(email = K[0])
    B.name = name2
    B.email = email2
    B.phone_no = phone2
    B.password = password2
    B.addres = address2
    B.city = city2
    B.state = state2
    B.gender = gender2
    B.primary_work = primaryjob2
    B.secondary_work = secondaryjob2
    B.save()
    return HttpResponse("<script>window.location = '/serviceman/login/loggedin/profile'</script>")



#****************************notification********************************
def notification(request):
    B =Serviceinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        S1 = S.reverse()
        return render(request,'serviceman/worker-notif.html',{"data":S1,"len":l})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")

def req_accept(request):
    name2 = request.POST.get('name1')
    work2 = request.POST.get('job1')
    desc2 = request.POST.get('desc1')
    
    X = Custom_order.objects.get(customer_name=name2,work=work2,request_date=desc2)
    X.accept_status = "Accepted"
    X.accept_date = timezone.now()
    X.save()
    return HttpResponse("<script>window.location = '/serviceman/login/loggedin/notification';window.alert('You accepted the work, kindly contact him and ask other information and Complete his/her work');</script>")

def req_rejected(request):
    name2 = request.POST.get('name1')
    work2 = request.POST.get('job1')
    desc2 = request.POST.get('desc1')
    #date = datetime.datetime.strptime(desc2, '%m/%d/%Y').strftime('%m/%d/%Y')
    X = Custom_order.objects.get(customer_name=name2,work=work2,request_date=desc2)
    X.accept_status = "Rejected"
    X.save()
    return HttpResponse("<script>window.location = '/serviceman/login/loggedin/notification';window.alert('This work has been rejected ');</script>")
#*******************************************************

def history(request):
    B = Serviceinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        A = Feedback.objects.filter(serviceman_email=K[0])
        return render(request,'serviceman/worker_history_page.html',{"len":l,"data":A})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")


def donateus(request):
    B = Serviceinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        S = Custom_order.objects.filter(serviceman_email=K[0],accept_status="None")
        l = len(S)
        return render(request,'serviceman/donate.html',{"len":l})
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")


def logout(request):
    B = Serviceinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        B.loginstate = "no"
        B.save()
        print("logged out")
        return HttpResponse("<script>window.location = '/'</script>")
    else:
        return HttpResponse("<script>window.location = '/serviceman/login'</script>")
