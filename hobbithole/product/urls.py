from django.urls import path, include

#from .views import LatestProductsList //LatestProductsList
from product import views
#from .views import LatestProductsList
urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    
]