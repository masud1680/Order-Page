from django.shortcuts import render, HttpResponse,redirect
from .models import OrderModel, FontSection, FeatureSection, ContactSection, GellerySection, Photo, ProductDetails
from .forms import  AdminUpadteOrderForm, FontSectionForm, FeatureSectionForm, ContactSectionForm, GellerySectionForm, PhotoSectionForm, ProductDetailsFrom
from django.db.models import Q, Count
import datetime
import json


# Create your views here.

def qr_code(request):
    return render(request, 'qr_code.html')

def home(request):
    return render(request, 'home.html')

def product_details(request):
    return render(request, 'product_details.html')

def landing_page(request):
    
    # collect data from django template
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comment = request.POST.get('comment')
        area = request.POST.get('area')
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        delivery_charge = request.POST.get('delivery_charge')
        total_price = request.POST.get('total_price')
        payment_method = request.POST.get('payment_method')
        if payment_method == "Online Payment":
            transaction_method = request.POST.get('transaction_method')
            transaction_id = request.POST.get('transaction_id')
        
        # Save data to database
        if payment_method == "Online Payment":
            OrderModel.objects.create(
                name = name,
                phone = phone,
                address = address,
                comment = comment,
                location_choice = area,
                product_name = product_name,
                quantity = quantity,
                price = price,
                delivery_charge = delivery_charge,
                total_price = total_price,
                payment_method = payment_method,
                transaction_method = transaction_method,
                transaction_id = transaction_id
            )
        else:
            OrderModel.objects.create(
                name = name,
                phone = phone,
                address = address,
                comment = comment,
                location_choice = area,
                product_name = product_name,
                quantity = quantity,
                price = price,
                delivery_charge = delivery_charge,
                total_price = total_price,
                payment_method = payment_method
            )
        
        return redirect('order-success')
    # get landing page data from database 
    FontSectionDetails = FontSection.objects.get(id = 1)
    FeatureSectionDetails = FeatureSection.objects.get(id = 1)
    ContactSectionDetails = ContactSection.objects.get(id = 1)
    GallerySectionDetails = GellerySection.objects.prefetch_related('photos').get(id = 1)
    product_details = ProductDetails.objects.get(id = 1)
    
    context ={
        "fontSectionDetails" : FontSectionDetails,
        "FeatureSectionDetails" : FeatureSectionDetails,
        "ContactSectionDetails" : ContactSectionDetails,
        "GallerySectionDetails" : GallerySectionDetails,
        "product_details" : product_details,
    }
    
    return render(request, 'landing_page/landing_page.html', context)

def update_font_section(request):
    # FontSectionDetails = FontSection.objects.get(id = 1)
    form = FontSectionForm() #(instance=FontSectionDetails)
    if request.method == 'POST':
        form = FontSectionForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    return render(request, 'form.html', {'form' : form})
    
def update_feature_section(request):
    FeatureSectionDetails = FeatureSection.objects.get(id = 1)
    form = FeatureSectionForm(instance=FeatureSectionDetails)
    if request.method == 'POST':
        form = FeatureSectionForm(request.POST,  instance=FeatureSectionDetails)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    return render(request, 'form.html', {'form' : form})
  
def update_contact_section(request):
    ContactSectionDetails = ContactSection.objects.get(id = 1)
    form = ContactSectionForm(instance=ContactSectionDetails) #instance=ContactSectionDetails
    if request.method == 'POST':
        form = ContactSectionForm(request.POST, instance=ContactSectionDetails)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    return render(request, 'admin/form.html', {'form' : form})
    
def update_gallery_section_data(request):
    GellerySectionDetails = GellerySection.objects.get(id = 1)

    form = GellerySectionForm(instance=GellerySectionDetails) # instance=GellerySectionDetails
    
    if request.method == 'POST':
        form = GellerySectionForm(request.POST, instance=GellerySectionDetails)
        
        
        if form.is_valid():
            form.save()
                    
            return redirect('landing-page')
     
    return render(request, 'admin/form.html', {'form' : form} )
    
def update_gallery_section_photo(request):
    GellerySectionDetails = GellerySection.objects.get(id = 1)

    form = PhotoSectionForm() # instance=PhotoFormSetDetails
    
    if request.method == 'POST':
        
        form= PhotoSectionForm(request.POST, request.FILES,) #  request.FILES,  queryset=Photo.objects.all()
        
        if form.is_valid():
            # print(form)
            gallery = form.save()
            GellerySectionDetails.photos.add(gallery)        
            # return redirect('landing-page')
    
    return render(request, 'admin/form.html',  {'form' : form}  )

def delete_gallery_section_photo(request):
    GellerySectionDetails = GellerySection.objects.prefetch_related('photos').get(id = 1)
    
    # if request.method == 'POST':
    for photo in GellerySectionDetails.photos.all():
        # if photo.id == 4:
            # print(photo.photo_asset.name)
            # print("url:::::::::::::::::" , photo.photo_asset.url)      
            photo = photo.delete()
    
    # return redirect('landing-page')
    return HttpResponse("working")
    
def updateProductDetails(request):
    product_details = ProductDetails.objects.get(id = 1)
    form = ProductDetailsFrom(instance=product_details)
    
    if request.method == 'POST':
        form = ProductDetailsFrom(request.POST, instance=product_details)
        
        if form.is_valid():
            form.save()
        return HttpResponse("Update successfull.") 
    return render(request, "admin/form.html", {"form" : form})   


