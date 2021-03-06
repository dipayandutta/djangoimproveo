from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from areas.models import ProductionLine
from categories.models import Category
# Create your models here.
hours = ([(str(x) , str(x)) for x in range(1,25)])
class Report(models.Model):
    day = models.DateTimeField(default=timezone.now)
    start_hour = models.CharField(max_length=2,choices=hours)
    end_hour = models.CharField(max_length=2,choices=hours)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.PositiveIntegerField()
    execution = models.PositiveIntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    production_line = models.ForeignKey(ProductionLine,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{0}-{1}-{2}".format(self.start_hour,self.end_hour,self.production_line)


class ProblemReported(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    problem_id = models.CharField(max_length=12,unique=True,blank=True)
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return "{0}-{1}".format(self.category.name,self.description)


    class Meta:
        verbose_name = "Problem Reported"
        verbose_name_plural = "Problems Reported"

