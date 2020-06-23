from django.db import models
from django.contrib.auth.models import User
import uuid
from django.template.defaultfilters import  slugify
from phonenumber_field.modelfields import  PhoneNumberField
from django.utils import timezone

# Create your models here.

my_choices = (
    ('one','number one'),
    ('two', 'number two')
)

class TestModel(models.Model):
    boolean = models.BooleanField(default=True,verbose_name="This is a boolean Field")
    char    = models.CharField(verbose_name="New Name",max_length=220,unique=True,help_text="This is the help text")
    date    = models.DateField(default=timezone.now)
    decimal = models.DecimalField(max_digits=5 , decimal_places=2)
    email   = models.EmailField(max_length=200)
    file    = models.FileField(upload_to='uploads',blank=True)
    image   = models.ImageField(upload_to='uploads',blank=True)
    integer = models.IntegerField()
    pos_sm_int= models.PositiveIntegerField()
    slug    = models.SlugField(blank=True)
    text    = models.TextField()
    url     = models.URLField(max_length=200)
    uuid1   = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    date_time= models.DateTimeField()
    choice  = models.CharField(max_length=10,choices=my_choices)

    phone_number = PhoneNumberField()

    new_field = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 


    def save(self,*args,**kwargs):
        self.slug = slugify(self.text[:30])
        super(TestModel,self).save(*args,**kwargs)


    def __str__(self):
        return "{0}".format(self.new_field)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio  = models.TextField()
    profile_picture = models.ImageField(blank=True)
    website = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # String method to return the object 
    def __str__(self):
        return "{0} - {1}".format(self.user.first_name,self.user.last_name)