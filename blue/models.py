
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class categoriesPRODUCT(models.Model):
    namecategorie = models.CharField(max_length=100)

    def __str__(self):
        return self.namecategorie
class profile(models.Model):
    image1 = models.ImageField(upload_to='product_images/')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories1 = models.ForeignKey(categoriesPRODUCT, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/')
    image3 = models.ImageField(upload_to='product_images/',blank=True)
    image4 = models.ImageField(upload_to='product_images/',blank=True)
    image5 = models.ImageField(upload_to='product_images/',blank=True)
    details = models.TextField()

    def __str__(self):
        return self.name
    
from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')

    def __str__(self):
        return self.title