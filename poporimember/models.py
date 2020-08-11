from django.db import models
from django.contrib.auth.models import AbstractUser
import birthday
# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    # interested_popori = 해시태그로 해야될듯
    birth = models.DateTimeField(null=True, blank=False)
    # email =
   
    

    class Meta:
        verbose_name = "이용자 리스트"
        verbose_name_plural = "popori 이용자 ^^"
        
    