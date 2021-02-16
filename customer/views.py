from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Custinfo,Custom_order
from customer.models import Contact
from serviceman.models import Serviceinfo
from django.utils import timezone
# Create your views here.


def redirect(request):
    return render(request,'customer/redirect.html')

def otp(request):
    name = request.POST.get('user_name')
    email = request.POST.get('e_mail')
    password = request.POST.get('password')
    phone = request.POST.get('phone_no')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    global A
    A = [name,email,password,phone,address,city,state]
    
    B = list(Custinfo.objects.filter(email = email))
    if len(B)>0:
        return HttpResponse("you allready have a account")
    else:  
        return render(request, 'customer/otp.html')

def status(request):
    otp1 = request.POST.get('otp')
    if otp1 == "1234":
        person = Custinfo(cust_name=A[0],email = A[1],phone_no=A[3],password = A[2],sign_up_date = timezone.now(),city=A[5],state=A[6],addres = A[4])
        person.save()
        return render(request, 'customer/succes.html')
    else:
        return render(request, 'customer/failed.html')


def login(request):
    return render(request, 'customer/login.html')    

def profile_customer(request):
    email1 = request.POST.get('email')
    password1 = request.POST.get('passwd')
    global K 
    K = [email1,password1]
    A = list(Custinfo.objects.filter(email = email1))
    if len(A) >0:
        B = Custinfo.objects.get(email = email1)
        if password1 == B.password:
            B.loginstate = "yes"
            B.save()
            return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")
        else:
            
            return HttpResponse("<script>window.location = '/customer/login'</script>")
    else:
        return HttpResponse("no accout with this email id , please check your email or creat one ")        

def services(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        return render(request, 'customer/customer-service-list.html')
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")    

def about(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        return render(request, 'customer/about_us.html')
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")   

def profile(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    data = {"name":B.cust_name,"gender":B.gender,"date":B.sign_up_date,"email":B.email,"phoneno":B.phone_no,"address":B.addres,"city":B.city,"state":B.state,"password":B.password}
    if k == "yes":
        return render(request,'customer/cust_profile.html',data)
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def profileupdate(request):
    name2 = request.POST.get('user_name1')
    email2 = request.POST.get('email1')
    password2 = request.POST.get('password1')
    phone2 = request.POST.get('phone_no1')
    address2 = request.POST.get('address1')
    city2 = request.POST.get('city1')
    state2 = request.POST.get('state1')
    gender2 = request.POST.get('gender1')
    B = Custinfo.objects.get(email = K[0])
    B.cust_name = name2
    B.email = email2
    B.phone_no = phone2
    B.password = password2
    B.addres = address2
    B.city = city2
    B.state = state2
    B.gender = gender2
    B.save()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/profile'</script>")

def logout(request):
    B = Custinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        B.loginstate = "no"
        B.save()
        print("logged out")
        return HttpResponse("<script>window.location = '/'</script>")
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def contact(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        return render(request, 'customer/contact_us.html')
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def contact_submit(request):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    subject2 = request.POST.get('subject1')
    comment2 = request.POST.get('comment1')
    comment = Contact(name = name2, email = email2, subject = subject2, comment = comment2,date = timezone.now())
    comment.save()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")



def search(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":

        B = Custinfo.objects.get(email = K[0])
        carpenter2 = request.POST.get('carpenter')
        electrecian2 = request.POST.get('electrecian')
        plumber2= request.POST.get('plumber')
        technecian2 = request.POST.get('technecian')
        cleaning2 = request.POST.get('cleaning')
        kitchen2 = request.POST.get('kitchen')
        button12 = request.POST.get('button1')
        button22 = request.POST.get('button2')
        lst = [cleaning2,technecian2,plumber2,electrecian2,carpenter2,kitchen2]
        services = ['cleaning','technecian','plumber','electrecian','carpenter','kitchen']
        if button12 == "on":
            print(lst)
            l = lst.index('on')
            print(l,services[l])
            service = services[l]
            if service == 'cleaning':
                service_data = Serviceinfo.objects.filter(cleaning='on')
                print(service_data)
                return render(request,'customer/custom_search.html',{"data":service_data})
            elif service == 'technecian':
                service_data = Serviceinfo.objects.filter(technecian='on')
                print(service_data)    
                return render(request,'customer/custom_search.html',{"data":service_data})
            elif service == 'plumber':
                service_data = Serviceinfo.objects.filter(plumber='on')
                print(service_data) 
                return render(request,'customer/custom_search.html',{"data":service_data})
            elif service == 'electrecian':
                service_data = Serviceinfo.objects.filter(electrecian='on')
                print(service_data) 
                return render(request,'customer/custom_search.html',{"data":service_data})
            elif service == 'carpenter':
                service_data = Serviceinfo.objects.filter(carpenter='on')
                print(service_data) 
                return render(request,'customer/custom_search.html',{"data":service_data})
            elif service == 'kitchen':
                service_data = Serviceinfo.objects.filter(kitchen='on')
                print(service_data) 
                return render(request,'customer/custom_search.html',{"data":service_data})
            else:
                return HttpResponse("Entered Wrong information")
            
        elif button22 == "on":
            return HttpResponse("randomsearch page") 
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def search_request(request):
    B = Custinfo.objects.get(email = K[0])
    a = request.POST.get('request')
    work = Custom_order(customer_email=K[0],serviceman_email=a,request_date=timezone.now())
    work.save()
    
    return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")