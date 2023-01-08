from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=50) 
    price = models.PositiveIntegerField()
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
