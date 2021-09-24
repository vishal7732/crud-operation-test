from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    tag = models.ManyToManyField(Tag)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False)
    image = models.ImageField(upload_to='images/', default=True)
    describtion = models.CharField(max_length=200)

    def __str__(self):
        return self.name