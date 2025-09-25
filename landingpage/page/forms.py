from django import forms
from .models import OrderModel, FontSection, FeatureSection, ContactSection, GellerySection, Photo, ProductDetails
from django.forms import modelformset_factory

class AdminUpadteOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['status','name','phone','address','comment','product_name', 'quantity', 'price', 'total_price', 'delivery_charge',  'location_choice', 'payment_method']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md',
                'placeholder': 'Enter your name'
            }),
            'product_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md',
                'placeholder': 'Enter your name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'block w-full rounded-md p-4 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md',
                'placeholder': 'Enter your phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md',
                'rows': 3,
                'placeholder': 'Enter your address'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md',
                'rows': 3,
                'placeholder': 'Enter your address'
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'price': forms.TextInput(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'total_price': forms.TextInput(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'delivery_charge': forms.TextInput(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'location_choice': forms.Select(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'status': forms.Select(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'block w-full p-4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-md'
            }),
        }
        

class FontSectionForm(forms.ModelForm):
    class Meta:
        model = FontSection
        fields = ['name', 'small_title', 'big_title', 'font_asset', 'details']
        
class FeatureSectionForm(forms.ModelForm):
    class Meta:
        model = FeatureSection
        fields = ['name', 'first_title', 'features_name', 'second_title', 'benefits_name']
        
class ContactSectionForm(forms.ModelForm):
    class Meta:
        model = ContactSection
        fields = ['title', 'number']
        
class GellerySectionForm(forms.ModelForm):
    class Meta:
        model = GellerySection
        fields = ['title', 'description']
        
class PhotoSectionForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'photo_asset']
    
class ProductDetailsFrom(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['name', 'quantity', 'price', 'insideDhaka', 'outsideDhaka']
        





