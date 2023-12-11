from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Shop(models.Model):
    shop_name = models.CharField(
        max_length=50,
        verbose_name='Shop Name'
    )
    shop_reg_id= models.CharField(
        max_length=50,
       
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    status=models.IntegerField(default=0)
    