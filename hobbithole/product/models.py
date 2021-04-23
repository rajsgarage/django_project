from django.db import models #default
from io import BytesIO 
from PIL import Image #pillow 
from django.core.files import File


# Create your models here.
# Here we describe what kid of info we will have in DB
# variables in DB - structure

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField() #address version of name

    class Meta:
        ordering = ('name',)
        #order category by name in backend
        #tuple needs comma
    
    #string repreoesent of obj, obj.___ instead have str
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    #if u delete category delete all prducts related to it

    name = models.CharField(max_length=255)
    slug = models.SlugField() 
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    #not necessary to have image
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True) #adds date whenever we create object

    class Meta:
        ordering = ('-date_added',)
        #order by date, minus is for descending
    
    #string repreoesent of obj, obj.___ instead have str
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/' #get slug based on category

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url 
            #if img exists return urls so easier to use in frontend
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url 
        
        #if no thumbnail, make on using img if it exists
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image) #this func needs to be defined
                self.save() #save in db
                return 'http://127.0.0.1:8000' + self.thumbnail.url 
            else : 
                return '' #empty str if no thumbnail possible

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)

        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail







