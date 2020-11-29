from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    sal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, salary: {self.sal}"
