from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Name = models.CharField(max_length=200)
    Price_one_month = models.IntegerField(max_length=10 ,null=True)
    Price_three_month  = models.IntegerField(max_length=10,null=True)
    Price_six_month  = models.IntegerField(max_length=10,null=True)
    Price_yearly  = models.IntegerField(max_length=10,null=True)


    def __str__(self):
        return self.Name

class Members_form(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField(max_length=10)
    Mobile_No = models.IntegerField(max_length=10)  
    Height = models.IntegerField(max_length=10)
    Weight = models.IntegerField(max_length=10)
    Address = models.TextField(null = True , blank =True)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , null= True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)


    def __str__(self):
        return self.First_Name + " " + self.Last_Name



class Demo_Members_form(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField(max_length=10)
    Mobile_No = models.IntegerField(max_length=10)
    Height = models.IntegerField(max_length=10)
    Weight = models.IntegerField(max_length=10)
    Address = models.TextField(null = True , blank =True)
   

    def __str__(self):
        return self.First_Name + " " + self.Last_Name