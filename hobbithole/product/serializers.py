from rest_framework import serializers

#since we;re in same folder .models can be used
from .models import Category, Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )
        #field= '__all__'
