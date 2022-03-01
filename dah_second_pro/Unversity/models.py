from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Unversity(models.Model):
    Unversity_choice = (
        ('Al_azhar', 'Al_azhar'),
        ('Islamic_Unversity','Islamic_Unversity')
    )
    unversity_name = models.CharField(max_length = 50 , choices = Unversity_choice )
    
    
    def __str__(self) :
        return self.unversity_name