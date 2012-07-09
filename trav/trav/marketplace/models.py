from django.db import models
from taggit.managers import TaggableManager
from trav.settings import STATICFILES_DIRS
class usr(models.Model):
    username=models.CharField(max_length=30,unique=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    def __unicode__(self):
        return self.username

class profile(models.Model):
    userid=models.IntegerField()
    plcvisited=models.CharField('Places visited',max_length=30)
    plctovisit=models.CharField('Places to Visit',max_length=30)
    user_rating=models.IntegerField('User rating',default=3)
    user_feedback=models.TextField('Feedback')
    def __unicode__(self):
        return self.plcvisited
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    image=models.ImageField(upload_to=STATICFILES_DIRS)
    details=models.TextField()
    sellerid=models.IntegerField()
    expiration_date=models.DateField(null=True,blank=True)
    price=models.DecimalField(max_digits=19,decimal_places=4)
    price=models.DecimalField(max_digits=15,decimal_places=4)
    tags = TaggableManager()  