def myorder_view(request):
    if request.method == 'POST':
        query = request.POST['search']
       
        MyallOrder = OrderModel.objects.filter(phone = query).order_by('-order_created_at')
        
    else:
        MyallOrder = OrderModel.objects.none()
    return render(request, 'myorder_view.html',{'MyallOrder' : MyallOrder})
    


def order_create_admin_dashboard(request):
    
    # collect data from django template
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comment = request.POST.get('comment')
        area = request.POST.get('area')
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        delivery_charge = request.POST.get('delivery_charge')
        total_price = request.POST.get('total_price')
        payment_method = request.POST.get('payment_method')
        if payment_method == "Online Payment":
            transaction_method = request.POST.get('transaction_method')
            transaction_id = request.POST.get('transaction_id')
        
        # Save data to database
        if payment_method == "Online Payment":
            OrderModel.objects.create(
                name = name,
                phone = phone,
                address = address,
                comment = comment,
                location_choice = area,
                product_name = product_name,
                quantity = quantity,
                price = price,
                delivery_charge = delivery_charge,
                total_price = total_price,
                payment_method = payment_method,
                transaction_method = transaction_method,
                transaction_id = transaction_id
            )
        else:
            OrderModel.objects.create(
                name = name,
                phone = phone,
                address = address,
                comment = comment,
                location_choice = area,
                product_name = product_name,
                quantity = quantity,
                price = price,
                delivery_charge = delivery_charge,
                total_price = total_price,
                payment_method = payment_method
            )
        
        return redirect('admin-dashboard')
    
    product_details = ProductDetails.objects.get(id = 1)
    return render(request, 'admin/form.html', {"product_details" : product_details})

def ordersuccess(request):
    return render(request, 'order_success.html')



############ Admin Panel working

from django.utils import timezone
from datetime import timedelta


def all_count():
    now = timezone.now()
    # print("date========", now)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)
    
    counts = OrderModel.objects.aggregate(
     total_orders = Count('id', distinct=True),
     today_orders = Count('id', filter=Q(order_created_at__range=(start_of_day,end_of_day)), distinct=True),
     submit_orders = Count('id',  filter=Q(status = "Submitted" )) ,
     complete_orders = Count('id',  filter=Q(status = "Completed")),
     cancle_orders = Count('id',  filter=Q(status = "Cancelled")), 
    )
    
    

    coutext = {
        "total_orders" : counts['total_orders'], 
        "today_orders" : counts['today_orders'], 
        "submit_orders" : counts['submit_orders'], 
        "complete_orders" : counts['complete_orders'], 
        "cancle_orders" : counts['cancle_orders']
        }
    
    return coutext

def admin_dashboard(request):
    
    # last 3 days orders show
    now = timezone.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)
    
    
    # query
    orders = OrderModel.objects.filter(order_created_at__range=(start_of_day,end_of_day))

    #make json data
    orders_list = []

    for order in orders:
        orderData = {          
            "id": order.id,  
            "product": order.product_name,
            "customer": order.name, 
            "date": order.order_created_at, 
            "status": order.status,
            
        }
        orders_list.append(orderData)
        
    #print(orders_list)
    
    
    
    counts = all_count()
    context ={
        "counts" : counts,
        "orders_json": json.dumps(orders_list, default=str),  # convert datetime to string
    }
    
    return render(request, 'admin/main_dashboard.html', context)


def order_dashboard(request):
    orders = OrderModel.objects.all()
    
    #make json data
    orders_list = []
    for order in orders:
        orderData = {
            "id": order.id, 
            "customer": order.name, 
            "contact": order.phone, 
            "email": order.phone, 
            "product": order.product_name, 
            "photoUrl": 'https://png.pngtree.com/png-clipart/20230325/original/pngtree-islam-muslim-women-girl-hijab-pray-namaz-on-prayer-mat-png-image_9002987.png', 
            "quantity": order.quantity, 
            "amount": order.price, 
            "totalamount": order.total_price, 
            "location": order.location_choice, 
            "fullAddress": order.address, 
            "comment": order.comment, 
            "status": order.status, 
            "createdAt": order.order_created_at, 
            "updatedAt": order.order_updated_at 
            
        }
        orders_list.append(orderData)
        
    # print(orders_list)

    context ={
        "orders" : orders,
        "orders_json": json.dumps(orders_list, default=str),  # convert datetime to string
    }
    
    return render(request, 'admin/order_dashboard.html', context)


def order_update(request, order_id):
    # get spacific order ditels
    order = OrderModel.objects.get(id = order_id)
    
    if request.method == 'POST':
        form = AdminUpadteOrderForm(request.POST, instance=order)
        if form.is_valid():
            if request.user:
                order = form.save(commit = False)
                order.user = request.user
                order.save()
                return redirect('order-dashboard')
                # return HttpResponse('order complete.')
            else:
                form.save()
                return HttpResponse('order complete.')
    else:
        form = AdminUpadteOrderForm(instance=order)
    
    return render(request, 'order_page.html', {'form' : form})


def users_dashboard(request):
    
    
    return render(request, 'admin/users.html')

def content_dashboard(request):
    
    
    return render(request, 'admin/content.html')

from django.contrib.auth.models import User
def test_template(request):
    

    print(User.objects.all())

    return render(request, 'test_template.html')
