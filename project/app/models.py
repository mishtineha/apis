from django.db import models
from django.contrib.auth.models import User
class Address(models.Model):
    Street_add = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
class Profile(models.Model):
    Name = models.CharField(max_length = 50,null = False,blank = False)
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = False,blank = False)
    phone_number = models.CharField(max_length = 30, unique = True)
    gender = models.CharField(max_length = 50)
    profile_pic = models.ImageField(upload_to = "post1_image",blank = True,null = True)
    dob = models.DateTimeField(auto_now_add = True,null = True,blank = True)
    per_add = models.OneToOneField(Address,on_delete=models.CASCADE,related_name ='per_address',null = True,blank = True)
    company_add = models.OneToOneField(Address,on_delete=models.CASCADE,related_name = 'company_address',null = True,blank = True)
    Friends = models.ManyToManyField('self',symmetrical=False,null = True,blank = True)
    
    def profile_pic_tag(self):
        return u'<img src = "%s" />' % self.profile_pic
    profile_pic_tag.allow_tags = True
    
    profile_pic_tag.short_description = 'profile_pic'
    def __str__(self):
        return self.user.username+'    '+self.phone_number+' '+str(self.profile_pic)
        
       
    


# Create your models here.
