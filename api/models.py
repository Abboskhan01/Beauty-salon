from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cosmetic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return self.name
