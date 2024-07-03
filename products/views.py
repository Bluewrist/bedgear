from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import ContactForm
import datetime
import json


# Create your views here.

def searchbar(request):
    if request.method == 'GET':
        seacrh_term = Search()
        search = request.GET.get('search')
        products = Product.objects.all().filter(product_name = search)
        seacrh_term.search = search
        seacrh_term.save()
    return render(request,"search.html",{'products':products})

def home(request):
    new = Product.objects.filter(is_new =True)
    trending = Product.objects.filter(is_trending=True)
    on_sale = Product.objects.filter(on_sale=True)

    context = {
        "new":new,
        "trending":trending,
        "on_sale":on_sale,
        
    }
  
    return render(request,'front/index.html',context)

def erro_page(request,exception):
    return render(request,"front/404.html")


def about(request):
    return render(request, 'front/about.html') 


'''def login_process(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request=request,username=username,password=password)  
            if user is not None:
                login(request=request,user=user)
                messages.success(request,f"You have successfuly logged in as {username} ")
                return redirect('home')
                
            else:
                msg =  'invalid credentials'
        else:
            msg = "error invalid creadentials"
    return render(request,'front/loginform.html',{'form':form, 'msg':msg})


def registration(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"You have successfully registered login to bid ")
            return redirect('login_process')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm
    return render(request,'front/signup.html',{'form':form, 'msg':msg})   

'''

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Thank you for contacting us we will respond as soon as possible ")
        else:
            msg = 'form is not valid'
    else:
        form = ContactForm 
    return render(request, 'front/contact.html',{'form':form})
        
        

def about(request):
    return render(request,'front/about.html')  



def product_list(request):
    return render(request,'front/shop.html')      


def product_detail(request, id):
    product = Product.objects.get(id=id)
    product_images = product.product_images_set.all()
    related_products = Product.objects.filter(product_category= product.product_category).exclude(id=id)[:1]
   
    
    context = {
		'product': product,
        'related_products':related_products,
        'product_images':product_images,
	}
    return render(request, "front/detail.html",context)

## start of shopping cart logic


def cart(request):
    if request.user.is_authenticated:
        user =  request.user.customer
        order, created =  Order.objects.get_or_create(customer=user ,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        pass
    context =  {'items': items,'order':order,'cartItems':cartItems}
    return render(request, 'front/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        user =  request.user.customer
        order, created =  Order.objects.get_or_create(customer=user,complete=False)
        items =  order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        pass

    context =  {'items': items,'order':order,"dillivery":False,'cartItems':cartItems}
    return render(request, 'front/chackout.html',context)



def updateItem(request):
    data =  json.loads(request.body)
    productId =  data['productId']
    action =  data['action']

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)

    orderitem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderitem.quantity = (orderitem.quantity  + 1)
    elif action == "remove":
        orderitem.quantity = (orderitem.quantity  - 1)
    
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('item was added successfully',safe =  False)

'''
def procesedOrder(request):
    transaction = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = request.user.customer
        order, created =  Order.objects.get_or_create(customer=user,complete=False,transaction_id=transaction)
        DiliveryAddress.objects.create(
            customer = user ,
            order = order,
            city = data['delivery']['city'],
            suburb = data['delivery']['suburb'],
            address = data['delivery']['address'],
            date_orderd = transaction ,
        )

    else:
        coockieData = cookieCart(request)
        items = coockieData['items']

        order = Order.objects.create(
            complete=False
        )

        for item in items:
            product = Product.objects.get(id=item['product']['id'])

            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )
        DiliveryAddress.objects.create(
            first_name = data['form']['first_name'],
            last_name = data['form']['last_name'],
            phone = data['form']['phone'],
            phone2 = data['form']['phone2'],
            order = order,
            city = data['delivery']['city'],
            suburb = data['delivery']['suburb'],
            address = data['delivery']['address'],
            date_orderd = transaction ,
        )
    
    total = float(data['form']['total'])

    if total == order.grand_total:
        order.complete == True
    order.save()

    return JsonResponse('Order has been processed successfuly',safe =  False)
'''


def terms(request):
    return render(request,'front/terms.html')


def faqs(request):
    return render(request,'front/faqs.html')


def orders(request):
    orders = DiliveryAddress.objects.all()
    context = {
        'orders':orders
    }
    return render(request,'front/orders.html',context)


def order_detail(request,id):
    order = Order.objects.get(id=id)
    items =  order.orderitem_set.all()
    context = {
        'order':order,
        'items':items,
    }
    return render(request,'front/order_detail.html',context)








