from django.db import models
 
class Log_In_ID(models.Model):
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    class Meta:
        db_table = 'login'



class Data(models.Model):
    name = models.CharField(max_length=190)
    mobile = models.IntegerField()
    email = models.CharField(max_length=190)
    address = models.CharField(max_length=190)
    pincode = models.IntegerField()
    idproof = models.CharField(max_length=190)
    idnumber = models.IntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    # Idproof = models.CharField(max_length=255)
   
    class Meta:
        db_table = 'booking'


class FoodList(models.Model):
    name = models.CharField(max_length=190)
    mobile = models.IntegerField()
    time = models.DateTimeField()
    item = models.CharField(max_length=190)
    quantity = models.IntegerField()
    class Meta:
        db_table = 'food'


class Query(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class Meta:
        db_table = 'query'


class Bill(models.Model):
    transactionId = models.CharField(max_length=190)
    name = models.CharField(max_length=190)
    date = models.DateTimeField()
    total = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    class Meta:
        db_table = 'invoice'

