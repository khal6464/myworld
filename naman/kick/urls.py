from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('SignupPage/', views.SignupPage, name='SignupPage'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('list/',views.list_equipment,name='list'),
    path('contact/',views.contact , name='contact'),

    path('listings/<str:category>/', views.listings, name='listings'),

    path('product/<int:product_id>/', views.product, name='product')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
