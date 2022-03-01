from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Finance(models.Model):
    Finance_name = models.CharField(max_length= 60, default="file name",)
    Finance_student = models.ForeignKey(User, on_delete= models.CASCADE)
    finance_reports = models.FileField(upload_to= 'finance_reports') #التقارير المالية
    date = models.DateTimeField(auto_now = True , null = True)

    def __str__(self):
        return self.Finance_name
        
    def get_absolute_url(self):

        return reverse('detail_files' , kwargs={'pk' : self.pk})