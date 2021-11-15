from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import BooleanField, IntegerField
from datetime import datetime
from croniter import croniter
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
# Create your models here.

class Parent(models.Model):
    # orders = models.ForeignKey(Order, null=True, on_delete= models.SET_NULL)

    
    # referals = IntegerField(default = 0,blank=True,null=True)
    # code = models.CharField(max_length=12,blank=True, null=True)
    # refered_by = models.CharField(max_length=200,blank=True, null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    parent_name = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    email = models.CharField(max_length=200, null=True)
    

    # is_token_valid = BooleanField(default=False,blank=True,null=True)
    
	# profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # is_shortlisted = BooleanField(default=False,blank=True,null=True)

    def __str__(self):
	    return self.user.username
    
    # def save(self,*args, **kwargs):
    #     print("in save")
    #     print(self.code)
    #     if self.code is None:
    #         # code = 45
    #         code = generate_ref_code()
    #         self.code = code
    #         print("code printed")
    #     super(Customer,self).save(*args, **kwargs)


class Child(models.Model):
    parent = models.ForeignKey(Parent, null=True, on_delete= models.CASCADE)
    child_name = models.CharField(max_length=250,null=True)
    child_gender = [
        ('Boy','Boy'),
        ('Girl','Girl'),
    ]
    child_gender = models.CharField(max_length=250,null=False,choices=child_gender,default='---')
    child_Age_attributes = [
        ('Days','Days'),
        ('Weeks','Weeks'),
        ('Year','Year'),


    ]
    date_of_birth = models.DateField()

    child_age_integer = models.IntegerField(default=1)
    child_age_attributes = models.CharField(max_length = 20 ,default='---',choices=child_Age_attributes)
    child_age_in_days = models.IntegerField(null=True,blank=True)
    


    # address = models.CharField(max_length=250,null = True)
    # alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # numeric = RegexValidator(r'^[0-9]*$', 'Only Numbers are allowed.')
    # adhar_card_number = models.CharField(max_length=12,null = True,validators=[alphanumeric])
    # age = models.CharField(max_length=14,null = True,blank=True,validators=[numeric])
    # website_address = models.CharField(max_length=250,null=True)
    
    # state = models.CharField(max_length=250,null = True)
    # country= models.CharField(max_length=250,null = True)
    
    def __str__(self):
            return self.child_name

    def save(self,*args, **kwargs):
        print("in save")
        print(self.child_age_integer)
        if self.child_age_in_days is None:
            if self.child_age_attributes == 'Days':
                self.child_age_in_days = self.child_age_integer
            elif self.child_age_attributes == 'Weeks':
                self.child_age_in_days = self.child_age_integer*7
            elif self.child_age_attributes == 'Year':
                self.child_age_in_days = self.child_age_integer*365
            from datetime import date
            # d0 = date(2017, 8, 18)
            # d1 = date(2017, 10, 26)
            delta = date.today() - self.date_of_birth
            print(delta.days)


            print("code printed")
        super(Child,self).save(*args, **kwargs)



class Vaccine(models.Model):
    # customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    vaccine_name = models.CharField(max_length=250,null=True)
    vaccine_use =  models.CharField(default="Something", max_length=250,null=True)
    child_Age = [
        ('Birth','Birth'),
        ('6 weeks','6 weeks'),
        ('10 weeks','10 weeks'),
        ('14 weeks','14 weeks'),
        ('6 months',' 6 months'),
        ('7 months','7 months'),
        ('9 months','9 months'),
        ('12 months','12 months'),
        ('13 months','13 months'),
        ('15 months','15 months'),
        ('16-18 months','16-18 months'),
        ('18 months','18 months'),
        ('4-6 years','4 - 6 years'),
        ('9 years','9 years'),
        ('9 years 6 months','9 years 6 months'),
        ('10 years','10 years'),


    ]
    to_be_taken_age =  models.CharField(max_length = 20,choices=child_Age,default="Birth")
    to_be_taken_age_in_days =  models.IntegerField(null=True,blank=True)
    to_be_taken_by = [
        ('Both','Both'),
        ('Boys','Boys'),
        ('Girls','Girls')

    ]
    to_be_taken_by = models.CharField(max_length = 20,choices=to_be_taken_by,default='Both')
    Added_on = models.DateField(auto_now_add=True)
    next_date = models.DateField(null=True,blank=True)

    def save(self,*args, **kwargs):
        print("in save")
        # print(self.child_age_integer)
        if self.to_be_taken_age_in_days is None:
            if 'weeks' in self.to_be_taken_age:
                self.extract_days = self.to_be_taken_age.replace(" weeks","")
                self.extract_days = int(self.extract_days)
                self.to_be_taken_age_in_days  = self.extract_days*7
            elif 'months' in self.to_be_taken_age:
                self.extract_days = self.to_be_taken_age.replace(" months","")
                self.extract_days = int(self.extract_days)
                self.to_be_taken_age_in_days  = self.extract_days*30
            elif 'years' in self.to_be_taken_age:
                self.extract_days = self.to_be_taken_age.replace(" years","")
                self.extract_days = int(self.extract_days)
                self.to_be_taken_age_in_days  = self.extract_days*365


            elif 'Birth' in self.to_be_taken_age:
                
                self.to_be_taken_age_in_days  = 1
            


                # self.child_age_in_days = self.child_age_integer
            # elif self.child_age_attributes == 'Weeks':
            #     self.child_age_in_days = self.child_age_integer*7
            # elif self.child_age_attributes == 'Year':
            #     self.child_age_in_days = self.child_age_integer*365


            print("code printed")
        super(Vaccine,self).save(*args, **kwargs)
    # to_be_taken_age_in_months =  models.IntegerField(null=True,blank=True)

    def __str__(self):
            return self.vaccine_name
    


    
        

        

        
	    