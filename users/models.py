from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'admin'
        STUFF = "STUFF",'stuff'
        SUPPLIER = "SUPPLIER",'supplier'
        AFFILLIATE = "AFFILLIATE",'affilliate'
        CUSTOMER = "CUSTOMER",'customer'
    base_role = Role.ADMIN
    role = models.CharField(max_length=50,choices=Role.choices)

    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)
    


class AdminManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.ADMIN)

class AdminUser(User):
    admin = AdminManager()
    base_role = User.Role.ADMIN

    class Meta:
        proxy = True

class AdminProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True,blank=True)

@receiver(post_save,sender=AdminUser)
def create_admin_profile(sender,instance,created,**kwargs):
    if created and instance.role ==  "ADMIN":
        AdminProfile.objects.create(user=instance)




class StuffManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.STUFF)


class StaffUser(User):
    stuff = StuffManager()
    base_role = User.Role.STUFF

    class Meta:
        proxy = True


class StuffProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True,blank=True)

@receiver(post_save,sender=StaffUser)
def create_admin_profile(sender,instance,created,**kwargs):
    if created and instance.role ==  "STUFF":
        AdminProfile.objects.create(user=instance)



class SupplierManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.SUPPLIER)

class SupplierUser(User):
    supplier = SupplierManager()
    base_role = User.Role.SUPPLIER

    class Meta:
        proxy = True

class SupplierProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True,blank=True)
    is_verified = models.BooleanField(default=False,null=True,blank=True)
    contact = models.CharField(max_length=200,null=True,blank=True)

@receiver(post_save,sender=SupplierUser)
def create_admin_profile(sender,instance,created,**kwargs):
    if created and instance.role ==  "SUPPLIER":
        SupplierProfile.objects.create(user=instance)


class CustomerManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.CUSTOMER)

class CustomerUser(User):
    customer = CustomerManager()
    base_role = User.Role.CUSTOMER

    class Meta:
        proxy = True

class CustomerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True,blank=True)

@receiver(post_save,sender=CustomerUser)
def create_customer_profile(sender,instance,created,**kwargs):
    if created and instance.role ==  "CUSTOMER":
        CustomerProfile.objects.create(user=instance)        


class AffilliateManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.AFFILLIATE)

class AffiliateUser(User):
    affilliate = AffilliateManager()
    base_role = User.Role.AFFILLIATE

    class Meta:
        proxy = True

class AffilliateProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True,blank=True)

@receiver(post_save,sender=AffiliateUser)
def create_admin_profile(sender,instance,created,**kwargs):
    if created and instance.role ==  "AFFILLIATE":
        AffilliateProfile.objects.create(user=instance)        


    





    
   

