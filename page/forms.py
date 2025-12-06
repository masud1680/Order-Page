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
        

# class FontSectionForm(forms.ModelForm):
#     class Meta:
#         model = FontSection
#         fields = ['name', 'small_title', 'big_title', 'font_asset', 'details']



class TailwindFormMixin:
    """
    Apply Tailwind classes to all fields in a form automatically.
    """
    tailwind_class = "block w-full px-4 py-2 mb-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition duration-200"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Add the tailwind class to all widgets
            existing_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{existing_class} {self.tailwind_class}".strip()


class FontSectionForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = FontSection
        fields = ['name','small_title', 'big_title', 'font_asset', 'details']
        widgets = {
            'font_asset': forms.ClearableFileInput(attrs={
                'class': 'file:py-2 file:px-4 file:border-0 file:rounded-lg file:text-sm file:font-semibold file:bg-indigo-100 file:text-indigo-700 hover:file:bg-indigo-200',
            }),
        }
        
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
        
class PhotoSectionForm(TailwindFormMixin,forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'photo_asset']

    
class ProductDetailsFrom(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['name', 'quantity', 'price', 'insideDhaka', 'outsideDhaka']

# using for admin update content page
class FontSectionImageForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = FontSection
        fields = [ 'font_asset']
        widgets = {
            'font_asset': forms.ClearableFileInput(attrs={
                'class': 'file:py-2 file:px-4 file:border-0 file:rounded-lg file:text-sm file:font-semibold file:bg-indigo-100 file:text-indigo-700 hover:file:bg-indigo-200',
            }),
        }
        





