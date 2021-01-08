from rest_framework import serializers 
from tutorials.models import *
from django.contrib.auth.models import User, Group 


############################# KILOSAHIHI #############################################

class CooperativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperatives
        fields = ('id','name','reg_date','status')

class UsersViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        depth=1

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        depth=1

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ('id','name','reg_date','status')

class FactoriesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factories
        fields = ('id','name','product','cooperative','reg_date','status')
        depth = 1

class FactoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factories
        fields = ('id','name','product','cooperative','reg_date','status')

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ('id','name','factory','reg_date','imei','status')

class DevicesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ('id','name','factory','reg_date','imei','status')
        depth = 1

class ClerkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerk
        fields = ('id','name','user','national_id','username','password','phone_number','factory','reg_date','status')
        depth = 1

class ClerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerk
        fields = ('id','name','user','national_id','username','password','phone_number','factory','reg_date','status')
      
class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = ('id','name','national_id','username','password','phone_number','bank_branch','bank_account_name', 'bank_account','acres','lat','lon','reg_date','factory','status')

class FarmersViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = ('id','name','national_id','username','password','phone_number','bank_branch','bank_account_name', 'bank_account','acres','lat','lon','reg_date','factory','status')
        depth = 1

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id','tx_code','clerk','weight','total_payout','farmer','device','produce','tx_date','status')

class TransactionsTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id','tx_code','total_payout','farmer','device','produce','tx_date','status')


     
class TransactionsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id','tx_code','clerk','weight','total_payout','farmer','device','produce','tx_date','status')
        depth = 1

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id','payment_code','tx_reference','method','payment_status','payment_date','status')

class PaymentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id','payment_code','tx_reference','method','payment_status','payment_date','status')
        depth = 1

class AuditsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audits
        fields = ('id','name','user','action','date','status')
        depth = 1
############################# KILOSAHIHI END #############################################


############################# BAT END #############################################

class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = ('id','name','desc','reg_date','status')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        sku = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Products
        fields = ('id','name','desc','reg_date','sku','status')

class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','name','desc','reg_date','sku','status')
        depth = 1

class ProductweightsSerializer(serializers.ModelSerializer):
    class Meta:
        product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = ProductWeights
        fields = ('id','name','product','date','weight','status')

class ProductweightsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWeights
        fields = ('id','name','product','date','weight','status')
        depth = 1

############################# BAT END #############################################


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id','name','desc','reg_date','status')

class WeighbridgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weighbridges
        fields = ('id','name','desc','lat','long','status')

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('id','name','desc','status','reg_date')

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ('id','name','desc','status','reg_date')
        depth = 1

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:

        account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Customers
        fields = ('id','name','account','email','contact','reg_date','status')

class CustomersViewSerializer(serializers.ModelSerializer):
    class Meta:

        account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Customers
        fields = ('id','name','account','email','contact','reg_date','status')
        depth=1  
  

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Suppliers
        fields = ('id','name','account','email','contact','reg_date','status')

class SuppliersViewSerializer(serializers.ModelSerializer):
    class Meta:
        account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Suppliers
        fields = ('id','name','account','email','contact','reg_date','status')
        depth=1

class TransportersSerializer(serializers.ModelSerializer):
    class Meta:
        supplier = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Transporters
        fields = ('id','name','email','supplier','contact','reg_date','status')

class TransportersViewSerializer(serializers.ModelSerializer):
    class Meta:
        supplier = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Transporters
        fields = ('id','name','email','supplier','contact','reg_date','status')   
        depth=1

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        transporter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Vehicle
        fields = ('id','name','no_plate','transporter','reg_date','status')

class VehicleViewSerializer(serializers.ModelSerializer):
    class Meta:
        transporter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Vehicle
        fields = ('id','name','no_plate','transporter','reg_date','status')
        depth=1

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Commodity
        fields = ('id','name','desc','reg_date','status')
     

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Employees
        fields = ('id','name','title','email','contact','reg_date','status')
    

class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = ('id','name','clock_in','clock_out','status')
       

class OperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Operators
        fields = ('id', 'name','employee','reg_date','status')

class OperatorsViewSerializer(serializers.ModelSerializer):
    class Meta:
        employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Operators
        fields = ('id', 'name','employee','reg_date','status') 
        depth=1    

class ShiftsrecordsSerializer(serializers.ModelSerializer):
    class Meta:
        operator = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        shift = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = ShiftsRecords
        fields = ('id','name','operator','shift','clock_in','clock_out','status')


class ShiftsrecordsViewSerializer(serializers.ModelSerializer):
    class Meta:
        operator = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        shift = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = ShiftsRecords
        fields = ('id','name','operator','shift','clock_in','clock_out','status')
        depth=1

class WeighstagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeighStages
        fields = ('id','name','status','stages')
        depth=1

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        vehicle = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        commodity = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        weigh_stage = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        weighbrdige = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        customer = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        operator = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        origin = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        destination = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Tickets
        fields = ('id','name','first_weight','second_weight','vehicle','commodity','weigh_stage','pub_date_first','pub_date_second','weighbridge','customer','operator','origin','destination','operation','status')
      

class TicketsViewSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Tickets
        fields = ('id','name','first_weight','second_weight','vehicle','commodity','weigh_stage','pub_date_first','pub_date_second','front_photo','side_photo','back_photo','plate_photo','weighbridge','customer','operator','origin','destination','operation','status')
        depth=1

class ConnectionsserialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionsSerial
        fields = ('id','name','baud','desc','status')

class ConnectionsethoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionsEtho
        fields = ('id','name','ip_address','port','mac_address','status')

class ExpiryDates(serializers.ModelSerializer):
    class Meta:
        model = ExpiryDates
        fields = ('id','name','baud','desc','status')

