from django.db import models
from django.contrib import admin
# Create your models here.
#user
class Seller(models.Model):
    seller = models.IntegerField(null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    isfgpwd = models.BooleanField(default=False)
    resname = models.TextField()
    resaddress = models.TextField()
    resphone = models.TextField()
    resphoto = models.ImageField(upload_to='../media/images/resphoto/', default='defaultuser1.png')
    resintroduce = models.TextField()
    resopentime = models.TextField()
    resnotice = models.TextField()
    resother = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True, editable=True)
    #update_time = models.DateTimeField(auto_now=True, null=True)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('seller', 'username', 'email')
admin.site.register(Seller, SellerAdmin)
#dish
class Dish(models.Model):
    seller = models.IntegerField()
    username = models.CharField(max_length=50)
    dishname = models.CharField(max_length=50)
    dishphoto = models.ImageField(upload_to='../media/images/dishphoto/original/', default='../../static/images/business/defaultdish1.png')
    dishprice = models.CharField(max_length=50)
    dishintroduce = models.TextField()
    dishkind = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add=True, editable=True)
    #update_time = models.DateTimeField(auto_now=True, null=True)
class DishAdmin(admin.ModelAdmin):
    list_display = ('seller', 'username', 'dishname')
admin.site.register(Dish, DishAdmin)
#table
class Table(models.Model):
    seller = models.IntegerField()
    username = models.CharField(max_length=50)
    tablenum = models.CharField(max_length=50)
    tableperson = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add=True, editable=True)
    #update_time = models.DateTimeField(auto_now=True, null=True)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seller', 'username', 'tablenum', 'tableperson')
admin.site.register(Table, TableAdmin)


##test
#class Orderlist(models.Model):
#    customer = models.CharField(max_length=50)
#    business = models.CharField(max_length=50)
#    time = models.DateTimeField(auto_now_add=True, editable=True)
#    price = models.CharField(max_length=50)
#    is_ok = models.BooleanField(default=False)
#    dishname = models.CharField(max_length=50)
#    dishnumber = models.CharField(max_length=50)
#class OrderlistAdmin(admin.ModelAdmin):
#    list_display = ('customer', 'business', 'price')
#admin.site.register(Orderlist, OrderlistAdmin)
