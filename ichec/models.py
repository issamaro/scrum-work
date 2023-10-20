from django.db import models
from django.urls import reverse

# Create your models here.
class Master(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    
    def get_courses(self):
        return self.master_courses.all()
        
    def get_absolute_url(self):
        return reverse('ichec:master_detail', kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.title}"
    
class Course(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name="master_courses")
    credits = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.title}"