from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY=(
    ('Phone','Phone'),
    ("Laptop",'Laptop'),
    ('TV',"TV"),
    ('Smart Watches','Smart Watches'),
)

class Product(models.Model):
    name= models.CharField(max_length=100 , null=True)
    category=models.CharField(max_length=20 , choices=CATEGORY ,null=True)
    quantity=models.PositiveIntegerField(null=True)
    
    class Meta:
        verbose_name='Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

#order will be linked with User with user model#


class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE ,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)
      
    class Meta:
        verbose_name='Order'

    def __str__(self):
        return f"{self.product} ordered by {self.staff.username}" #linked staff with user model
