from django.db import models
from django.urls import reverse
# Create your models here.
#have memory of product
class Product(models.Model):
    #mapping to database
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True,null = True)
    price       = models.DecimalField(decimal_places = 2,max_digits = 1000)
    summary     = models.TextField(blank = False,null = False)
    #blank has to be related to field and null is related to dabase
    feature     = models.BooleanField(default = True)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("product-dtail",kwargs = {"my_id":self.id })
