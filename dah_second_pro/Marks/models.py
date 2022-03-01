from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Marks(models.Model):
    
    mark_student = models.ForeignKey(User, on_delete= models.CASCADE)
    marks_name = models.CharField(max_length= 200, default= 'marks'
            ,help_text='من فضلك ادخل تفاصيل العلامة')
    marks = models.FileField(upload_to = 'grades') # كشف الدرجات
    date = models.DateTimeField(auto_now=True , null = True)
    
    def __str__(self):
        return self.marks_name

    def get_absolute_url(self):
        return reverse("Mark_Detail", kwargs={"pk": self.pk})
        