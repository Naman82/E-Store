from django.db import models
import os, uuid

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255,null=True)
    category_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Inventory(models.Model):
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quantity

class Discount(models.Model):
    name = models.CharField(null=True,max_length=255)
    desc = models.TextField()
    discount_perct = models.DecimalField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    def get_update_filename(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('uploads/product/', filename)

    user = models.ForeignKey("users.User",on_delete=models.CASCADE)
    product_name = models.CharField(null=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    product_image = models.ImageField(upload_to=get_update_filename, default='uploads/product/default_profile.jpg')
    sku = models.CharField(null=True,max_length=255)
    price = models.DecimalField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


