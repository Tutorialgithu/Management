from email import message_from_file
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from.models import Log_In_ID, Data, FoodList, Query, Bill 
from django.contrib import messages




def Index(request):
    return render(request, "index.html")

def Aboutpage(request):
    return render(request, "About.html")

def LogInpage(request):
    return render(request, "Login.html")

def booking(request):
    return render(request, "booking.html")

def savedata(request):
    n=''
    if request.method == "POST":
         if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address') and request.POST.get('pincode')  and request.POST.get('idproof')  and request.POST.get('idnumber') and request.POST.get('check_in') and request.POST.get('check_out'):
            obj = Data()
            obj.name = request.POST.get('name')   
            obj.mobile = request.POST.get('mobile')   
            obj.email = request.POST.get('email')   
            obj.address = request.POST.get('address')   
            obj.pincode = request.POST.get('pincode')   
            obj.idproof = request.POST.get('idproof')   
            obj.idnumber = request.POST.get('idnumber')   
            obj.check_in = request.POST.get('check_in')   
            obj.check_out = request.POST.get('check_out')  
            obj.save()  
            info= Data.objects.all()
            return render(request, 'booking.html',{'obj':info})
    else:
        return render(request, 'booking.html')


def contactpage(request):
    return render(request,'contact.html')


def contactdata(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
          data = Query()
          data.name = request.POST.get('name')
          data.email= request.POST.get('email')
          data.subject = request.POST.get('subject')
          data.message = request.POST.get('message')
          data.save()
          return render(request,'contact.html')
    else:
        return HttpResponse('ERROR')



def Servicepage(request):
    return render(request, "service.html")


def Roomspage(request):
    return render(request, "rooms.html")


def Dashboardpage(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password  = request.POST['Password']
        data = Log_In_ID.objects.get(id=1)
        uname = data.Username
        pw = data.Password
        if username == uname and password == pw:
            return render(request, 'dashboard.html')
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')


def orderlist(request):
    info= Data.objects.all()
    return render(request,'orderlist.html',{'obj':info})

def orderlistpage(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address') and request.POST.get('pincode')  and request.POST.get('idproof')  and request.POST.get('idnumber') and request.POST.get('check_in') and request.POST.get('check_out'):
            obj = Data()
            obj.name = request.POST.get('name')   
            obj.mobile = request.POST.get('mobile')   
            obj.email = request.POST.get('email')   
            obj.address = request.POST.get('address')   
            obj.pincode = request.POST.get('pincode')   
            obj.idproof = request.POST.get('idproof')   
            obj.idnumber = request.POST.get('idnumber')   
            obj.check_in = request.POST.get('check_in')   
            obj.check_out = request.POST.get('check_out')  
            obj.save()  
            info= Data.objects.all()
            return render(request, 'orderlist.html',{'obj':info})
        else:
            info= Data.objects.all()
            return render(request, 'orderlist.html',{'obj':info})
    else:
        return render(request, 'login.html')

def Foodpage(request):
    info= FoodList.objects.all()
    return render(request, "food.html", {'data':info})   

def foodlist(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('time') and request.POST.get('item') and request.POST.get('quantity'):
            data = FoodList()
            data.name = request.POST.get('name')
            data.mobile= request.POST.get('mobile')
            data.time = request.POST.get('time')
            data.item = request.POST.get('item')
            data.quantity = request.POST.get('quantity')
            data.save()
            info= FoodList.objects.all()
            return render(request, 'food.html',{'data':info})
        else:
            info= FoodList.objects.all()
            return render(request, 'food.html',{'data':info})
    else:
        return render(request, 'login.html')
    

def billinglist(request):
    info= Bill.objects.all()
    return render(request, 'billinglist.html', {'info':info})
    # return render(request, "billinglist.html")


def Querypage(request):
    info= Query.objects.all()
    return render(request, 'Query.html',{'data':info})



def display(request):
   return render(request, 'display.html',)

def edit(request):
    emp =Data.objects.all()
    return render(request, "orderlist.html",{'emp':emp} )





# def Updaterecord(request):
#    updatr_id = Data.objects.get(id=id)
#    template = loader.get_template('update.html')
#    return render(request, 'display.html',)

def paymentstatus(request):
     return render(request,'paymentstatus.html')

def Invoicepage(request):
     return render(request, 'invoice.html')

def invoicelist(request):
    if request.method == "POST":
        if request.POST.get('transactionId') and request.POST.get('name') and request.POST.get('date') and request.POST.get('total') and request.POST.get('payment_method')  and request.POST.get('payment_status'):
            obj = Bill()
            obj.transactionId = request.POST.get('transactionId')   
            obj.name = request.POST.get('name')   
            obj.date = request.POST.get('date')   
            obj.total = request.POST.get('total')   
            obj.payment_method = request.POST.get('payment_method')   
            obj.payment_status = request.POST.get('payment_status')     
            obj.save()  
            info= Bill.objects.all()
            return render(request, 'billinglist.html', {'info':info})
       
    else:
       return HttpResponse("error")


















    