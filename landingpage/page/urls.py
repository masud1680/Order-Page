from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_template, name='test'),
    path('order-create', views.order_create_landing_page, name='order-create'),
    path('product-details/', views.product_details, name='product-details'),
    path('landing-page/', views.landing_page, name='landing-page'),
    path('myorder-view/', views.myorder_view, name='myorder-view'),
    path('order-success/', views.ordersuccess, name='order-success'),
    
    # Admin Dashboard spacific Url
    path('admin-dashboard/', views.admin_dashboard , name='admin-dashboard'),
    path('update/font-section/', views.update_font_section, name='update-font-section'),
    path('update/feature-section/', views.update_feature_section , name='update-feature-section'),
    path('update/contact-section/', views.update_contact_section , name='update-contact-section'),
    path('update/gallery-section-data/', views.update_gallery_section_data , name='update-gallery-section-data'),
    path('update/gallery-section-photo/', views.update_gallery_section_photo , name='update-gallery-section-photo'),
    path('delete/gallery-section-photo/', views.delete_gallery_section_photo , name='delete-gallery-section-photo'),
    path('update/product-details/', views.updateProductDetails , name='product-details'),
]