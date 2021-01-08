from django.db import models
from django.conf import settings

################################# KILOSAHIHI START #############################################
class Cooperatives(models.Model):
    name = models.CharField(max_length=50)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Cooperatives"

class Produce(models.Model):
    name = models.CharField(max_length=50, unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Produce"

class Factories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Produce,on_delete=models.CASCADE,null=True)
    cooperative =  models.ForeignKey(Cooperatives,on_delete=models.CASCADE,null=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Factories/Collection Centres"

class Devices(models.Model):
    name = models.CharField(max_length=50)
    factory = models.ForeignKey(Factories,on_delete=models.CASCADE,null=True)
    imei  = models.CharField(max_length=50, unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Devices"

class Clerk(models.Model):
    name = models.CharField(max_length=50)
    national_id  = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    username  = models.CharField(max_length=50, unique=True)
    password  = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=50, unique=True)
    factory = models.ForeignKey(Factories,on_delete=models.CASCADE,null=True)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Clerks"

class Farmers(models.Model):
    name = models.CharField(max_length=50)
    national_id  = models.CharField(max_length=50, unique=True)
    username  = models.CharField(max_length=50, unique=True)
    password  = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=50, unique=True)
    bank_branch  = models.CharField(max_length=50)
    bank_account_name  = models.CharField(max_length=50)
    bank_account  = models.CharField(max_length=50)
    acres  = models.CharField(max_length=50)
    lat  = models.CharField(max_length=50)
    lon  = models.CharField(max_length=50)
    factory = models.ForeignKey(Factories,on_delete=models.CASCADE,null=True)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farmers"

class Transactions(models.Model):
    tx_code = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    total_payout = models.CharField(max_length=50)
    farmer = models.ForeignKey(Farmers,on_delete=models.CASCADE,null=True)
    device = models.CharField(max_length=100,null=True)
    produce = models.ForeignKey(Produce,on_delete=models.CASCADE,null=True)
    clerk = models.ForeignKey(Clerk,on_delete=models.CASCADE,null=True)
    tx_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Transactions"

class Payment(models.Model):
    payment_code = models.CharField(max_length=50)
    tx_reference = models.ForeignKey(Transactions,on_delete=models.CASCADE,null=True)
    method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Payment"

class Audits(models.Model):
    name = models.CharField(max_length=50)
    # action = models.CharField(max_length=50)
    action = models.TextField()
    user = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Audits"

############################# KILOSAHIHI END #############################################


#################################BAT START #############################################

class Sku(models.Model):
    name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "SKU"

class Products(models.Model):
    name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=50)
    sku = models.ForeignKey(Sku,on_delete=models.CASCADE,null=True)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Products"

