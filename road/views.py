from django.shortcuts import render, redirect
from users.models import User, SmsCode, GAI, CUSTOMER
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout
import random
from road.utils.send_code import send_code
from django.db.models import Q
# Create your views here.

def fine(request, pk ):
    fines = Fine.objects.filter(car=pk)
    payment = request.GET
    print(payment, "-----------------") 

    if payment.get('payment') =='true':
        fines = fines.filter(is_payment=True)
    elif payment.get('payment') =='false':
        fines = fines.filter(is_payment=False)
    else:
        fines
    car = Car.objects.filter(id=pk).first()
    print(fines)
    return render(request,'fine.html' , {'fines':fines , 'car':car, 'car_pk': pk})

def avtorizatsiya(request):

    phone = request.POST.get("number")
    user = User.objects.filter(phone=phone).first()
    
    
    if request.method =="POST":
        if not phone or len(phone)!=17  :
            messages.error(request, "Telefon raqam kiritmadingiz")
            return redirect("avtorizatsiya")
        
        code = send_code(phone)
        if user:
            user.dispatch_id = code['dispatch_id']
            user.save()
            return redirect("sms", phone=phone, dis_id=code['dispatch_id'])
        else:
            user, created = User.objects.update_or_create(
                phone=phone,
                defaults={
                    'email': phone,
                    'username': phone,
                    'dispatch_id': code['dispatch_id'],
                    'role': CUSTOMER
                }
            )
            return redirect("sms", phone=phone, dis_id=code['dispatch_id'])
    
    return render(request ,  'avtorizatsiya.html' , )



def main(request ):
    cars = Car.objects.filter(user=request.user, is_active=True)
    return render(request ,  'main.html ', {'cars':cars} )



def addCart(request ):
    return render(request ,'addCart.html' )


def sms(request, phone, dis_id):
    code = request.POST.get("code")
    
    sms_code = SmsCode.objects.filter(dispatch_id = dis_id ).first()
    user = User.objects.filter(dispatch_id = dis_id ).first()
    print(user.role, "-------------------------")
    if request.method =="POST":    
        if not code or len(code)!=4 or str(sms_code.code) != str(code):
            messages.error(request, "Tasdiqlash kodi noto`g`ri!")
            return redirect("sms", phone, dis_id)
        if user.role == GAI:
            login(request, user) 
            return redirect("shtraf")
        else:
            login(request, user)
            return redirect("create")
    
    return render(request ,  'sms.html' , {'user':phone, 'dis_id':dis_id})


def verification_sms(request):
    return render(request, )

def radar(request, pk):
    fine = Fine.objects.filter(pk=pk).first()
    card = Card.objects.filter(user=request.user)
    return render(request ,  'radar.html',  {'fine': fine , 'card':card})  


def shtraf(request):
    decision_numbers = random.randint(10000000000 , 99999999999) 
    modda = random.randint(1,300)
    band = random.randint(1,10)
    data = request.POST
    car = Car.objects.filter(id=data.get("id")).first()  
    min_amount = 340000

    print(data)
    if request.method == 'POST':
        if int(data.get('fine_fast')) >60 and int(data.get('fine_fast')) < 81:
            fine = Fine.objects.create(
            car = car,
            decision_number =  decision_numbers,
            violation_clause = f'{modda}-modda {band}-band ',
            violation_description = data.get('violation_description'),
            violation_address = data.get('violation_address'),
            fine_amount = min_amount,
            fine_fast = data.get('fine_fast'),
            fine_image = data.get('fine_image')
        )
        if int(data.get('fine_fast')) > 80 and int(data.get('fine_fast'))  < 100:
            fine = Fine.objects.create(
                car = car,
                decision_number =  decision_numbers,
                violation_clause = f'{modda}-modda {band}-band ',
                violation_description = data.get('violation_description'),
                violation_address = data.get('violation_address'),
                fine_amount = 5 * min_amount,
                fine_fast = data.get('fine_fast'),
                fine_image = data.get('fine_image')
        )
        if int(data.get('fine_fast')) > 100 :
            fine = Fine.objects.create(
            car = car,
            decision_number =  decision_numbers,
            violation_clause = f'{modda}-modda {band}-band ',
            violation_description = data.get('violation_description'),
            violation_address = data.get('violation_address'),
            fine_amount = 10* min_amount,
            fine_fast = data.get('fine_fast'),
            fine_image = data.get('fine_image')
        )    

    cars = enumerate(Car.objects.all(), 1)
    return render(request ,  'shtraf.html'  , {'cars':cars} )

def create(request):
    region =[ '01','10' ,'20','25','30','40','50','60','70','75','80','85','90','95']
    data = request.POST

   
    if request.method=='POST':
        if data.get('number')[:2] not in region:
            messages.error(request, "xato kiritdiz")
            return redirect('create')
        car = Car.objects.create(
            number = data.get("number"),
            teck_number = f"{data.get('seriya')} {data.get('num')}",
            brand =data.get('marka'),
            user=request.user,
            model =data.get('model'),
            image =data.get('image'),
            is_active = True

         )
        return redirect('main')
    return render(request ,  'create.html'  )

def delete_car_item(request, pk):
    car =Car.objects.get(pk=pk)
    car.is_active = False
    car.save()
    return redirect('main')


def addCart(request ):
    cards = Card.objects.filter(user=request.user)
    
    data = request.POST

    if request.method=='POST':
        if len(cards)==1:
            messages.error(request, "Siz bittadan ortiq karta qo`sholmaysiz")
            return redirect("addCart")
      
        else:
            cards = Card.objects.create(
                card_number = data.get('card-number'),
                card_date = data.get('card-date'),
                card_holder = data.get('card-holder'),
                user=request.user,
                card_cvc = data.get('card-cvc'),
                price = 400000
                )
            return redirect('addCart')
    return render(request ,'addCart.html' , {'cards':cards} )

def delete_card_item(request , pk):
    card =Card.objects.get(pk=pk).delete()
    return redirect('addCart')

 
def to_pay(request, pk):
    fines = Fine.objects.get(pk=pk) 
    cards = Card.objects.get(user=request.user)
    print(fines, cards.price > fines.fine_amount,)
    print(cards.price, "-------------------")
    print(fines.fine_amount, "====================")
    if fines:
        
        fines.is_payment = True
        if cards.price > fines.fine_amount:
            cards.price =  cards.price - fines.fine_amount
            fines.save()
            cards.save()
            return redirect('radar', pk)
        else:
            messages.warning(request, "Kartada mablag' yetarli emas!")
            return redirect('radar', pk)
    else:
        print('-------------------------------')
    return render(request , 'fine' )

def is_payment_true(request):
    fines = Fine.objects.filter(is_payment=True)
    return render('fine' , {'fines':fines})


def is_payment_false(request):
    fines = Fine.objects.filter(is_payment=False)

    return render('fine' , {'fines':fines})