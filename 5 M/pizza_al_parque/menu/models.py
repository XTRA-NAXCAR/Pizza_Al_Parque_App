from django.db import models

# Create your models here.
class Type (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Food (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    type_by = models.ForeignKey(Type, on_delete=models.CASCADE, db_column='type_by')
