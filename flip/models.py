from django.db import models

# Create your models here.
class contact(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    subject=models.TextField()
    
def __str__(self):
        return f"{self.firstname} {self.lastname}"
