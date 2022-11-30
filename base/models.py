from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique = True)
    email = models.EmailField(null =True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    

class Branch(models.Model):
    branchid = models.CharField(db_column='BranchID', primary_key=True, max_length=6)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', unique=True, max_length=100)  # Field name made lowercase.
    phonenum = models.CharField(db_column='PhoneNum', unique=True, max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'
        
class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=10)  # Field name made lowercase.
    citizenid = models.CharField(db_column='CitizenID', unique=True, max_length=12)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=45)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', unique=True, max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    point = models.PositiveIntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    customertype = models.PositiveIntegerField(db_column='CustomerType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'
        
        
class Booking(models.Model):
    bookingid = models.CharField(db_column='BookingID', primary_key=True, max_length=20)  # Field name made lowercase.
    bookingdate = models.DateTimeField(db_column='BookingDate')  # Field name made lowercase.
    guestnum = models.PositiveIntegerField(db_column='GuestNum')  # Field name made lowercase.
    checkin = models.DateTimeField(db_column='CheckIn')  # Field name made lowercase.
    checkout = models.DateTimeField(db_column='CheckOut')  # Field name made lowercase.
    status = models.PositiveIntegerField(db_column='Status')  # Field name made lowercase.
    totalpay = models.PositiveIntegerField(db_column='TotalPay')  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    packagename = models.ForeignKey('ServicePacket', models.DO_NOTHING, db_column='PackageName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'
        
class ServicePacket(models.Model):
    packagename = models.CharField(db_column='PackageName', primary_key=True, max_length=50)  # Field name made lowercase.
    daynum = models.PositiveIntegerField(db_column='DayNum')  # Field name made lowercase.
    guestnum = models.PositiveIntegerField(db_column='GuestNum')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service_packet'
        
        
class RoomType(models.Model):
    roomid = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=45)  # Field name made lowercase.
    area = models.PositiveIntegerField(db_column='Area')  # Field name made lowercase.
    numguest = models.PositiveIntegerField(db_column='NumGuest')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'room_type'
        
class SupplyType(models.Model):
    sppid = models.CharField(db_column='SppID', primary_key=True, max_length=6)  # Field name made lowercase.
    sppname = models.CharField(db_column='SppName', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supply_type'
        
        
class RoomTypeSupplyType(models.Model):
    sppid = models.OneToOneField('SupplyType', models.DO_NOTHING, db_column='SppID', primary_key=True)  # Field name made lowercase.
    roomid = models.ForeignKey(RoomType, models.DO_NOTHING, db_column='RoomID')  # Field name made lowercase.
    quantity = models.PositiveIntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        
        db_table = 'room_type_supply_type'
        unique_together = (('sppid', 'roomid'),)
        
        
class BedInfo(models.Model):
    roomid = models.OneToOneField('RoomType', models.DO_NOTHING, db_column='RoomID', primary_key=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=2, decimal_places=1)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        
        db_table = 'bed_info'
        unique_together = (('roomid', 'size'),)
        
        