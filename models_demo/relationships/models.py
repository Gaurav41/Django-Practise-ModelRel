from django.db import models
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
# limit_choices_to={'is_staff':True}, onlye emp who are staff can add adhar info


class UserDetails(models.Model):
    appuser = models.OneToOneField(AppUser,on_delete=models.CASCADE,primary_key=True)
    # employee = models.OneToOneField(AppUser,on_delete=models.PROTECT,primary_key=True)
    # employee = models.OneToOneField(AppUser,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})

    aadhaar_no = models.CharField(max_length=12,unique=True)
    mobile_no = models.IntegerField()
    updated_on = models.DateField(auto_now_add=True)


# class Temp(UserDetails):
#     user = models.OneToOneField(UserDetails,on_delete=models.CASCADE,primary_key=True)
#     likes = models.IntegerField()