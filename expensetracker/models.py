from django.db import models

class Expense(models.Model):
    title=models.CharField(max_length=100)
    amount=models.FloatField()
    category=models.CharField(max_length=300)
    date=models.DateField()

    def __str__(self):
        return f"{ self.title} - {self.amount} - {self.category} - {self.date}"
    
        
# Create your models here.
