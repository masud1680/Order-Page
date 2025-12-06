from django.contrib import admin
from .models import OrderModel, FontSection, FeatureSection, GellerySection, ContactSection, ProductDetails, Photo

# Register your models here.

admin.site.register(OrderModel)
admin.site.register(FontSection)
admin.site.register(FeatureSection)
admin.site.register(GellerySection)
admin.site.register(ContactSection)
admin.site.register(ProductDetails)
admin.site.register(Photo)