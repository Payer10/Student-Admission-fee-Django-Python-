from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import*
from sslcommerz_lib import SSLCOMMERZ 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # user = authenticate(username = name,password = str(password))
        user = User.objects.filter(name = name)
        # print(user)
        if user is not None:
            # login(request,user)
            return redirect('home/')
        # else:
        #     return redirect(login_page)
    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password1')
        print(password,password2)
        if password != password2:
            return redirect(register_page)
        else:
            user = User.objects.create(name=name,email=email,password=password)
            user.save()
            return redirect(login_page)

    return render(request,'register.html')

def logout_pages(request):
    logout(request)
    return redirect(login_page)

# @login_required(login_url='login')
def home_page(request):
    if request.method == 'POST':
        Student_ID = request.POST.get('student_id')
        Student_Name = request.POST.get('student_name')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        Addmission_Date = request.POST.get('addmission_date')
        addmission_fee = Student_Addminssion_fee(Student_ID=Student_ID,Student_Name=Student_Name,mobile=mobile,email=email,Addmission_Date = Addmission_Date)
        addmission_fee.save()
        return redirect(student_fee)
    return render(request,'home.html')

# @login_required(login_url='home')
def student_fee(request):
   
    store_id = settings.STORE_ID
    store_password =settings.STORE_PASSWORD 

    setting = { 'store_id': store_id, 'store_pass': store_password, 'issandbox': True }
    sslcommez = SSLCOMMERZ(setting)
    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "http://127.0.0.1:8000/student_fee/success/"
    post_body['fail_url'] = "http://127.0.0.1:8000/student_fee/fail/"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcommez.createSession(post_body)
    return redirect(response['GatewayPageURL'])
    print(response)


# @login_required(login_url='student_fee')
@csrf_exempt
def success(request):
    a = Student_Addminssion_fee.objects.all().last()
    return render(request,'success.html',{'a':a})

# @login_required(login_url='student_fee')
@csrf_exempt
def fail(request):
    a = Student_Addminssion_fee.objects.all().last()
    a.delete()
    return render(request,'fail.html',{'a':a})

