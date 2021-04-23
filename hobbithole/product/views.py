from django.shortcuts import render

#added
from .serializers import ProductSerializer
from .models import Product

#added
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.http import Http404

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4] #getting latest
        serializer = ProductSerializer(products, many=True) #more than 1 obj
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
            #return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)