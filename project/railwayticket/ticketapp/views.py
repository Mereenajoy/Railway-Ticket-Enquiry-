from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import messages

def demo(request):
    return render(request,'demo.html')

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        phno=request.POST['phno']
        aadhar = request.POST['aadhar']
        password=request.POST['password']
       
        if Register.objects.filter(email=email):
            context={'msg':'Email Already Exists!'}
            return render(request,'register.html',context)
        elif Register.objects.filter(username=username):
            context={'msg':'Username Already Exists!'}
            return render(request,'register.html',context)
        else:
            reg=Register(username=username , email=email,phno=phno,aadhar=aadhar,password=password)
            reg.save()
            return render(request,'login.html')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        u=Register.objects.filter(email=email, password=password, usertype="U")
        print(u)
        if len(u) == 1:
            request.session['email']=email
            return redirect("http://127.0.0.1:8000/userhome")
        else:
            print("Invalid")
            context={'msg':"Invalid Credentials"}
            return render(request,'login.html',context)

        
    else:
        return render(request, "login.html") 


def index(request):
    return render(request,'index.html')

def showtrain(request):
    return render(request,'showtrain.html')



def profile(request):
    u=request.session['email']
    display=Register.objects.filter(email=u)
    ss={'profile':display}
    return render(request,'profile.html',ss)


def updateprofile(request):
    if request.method == 'POST':
        user =request.session['email']
        up=Register.objects.get(email=user)
        xemail=up.email
        xpassword=up.password
        username = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        aadhar=request.POST.get('aadhar')
        password=request.POST.get('password')
        

        up.username = username
        up.email = email
        up.phno = phno
        up.aadhar=aadhar
        up.password = password
        # up.confirmpasswd=confirmpasswd

        up.save()
        
        if xemail != up.email or xpassword != up.password:
            return redirect(login)
        
        context = {'msg': 'User Details Updated', 'up': up}
       
        return redirect('profile')
    else:
        user =request.session['email']
        up=Register.objects.get(email=user)
        context={'up':up}
        return render(request, 'update_profile.html', context) 
    



def view_booking(request):
    u=request.session['email']
    display=Register.objects.get(email=u)
    v=Passenger.objects.filter(user=display)
    context={'v':v}
    return render(request,'view_booking.html',context)
    

def book(request):
    return render(request,'book.html')

def userhome(request):
    u=request.session['email']
    v=Register.objects.filter(email=u)
    context={'na':v}
    
    return render(request,'userhome.html',context)

def search_trains(request):
    if request.method == 'GET' and 'train_name' in request.GET:
        train_name = request.GET['train_name']
        trains = Add_Train.objects.filter(trainname__icontains=train_name)
    else:
        trains = Add_Train.objects.all()
    print(trains)
    
    return render(request, 'showtrain1.html', {'trains': trains})


def train_schedules(request, train_id):
    train = get_object_or_404(Add_Train, id=train_id)
    schedules = Train_shedulde.objects.filter(train=train)
    seat=Seat.objects.all()
    for i in seat:
        if i.name=="General":
            mid=i.rate
        elif i.name =="Sleeper":
            high=i.rate
        else:
            pass


    return render(request, 'showtrain.html', {'train': train, 'trains': schedules,'mid':mid,'high':high})

def searchtrain(request):
    
    if request.method == "POST":
        fr=request.POST["from"]
        to=request.POST["to"]
        date=request.POST["date"]
        print(date)
        fro=Place.objects.get(id=fr)
        too=Place.objects.get(id=to)
        trains=Train_shedulde.objects.filter(date=date,from_city=fro,to_city=too)
        seat=Seat.objects.all()
        for i in seat:
            if i.name=="General":
                mid=i.rate
            elif i.name =="Sleeper":
                high=i.rate
            else:
                pass
        context={'trains':trains,'mid':mid,'high':high}
        return render(request,'showtrain.html',context)
    else:
        place=Place.objects.all()
        seat=Seat.objects.all()
        t=Train_shedulde.objects.all()
        for i in t:
            print(i.date)
        return render(request,'searchtrain.html',{'place':place,'seat':seat})

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        cont=ContactMessage(name=name,email=email,message=message)
        cont.save()
        return render(request,'index.html')
    else:
        return render(request,'contact_form.html')
    
def book(request):
    pk=request.GET["id"]
    sid=request.GET["sid"]
    em=request.session["email"]
    user=Register.objects.get(email=em)
    s=Seat.objects.all()
    # id = request.GET.get('st')
    # st = Seat.objects.get(id=id)
    # print(st)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        s_id= request.POST["st"]
        # print(s_id)
        # print(type(s_id))
        
        # if s_id == 1:
        #     f=90
        
        # else:
        #     f=50
        
        st = Seat.objects.filter(id=s_id)
        for i in st:
            price = i.rate
            
        
        shed=Train_shedulde.objects.get(id=sid)  
        em=request.session["email"]
        user=Register.objects.get(email=em)
        train=Add_Train.objects.get(id=pk)
        seat=Seat.objects.get(id=s_id)
        fare=train.price + price
        new=Book_details.objects.create(user=user,train=train,name=name,seat=seat,age=age,gender=gender, status="booked",fare=fare)
        new.save()
        request.session['book_id'] = new.id
        shed.remaining_seats=shed.remaining_seats - 1
        shed.save()

        # r="/confirm_booking"
        return redirect(confirm_booking)

    else:
        em=request.session["email"]
        user=Register.objects.get(email=em)
        train = Train_shedulde.objects.all()
        passengers = Passenger.objects.filter(user=user)
        for passenger in passengers:
            print(passenger)
            
        return render(request, 'book.html', {'train': train,'seat':s,'p':passengers})


    
def showtrain1(request):
    return render(request,"showtrain1.html")




def confirm_booking(request):
    # u=request.session['email']
    # display=Register.objects.get(email=u)
    d = request.session['book_id']
    v=Book_details.objects.filter(id=d)
    context={'v':v}
    return render(request,'confirm_booking.html',context)
    

import os
import stripe

stripe.api_key = 'sk_test_51MzR0qSDsHoB6h4XS89hryuFO2ZLs4EGe6bs44P45Pq1pYzw1FbxRGwfHU1kcz13dX9qi9RFj2PDlFn56vF51rOe00Stz4HfFt'


#
# @app.route('checkout_session', methods=['POST'])
def checkout_session(request):
    id = request.session['book_id']
    book =Book_details.objects.get(id=id)
    print(book.name)
    data =  request.session['book_id']
    d = Book_details.objects.filter(id=data)
    for i in d:
        user = i.user
        train=i.train
        name=i.name
        seat=i.seat
        age=i.age
        gender=i.gender
        date1=i.date1
        fare=i.fare
        detail = Passenger(user=user,train=train,name=name,seat=seat,age=age,gender=gender,date1=date1,fare=fare,cancel_request='None')
        detail.save()
        del  request.session['book_id']

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': book.name,
                },
                'unit_amount': book.fare * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/view_booking',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
    )
   
       
        
    return redirect(session.url, code=303)

def pay_success(request):
    return render(request,'pay_success.html')

def pay_cancel(request):
    return render(request,"pay_cancel")

def cancel_ticket(request):
    id = request.GET.get('id')
    t = Passenger.objects.get(id=id)
    s ='request for cancel'
    t.cancel_ticket=s
    t.save()
    return render(request,'cancel_ticket.html')
