from django.shortcuts import render, HttpResponse,redirect
from .models import OrderModel, FontSection, FeatureSection, ContactSection, GellerySection, Photo, ProductDetails
from .forms import  PlaceOrderForm, FontSectionForm, FeatureSectionForm, ContactSectionForm, GellerySectionForm, PhotoSectionForm, ProductDetailsFrom


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
    
    return render(request, 'landing_page3.html', context)

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
        
    return render(request, 'form.html', {'form' : form})
    
def update_gallery_section_data(request):
    GellerySectionDetails = GellerySection.objects.get(id = 1)

    form = GellerySectionForm(instance=GellerySectionDetails) # instance=GellerySectionDetails
    
    if request.method == 'POST':
        form = GellerySectionForm(request.POST, instance=GellerySectionDetails)
        
        
        if form.is_valid():
            form.save()
                    
            return redirect('landing-page')
     
    return render(request, 'form.html', {'form' : form} )
    
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
    
    return render(request, 'form.html',  {'form' : form}  )

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
    return render(request, "form.html", {"form" : form})   


def myorder_view(request):
    if request.method == 'POST':
        query = request.POST['search']
       
        MyallOrder = OrderModel.objects.filter(phone = query).order_by('-order_created_at')
        
    else:
        MyallOrder = OrderModel.objects.none()
    return render(request, 'myorder_view.html',{'MyallOrder' : MyallOrder})
    
def order_create(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            if request.user:
                order = form.save(commit = False)
                order.user = request.user
                order.save()
                return redirect('ordersuccess')
                # return HttpResponse('order complete.')
            else:
                form.save()
                return HttpResponse('order complete.')
    else:
        form = PlaceOrderForm()
    
    return render(request, 'order_page.html', {'form' : form})

def order_create_landing_page(request):
    
    # collect data from django template
    if request.method == 'POST':
        name = request.POST('name')
        phone = request.POST('phone')
        address = request.POST('address')
        comment = request.POST('comment')
        area = request.POST('area')
        product_name = request.POST('product_name')
        quantity = request.POST('quantity')
        price = request.POST('price')
        delivery_change = request.POST('delivery_charge')
        total_price = request.POST('total_price')
        payment_method = request.POST('payment_method')
        transaction_method = request.POST('transaction_method')
        transaction_id = request.POST('transaction_id')
        
        # Save data to database
        
        OrderModel.objects.create(
            name = name,
            phone = phone,
            address = address,
            comment = comment,
            area = area,
            product_name = product_name,
            quantity = quantity,
            price = price,
            delivery_change = delivery_change,
            total_price = total_price,
            payment_method = payment_method,
            transaction_method = transaction_method,
            transaction_id = transaction_id
        )
        
        return redirect('order-success')
    return HttpResponse('Order Field!!')

def ordersuccess(request):
    return render(request, 'order_success.html')


def admin_dashboard(request):
    
    
    return render(request, 'admin/main_dashboard.html')

def test_template(request):
    
    
    return render(request, 'test_template.html')
