from turtle import onclick
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.http import HttpResponse

from Unversity.models import Unversity

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unversity = models.ForeignKey(Unversity, on_delete = models.CASCADE,blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    living_place = models.CharField(max_length= 50,blank=True, null=True)
    image = models.ImageField(default = 'default.jpg',upload_to =  'images_of_students',blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True) #رقم الهوية
    #specific
    specialization = models.CharField(max_length= 50,blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
    achieved_hours = models.PositiveIntegerField(default='40')
    still_hours = models.IntegerField(default='100')
    Cumulative_average = models.IntegerField(default='80')#المغدل التراكمي
    seimester_average = models.IntegerField(default='80')#المعدل الفصلي
    price_of_hour = models.IntegerField(blank=True, null=True)#سعر الساعة
    unversity_id_number = models.BigIntegerField(blank=True, null=True) #الرقم الجامعي
    comment_about_behavoir = models.TextField(max_length= 50,blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.user} Profile"
        
    def get_absolute_url(self):
        return reverse("detail_profile", kwargs={"pk": self.pk})

    

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
