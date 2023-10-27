from django.db import models

# Create your models here.

class Product(models.Model):
      name = models.CharField(max_length=100)
      slug = models.SlugField(max_length=100)
      is_digital = models.BooleanField(default=False)
      
      def __str__(self):
            return self.name