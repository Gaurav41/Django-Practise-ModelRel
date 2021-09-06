from django.db import models
from django.db.models.fields.related import ForeignKey
# Relationships
# one to one
class AppUser(models.Model):
    user_name = models.CharField(max_length=70,null=False)
    password = models.CharField(max_length=70)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user_name

# on_delete=models.CASCADE = if we delete Emp, aadhar will delete automatically
# on_delete=models.PROTECT = we have to delete adhar first thn user. 
# on_delete=models.SET_NULL = set null (null = True must be there)
# limit_choices_to={'is_staff':True}, onlye emp who are staff can add adhar info


class UserDetails(models.Model):
    appuser = models.OneToOneField(AppUser,on_delete=models.CASCADE,primary_key=True)
    # employee = models.OneToOneField(AppUser,on_delete=models.PROTECT,primary_key=True)
    # employee = models.OneToOneField(AppUser,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})

    aadhaar_no = models.CharField(max_length=12,unique=True)
    mobile_no = models.IntegerField()
    updated_on = models.DateField(auto_now_add=True)

# model inheritance and one to one relationship
class Temp(UserDetails):
    user = models.OneToOneField(UserDetails,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()


# Many to one Relationship
# 
# tables - appuser and post
  
class Post(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_des = models.CharField(max_length=500) 
    post_publish_date = models.DateField(auto_now_add=True)


# Many to Many Relationship
# tables - appuser and product

class Product(models.Model):
    user = models.ManyToManyField(AppUser)
    prod_name = models.CharField(max_length=50)
    prod_price = models.IntegerField()

    def ordered_by(self):
        return ",".join([str(u) for u in self.user.all()])

