from . import views
from django.urls import path,include

urlpatterns = [
   path('',views.homePage,name='home'),
   path('about/', views.about, name='about'),
   path('product/<int:pk>',views.product,name='product'),
   path('category/<str:foo>',views.category,name='category'),

]
