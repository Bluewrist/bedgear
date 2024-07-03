from django.urls import path,include
from. import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('products',views.product_list,name='products'),
    path('product_detai/<int:id>',views.product_detail,name='product_detail')


]
