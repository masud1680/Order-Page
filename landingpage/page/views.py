from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import OrderModel, FontSection, FeatureSection, ContactSection, GellerySection, Photo, ProductDetails
from .forms import  AdminUpadteOrderForm, FontSectionForm, FeatureSectionForm, ContactSectionForm, GellerySectionForm, PhotoSectionForm, ProductDetailsFrom
from django.db.models import Q, Count
import datetime
import json # send html js section json data
from django.http import JsonResponse # recived html js section json data


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
    FontSectionDetails = FontSection.objects.get(id = 1)
    form = FontSectionForm(instance=FontSectionDetails) #(instance=FontSectionDetails)
    if request.method == 'POST':
        form = FontSectionForm(request.POST, request.FILES,instance=FontSectionDetails)
        if form.is_valid():
            print(FontSectionDetails.font_asset)
            form.save()
            return redirect('content-dashboard')    
    return render(request, 'admin/photo_form.html', {'form' : form})
    
def update_feature_section(request):
    FeatureSectionDetails = FeatureSection.objects.get(id = 1)
    form = FeatureSectionForm(instance=FeatureSectionDetails)
    if request.method == 'POST':
        form = FeatureSectionForm(request.POST,  instance=FeatureSectionDetails)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    return render(request, 'admin/photo_form.html', {'form' : form})
  
def update_contact_section(request):
    ContactSectionDetails = ContactSection.objects.get(id = 1)
    form = ContactSectionForm(instance=ContactSectionDetails) #instance=ContactSectionDetails
    if request.method == 'POST':
        form = ContactSectionForm(request.POST, instance=ContactSectionDetails)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    return render(request, 'admin/photo_form.html', {'form' : form})
    
def update_gallery_section_data(request):
    GellerySectionDetails = GellerySection.objects.get(id = 1)

    form = GellerySectionForm(instance=GellerySectionDetails) # instance=GellerySectionDetails
    
    if request.method == 'POST':
        form = GellerySectionForm(request.POST, instance=GellerySectionDetails)
        
        
        if form.is_valid():
            form.save()
                    
            return redirect('landing-page')
     
    return render(request, 'admin/photo_form.html', {'form' : form} )
    
def update_gallery_section_photo(request):
    GellerySectionDetails = GellerySection.objects.get(id = 1)

    form = PhotoSectionForm() # instance=PhotoFormSetDetails
    
    if request.method == 'POST':
        
        form= PhotoSectionForm(request.POST, request.FILES,) #  request.FILES,  queryset=Photo.objects.all()
        
        if form.is_valid():
            # print(form)
            gallery = form.save()
            GellerySectionDetails.photos.add(gallery)        
            return redirect('content-dashboard')
    
    return render(request, 'admin/photo_form.html',  {'form' : form}  )

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

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt 
def content_dashboard(request):

    
    # get data from database send to fontand
    font = get_object_or_404(FontSection, pk=1)
    feature = get_object_or_404(FeatureSection, pk=1)
    contact = get_object_or_404(ContactSection, pk=1)
    gallery = get_object_or_404(GellerySection, pk=1)
    galleryImg = GellerySection.objects.prefetch_related('photos').get(id = 1) 
    product = get_object_or_404(ProductDetails, pk=1)
    
    # recived data from fontand send to database
    if request.method == "POST":
        try:
            recivedJsonData = json.loads(request.body)
        
            #-- font section---
            font_data = recivedJsonData.get("fontSection", {})
            font.small_title = font_data.get("small_title", font.small_title)
            font.big_title = font_data.get("big_title", font.big_title)
            font.details = font_data.get("details", font.details)
            font.font_asset = font_data.get("font_asset", font.font_asset)
            # print(font_asset)
            
            #--- feature section ---
            feature_data = recivedJsonData.get("featureSection",{})
            feature.first_title = feature_data.get("first_title", feature.first_title)
            feature.features_name = feature_data.get("features_name", feature.features_name)
            feature.second_title = feature_data.get("second_title", feature.second_title)
            feature.benefits_name = feature_data.get("benefits_name", feature.benefits_name)
            
            # --contact section--
            contact_data = recivedJsonData.get("contactSection",{})
            contact.title = contact_data.get("title", contact.title)
            contact.number = contact_data.get("number", contact.number)
            
            #--- product Section --
            productDetails_data = recivedJsonData.get("productDetails",{})
            product.name = productDetails_data.get("name", product.name)
            product.quantity = productDetails_data.get("quantity", product.quantity)
            product.price = productDetails_data.get("price", product.price)
            product.insideDhaka = productDetails_data.get("insideDhaka", product.insideDhaka)
            product.outsideDhaka = productDetails_data.get("outsideDhaka", product.outsideDhaka)
            
            #--- Gallery section
            galleryDetails_data = recivedJsonData.get("gellerySection",{})
            gallery.title = galleryDetails_data.get("title", gallery.title)
            gallery.description = galleryDetails_data.get("description", gallery.description)
            
            #---save every section----
            font.save()
            feature.save()
            contact.save()
            product.save()
            gallery.save()
            
            
            return JsonResponse({"received_back": recivedJsonData}) # working for print data in console log
        except Exception as e:
            return JsonResponse({"error" : str(e)}, status=500)
        
    # return JsonResponse({"error": "Invalid request"}, status=400) # if method is not post the show this error
    
    
    # make a dichonary in list for json gallery photos data
    photos = []
    for ph in galleryImg.photos.all():
        
        photo = {
                    "id":ph.id, 
                    "name": ph.name, 
                    "photo_asset": ph.photo_asset
                }
        photos.append(photo)
        
    
    
    # Sample data simulating what's in your database
    jsonSiteData = {
            "fontSection": { 
                            "small_title": font.small_title, 
                            "big_title": font.big_title, 
                            "font_asset": font.font_asset, 
                            "details": font.details, 
                            },
            "featureSection":{ 
                                "first_title": feature.first_title, 
                                "features_name": feature.features_name, 
                                "second_title": feature.second_title, 
                                "benefits_name": feature.benefits_name 
                            },
            "gellerySection":{ 
                                "title": gallery.title, 
                                "description": gallery.description, 
                                "photos":photos 
                            },
            "productDetails":{ 
                                "name": product.name, 
                                "quantity": product.quantity, 
                                "price": product.price, 
                                "insideDhaka": product.insideDhaka, 
                                "outsideDhaka": product.outsideDhaka 
                            },
            "contactSection":{ 
                                "title": contact.title, 
                                "number": contact.number 
                            }
    }
    
    context ={
        "jsonSiteData_json": json.dumps(jsonSiteData, default=str),  # convert datetime to string
    }
    
    return render(request, 'admin/content.html', context)

from django.contrib.auth.models import User
def test_template(request):
    

    print(User.objects.all())

    return render(request, 'test_template.html')