class ProductWeights(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    weight  = models.CharField(max_length=50)
    date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Product Weights"

############################# BAT END #############################################

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

#stores all the supplies incoming and outgoing depending on the weigh stage
class Accounts(models.Model):
    name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Accounts"


class Destination(models.Model):
    name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Accounts"

class Origin(models.Model):
    name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Accounts"


class Suppliers(models.Model):
    name = models.CharField(max_length=50)
    account = models.ManyToManyField(Accounts)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Suppliers"

class Weighbridges(models.Model):
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Weighbridges"


class Customers(models.Model):
    name = models.CharField(max_length=50)
    account = models.ManyToManyField(Accounts,related_name="account")
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Customers"


#store the different transporters that bring in the supplies.A transporter can many suppliers and vice versa
class Transporters(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    supplier = models.ManyToManyField(Suppliers)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    contact = models.CharField(max_length=50)
    status =models.CharField(max_length=10)   
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Transporters"

#The different tractors from different transporters related to one transporter
class Vehicle(models.Model):
    name=models.CharField(max_length=50)
    no_plate=models.CharField(max_length=20)
    transporter=models.ForeignKey(Transporters,on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Vehicles" 

#the commodities brought in by the different suppliers and vice versa
class Commodity(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status= models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Commodity"  

#employees and the title
class Employees(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Employees"

#different shifts in the institution
class Shifts(models.Model):
    name=models.CharField(max_length=50)
    clock_in=models.TimeField()
    clock_out=models.TimeField()
    status = models.CharField(max_length=10,blank=True)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Shifts"

#different  employees working as operators of the weighbridge
class Operators(models.Model):
    name=models.CharField(max_length=50)
    employee=models.ForeignKey(Employees,on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Operators"

#clocking in and out of the shifts
class ShiftsRecords(models.Model):
    name=models.CharField(max_length=50)
    operator=models.ForeignKey(Operators,on_delete=models.CASCADE)
    shift=models.ForeignKey(Shifts,on_delete=models.CASCADE)
    clock_in=models.DateTimeField()
    clock_out=models.DateTimeField()
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Shifts Performance"

#different weighing stages that the tractors go through

class AxleType(models.Model):
    name=models.CharField(max_length=50)
    axles=models.CharField(max_length=50)
    status =  models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Axle Type"

class WeighStages(models.Model):
    name=models.CharField(max_length=50)
    stages=models.CharField(max_length=50)
    status =  models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Weigh Stages"

#tickets that are generated for different weighing stages
class Tickets(models.Model):
    name=models.CharField(max_length=50)
    first_weight = models.CharField(max_length=50)
    second_weight = models.CharField(max_length=50,default=None)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    commodity=models.ForeignKey(Commodity,on_delete=models.CASCADE, null=True)
    supplier=models.ForeignKey(Suppliers,on_delete=models.CASCADE, null=True)
    weigh_stage=models.ForeignKey(WeighStages,on_delete=models.CASCADE, null=True)
    pub_date_first = models.DateTimeField()
    pub_date_second = models.DateTimeField()
    front_photo= models.FileField(upload_to='documents/tractors/tickets/front',default=None)
    side_photo= models.FileField(upload_to='documents/tractors/tickets/side',default=None)
    back_photo= models.FileField(upload_to='documents/tractors/tickets/back',default=None)
    plate_photo= models.FileField(upload_to='documents/tractors/tickets/plate',default=None)
    weighbridge =models.ForeignKey(Weighbridges,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    operator = models.ForeignKey(Operators,on_delete=models.CASCADE,null=True)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE,null=True)
    origin = models.ForeignKey(Origin,on_delete=models.CASCADE,null=True)
    operation = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Tickets"

#AxleGrouping

class Ticketsaxle(models.Model):
    name=models.CharField(max_length=50)
    groupa = models.CharField(max_length=50)
    groupb = models.CharField(max_length=50,default=None)
    groupc = models.CharField(max_length=50,default=None)
    groupd = models.CharField(max_length=50,default=None)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    commodity=models.ForeignKey(Commodity,on_delete=models.CASCADE, null=True)
    supplier=models.ForeignKey(Suppliers,on_delete=models.CASCADE, null=True)
    weigh_stage=models.ForeignKey(WeighStages,on_delete=models.CASCADE, null=True)
    axle_type=models.ForeignKey(AxleType,on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()
    front_photo= models.FileField(upload_to='documents/tractors/tickets/front',default=None)
    side_photo= models.FileField(upload_to='documents/tractors/tickets/side',default=None)
    back_photo= models.FileField(upload_to='documents/tractors/tickets/back',default=None)
    plate_photo= models.FileField(upload_to='documents/tractors/tickets/plate',default=None)
    weighbridge =models.ForeignKey(Weighbridges,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    operator = models.ForeignKey(Operators,on_delete=models.CASCADE,null=True)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE,null=True)
    origin = models.ForeignKey(Origin,on_delete=models.CASCADE,null=True)
    operation = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = " Tickets Axle Weighing"

#serial connections 
class ConnectionsSerial(models.Model):
    name=models.CharField(max_length=50)
    baud=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Serial Connections"

#ethernet connections
class ConnectionsEtho(models.Model):
    name=models.CharField(max_length=50)
    ip_address=models.CharField(max_length=50)
    port=models.CharField(max_length=50)
    mac_address=models.CharField(max_length=50,default=None)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Ethernet Connections"

class ExpiryDates(models.Model):
    name=models.CharField(max_length=50)
    licence=models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    reg_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Expiry Dates"



