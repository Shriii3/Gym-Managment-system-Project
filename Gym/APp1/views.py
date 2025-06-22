from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import * 
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if fname and lname and email and password:
            data = User.objects.create_user(username = email , password = password  )
            data.save()
            return redirect('Login')

    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        if username  and password :
            user = authenticate(username = username  , password = password)

            if user is not None:
                messages.success(request,'You have Succesfully login')
                login(request,user)
                return redirect('index')
            
            messages.error(request,'Incorrect username and password')
            return redirect('Login')
        
        messages.error(request,'Please enter the username and password')
        return redirect('Login')

    return render(
        request,'login.html')

def user_logout(request):
    logout(request)
    messages.success(request,'You Have Succesfully Logout')
    return redirect('Login')

def about (request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def offer(request):
    return render(request,'offer.html')

def price(request):
    return render(request,'price.html')

def trainer(request):
    return render(request,'trainer.html')

def Join(request):
    if request.method == "POST":
        fname = request.POST.get('first name')
        lname = request.POST.get('last name')
        age = request.POST.get('age')
        mb_no = request.POST.get('number')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        address = request.POST.get('address')
        category_name = request.POST.get('gym_category')
        print (fname , lname,age,mb_no , height ,weight ,category_name)

        if fname and lname and age and mb_no and height and weight and address :

            category_instance, created = Category.objects.get_or_create(Name=category_name)



            temp = Members_form(First_Name = fname , Last_Name = lname , Age = age , Mobile_No = mb_no , Height = height , Weight = weight , Address = address , category=category_instance, user = request.user)
            temp.save()
            return redirect('review')


    return render(request,'join.html')

def review(request):
    form = Members_form.objects.filter(user= request.user)
    return render(request,'review.html',{'forms':form})


RAZORPAY_API_KEY = settings.RAZORPAY_API_KEY
RAZORPAY_API_SECRET_KEY = settings.RAZORPAY_API_SECRET_KEY
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))



@csrf_exempt
def Payment(request, pay): 
    category = Category.objects.get(Name=pay)

    if request.method == "POST":
        package = request.POST.get('gym_pay')  
        if not package:
            return JsonResponse({'error': 'No plan selected'}, status=400)

        order_amount = int(float(package) * 100)

        payment_order = client.order.create(dict(
            amount=order_amount,
            currency="INR",
            payment_capture=1
        ))

        return JsonResponse({
            'order_id': payment_order['id'],
            'amount': order_amount,
            'api_key': RAZORPAY_API_KEY,
        })

    return render(request, 'payment.html', {
        'categories': [category],
    })





def demo(request):
    if request.method == "POST":
        fname = request.POST.get('first name')
        lname = request.POST.get('last name')
        age = request.POST.get('age')
        mb_no = request.POST.get('number')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        address = request.POST.get('address')


        if fname and lname and age and mb_no and height and weight and address :
            temp =  Demo_Members_form(First_Name = fname , Last_Name = lname , Age = age , Mobile_No = mb_no , Height = height , Weight = weight , Address = address)
            temp.save()
            return redirect('index')
    return render(request, 'demo.html')