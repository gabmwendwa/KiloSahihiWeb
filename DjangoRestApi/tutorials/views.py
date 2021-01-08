from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.db.models import Sum

from tutorials.models import *
from tutorials.serializers import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


 ################################### KILOSAHIHI  ################################### 

 ###################################              USERS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           users = users.filter(name__icontains=name)
        
        users_serializer = UsersViewSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersViewSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try: 
        users = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        users_serializer = UsersViewSerializer(users) 
        return JsonResponse(users_serializer.data) 
 
    elif request.method == 'PUT': 
        users_data = JSONParser().parse(request) 
        users_serializer = UsersViewSerializer(users, data=users_data)
        if users_serializer.is_valid(): 
            users_serializer.save() 
            return JsonResponse(users_serializer.data) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        users.delete() 
        return JsonResponse({'message': 'Users was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def users_list_active(request):
    users = User.objects.filter(status="Active")
        
    if request.method == 'GET': 
        users_serializer = UsersViewSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


 ###################################               USERS              ############################### 



 ###################################              COOPERATIVES              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def cooperatives_list(request):
    if request.method == 'GET':
        cooperatives = Cooperatives.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           cooperatives = cooperatives.filter(name__icontains=name)
        
        cooperatives_serializer = CooperativesSerializer(cooperatives, many=True)
        return JsonResponse(cooperatives_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        cooperatives_data = JSONParser().parse(request)
        cooperatives_serializer = CooperativesSerializer(data=cooperatives_data)
        if cooperatives_serializer.is_valid():
            cooperatives_serializer.save()
            return JsonResponse(cooperatives_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Cooperatives.objects.all().delete()
        return JsonResponse({'message': '{} Cooperatives were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def cooperatives_detail(request, pk):
    try: 
        cooperatives = Cooperatives.objects.get(pk=pk) 
    except Cooperatives.DoesNotExist: 
        return JsonResponse({'message': 'The cooperative does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        cooperatives_serializer = CooperativesSerializer(sku) 
        return JsonResponse(cooperatives_serializer.data) 
 
    elif request.method == 'PUT': 
        cooperatives_data = JSONParser().parse(request) 
        cooperatives_serializer = CooperativesSerializer(cooperatives, data=cooperatives_data)
        if cooperatives_serializer.is_valid(): 
            cooperatives_serializer.save() 
            return JsonResponse(cooperatives_serializer.data) 
        return JsonResponse(cooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        cooperatives.delete() 
        return JsonResponse({'message': 'Cooperative was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def cooperatives_list_active(request):
    sku = Cooperatives.objects.filter(status="Active")
        
    if request.method == 'GET': 
        cooperatives_serializer = CooperativesSerializer(sku, many=True)
        return JsonResponse(cooperatives_serializer.data, safe=False)


 ###################################               COOPERATIVES               ###############################



  ###################################              AUDITS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def audits_list(request):
    if request.method == 'GET':
        audits = Audits.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           audits = audits.filter(name__icontains=name)
        
        audits_serializer = AuditsViewSerializer(audits, many=True)
        return JsonResponse(audits_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        audits_data = JSONParser().parse(request)
        audits_serializer = AuditsViewSerializer(data=audits_data)
        if audits_serializer.is_valid():
            audits_serializer.save()
            return JsonResponse(audits_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(audits_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Audits.objects.all().delete()
        return JsonResponse({'message': '{} Audits were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def audits_detail(request, pk):
    try: 
        audits = Audits.objects.get(pk=pk) 
    except Audits.DoesNotExist: 
        return JsonResponse({'message': 'The audits does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        audits_serializer = AuditsViewSerializer(audits) 
        return JsonResponse(audits_serializer.data) 
 
    elif request.method == 'PUT': 
        audits_data = JSONParser().parse(request) 
        audits_serializer = AuditsViewSerializer(audits, data=audits_data)
        if audits_serializer.is_valid(): 
            audits_serializer.save() 
            return JsonResponse(audits_serializer.data) 
        return JsonResponse(audits_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        audits.delete() 
        return JsonResponse({'message': 'Audits was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def audits_list_active(request):
    sku = Audits.objects.filter(status="Active")
        
    if request.method == 'GET': 
        audits_serializer = AuditsViewSerializer(audits, many=True)
        return JsonResponse(audits_serializer.data, safe=False)


 ###################################               AUDITS              ############################### 


###################################              PRODUCE              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def produce_list(request):
    if request.method == 'GET':
        produce = Produce.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           produce = produce.filter(name__icontains=name)
        
        produce_serializer = ProduceSerializer(produce, many=True)
        return JsonResponse(produce_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        produce_data = JSONParser().parse(request)
        produce_serializer = ProduceSerializer(data=produce_data)
        if produce_serializer.is_valid():
            produce_serializer.save()
            return JsonResponse(produce_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(produce_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Produce.objects.all().delete()
        return JsonResponse({'message': '{} Produce were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def produce_detail(request, pk):
    try: 
        produce = Produce.objects.get(pk=pk) 
    except Produce.DoesNotExist: 
        return JsonResponse({'message': 'The produce does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        produce_serializer = ProduceSerializer(produce) 
        return JsonResponse(produce_serializer.data) 
 
    elif request.method == 'PUT': 
        produce_data = JSONParser().parse(request) 
        produce_serializer = ProduceSerializer(produce, data=produce_data)
        if produce_serializer.is_valid(): 
            produce_serializer.save() 
            return JsonResponse(produce_serializer.data) 
        return JsonResponse(produce_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        produce.delete() 
        return JsonResponse({'message': 'Produce was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def produce_list_active(request):
    sku = Produce.objects.filter(status="Active")
        
    if request.method == 'GET': 
        produce_serializer = ProduceSerializer(sku, many=True)
        return JsonResponse(produce_serializer.data, safe=False)


 ###################################               PRODUCE END               ############################### 

###################################               FACTORIES            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def factories_list(request):
    if request.method == 'GET':
        factories = Factories.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            factories = factories.filter(name__icontains=name)
        
        factories_serializer = FactoriesViewSerializer(factories, many=True)
        return JsonResponse(factories_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        factories_data = JSONParser().parse(request)
        factories_serializer = FactoriesSerializer(data=factories_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            return JsonResponse(factories_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(factories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Factories.objects.all().delete()
        return JsonResponse({'message': '{} Factories were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def factories_detail(request, pk):
    try: 
        factories = Factories.objects.get(pk=pk) 
    except Factories.DoesNotExist: 
        return JsonResponse({'message': 'The factory does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        factories_serializer = FactoriesSerializer(factories) 
        return JsonResponse(factories_serializer.data) 
 
    elif request.method == 'PUT': 
        factories_data = JSONParser().parse(request) 
        factories_serializer = FactoriesSerializer(factories, data=factories_data) 
        if factories_serializer.is_valid(): 
            factories_serializer.save() 
            return JsonResponse(factories_serializer.data) 
        return JsonResponse(factories_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        factories.delete() 
        return JsonResponse({'message': 'Factory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def factories_list_active(request):
    factories = Factories.objects.filter(published=True)
        
    if request.method == 'GET': 
        factories_serializer = FactoriesSerializer(factories, many=True)
        return JsonResponse(factories_serializer.data, safe=False)


###################################               DEVICES            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def devices_list(request):
    if request.method == 'GET':
        devices = Devices.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            devices = devices.filter(name__icontains=name)
        
        devices_serializer = DevicesViewSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        devices_data = JSONParser().parse(request)
        devices_serializer = DevicesSerializer(data=devices_data)
        if devices_serializer.is_valid():
            devices_serializer.save()
            return JsonResponse(devices_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(devices_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Devices.objects.all().delete()
        return JsonResponse({'message': '{} Devices were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def devices_detail(request, pk):
    try: 
        devices = Devices.objects.get(pk=pk) 
    except Devices.DoesNotExist: 
        return JsonResponse({'message': 'The device does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        devices_serializer = DevicesSerializer(devices) 
        return JsonResponse(devices_serializer.data) 
 
    elif request.method == 'PUT': 
        devices_data = JSONParser().parse(request) 
        devices_serializer = DevicesSerializer(devices, data=devices_data) 
        if devices_serializer.is_valid(): 
            devices_serializer.save() 
            return JsonResponse(devices_serializer.data) 
        return JsonResponse(devices_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        devices.delete() 
        return JsonResponse({'message': 'The device was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def devices_list_active(request):
    devices = Devices.objects.filter(published=True)
        
    if request.method == 'GET': 
        devices_serializer = DevicesSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)


###################################               CLERK            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def clerk_list(request):
    if request.method == 'GET':
        clerk = Clerk.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            clerk = clerk.filter(name__icontains=name)
        
        clerk_serializer = ClerkViewSerializer(clerk, many=True)
        return JsonResponse(clerk_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        clerk_data = JSONParser().parse(request)
        clerk_serializer = ClerkSerializer(data=clerk_data)
        if clerk_serializer.is_valid():
            clerk_serializer.save()
            return JsonResponse(clerk_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(clerk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Clerk.objects.all().delete()
        return JsonResponse({'message': '{} Clerks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def clerk_detail(request, pk):
    try: 
        clerk = Clerk.objects.get(pk=pk) 
    except Clerk.DoesNotExist: 
        return JsonResponse({'message': 'The clerk does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        clerk_serializer = ClerkSerializer(clerk) 
        return JsonResponse(clerk_serializer.data) 
 
    elif request.method == 'PUT': 
        clerk_data = JSONParser().parse(request) 
        clerk_serializer = ClerkSerializer(clerk, data=clerk_data) 
        if clerk_serializer.is_valid(): 
            clerk_serializer.save() 
            return JsonResponse(clerk_serializer.data) 
        return JsonResponse(clerk_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        clerk.delete() 
        return JsonResponse({'message': 'The clerk was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def clerk_list_active(request):
    clerk = Clerk.objects.filter(published=True)
        
    if request.method == 'GET': 
        clerk_serializer = ClerkSerializer(clerk, many=True)
        return JsonResponse(clerk_serializer.data, safe=False)


###################################               FARMERS            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farmers_list(request):
    if request.method == 'GET':
        farmers = Farmers.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farmers = farmers.filter(name__icontains=name)
        
        farmers_serializer = FarmersViewSerializer(farmers, many=True)
        return JsonResponse(farmers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farmers_data = JSONParser().parse(request)
        farmers_serializer = FarmersSerializer(data=farmers_data)
        if farmers_serializer.is_valid():
            farmers_serializer.save()
            return JsonResponse(farmers_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Farmers.objects.all().delete()
        return JsonResponse({'message': '{} Farmers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farmers_detail(request, pk):
    try: 
        farmers = Farmers.objects.get(pk=pk) 
    except Farmers.DoesNotExist: 
        return JsonResponse({'message': 'The farmer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farmers_serializer = FarmersSerializer(farmers) 
        return JsonResponse(farmers_serializer.data) 
 
    elif request.method == 'PUT': 
        farmers_data = JSONParser().parse(request) 
        farmers_serializer = FarmersSerializer(farmers, data=farmers_data) 
        if farmers_serializer.is_valid(): 
            farmers_serializer.save() 
            return JsonResponse(farmers_serializer.data) 
        return JsonResponse(farmers_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farmers.delete() 
        return JsonResponse({'message': 'The farmer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farmers_list_active(request):
    farmers = Farmers.objects.filter(published=True)
        
    if request.method == 'GET': 
        farmers_serializer = FarmersSerializer(farmers, many=True)
        return JsonResponse(farmers_serializer.data, safe=False)


###################################               TRANSACTIONS            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def transactions_list(request):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            transactions = transactions.filter(name__icontains=name)
        
        transactions_serializer = TransactionsViewSerializer(transactions, many=True)
        return JsonResponse(transactions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        transactions_data = JSONParser().parse(request)
        transactions_serializer = TransactionsSerializer(data=transactions_data)
        if transactions_serializer.is_valid():
            transactions_serializer.save()
            return JsonResponse(transactions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Transactions.objects.all().delete()
        return JsonResponse({'message': '{} Transactions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def transactions_detail(request, pk):
    try: 
        transactions = Transactions.objects.get(pk=pk) 
    except Transactions.DoesNotExist: 
        return JsonResponse({'message': 'The transaction does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        transactions_serializer = TransactionsViewSerializer(transactions) 
        return JsonResponse(transactions_serializer.data) 
 
    elif request.method == 'PUT': 
        transactions_data = JSONParser().parse(request) 
        transactions_serializer = TransactionsSerializer(transactions, data=transactions_data) 
        if transactions_serializer.is_valid(): 
            transactions_serializer.save() 
            return JsonResponse(transactions_serializer.data) 
        return JsonResponse(transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        transactions.delete() 
        return JsonResponse({'message': 'The transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def transactions_list_active(request):
    transactions = Transactions.objects.filter(published=True)
        
    if request.method == 'GET': 
        transactions_serializer = TransactionsSerializer(transactions, many=True)
        return JsonResponse(transactions_serializer.data, safe=False)


@api_view(['GET'])
def transactions_total(request,pk):
    cumulative_weight = Transactions.objects.filter(farmer=pk).aggregate(Sum('weight'))['weight__sum']
        
    if request.method == 'GET': 
        #transactions_serializer = TransactionsTotalSerializer(transactions, many=True)
        #return JsonResponse(transactions_serializer.data, safe=False)
        return JsonResponse({'cumulative_weight': cumulative_weight if cumulative_weight else 0,'farmer':pk})
        


###################################               PAYMENT            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def payment_list(request):
    if request.method == 'GET':
        payment = Payment.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            payment = payment.filter(name__icontains=name)
        
        payment_serializer = PaymentViewSerializer(transactions, many=True)
        return JsonResponse(payment_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Payment.objects.all().delete()
        return JsonResponse({'message': '{} Payments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    try: 
        payment = Payment.objects.get(pk=pk) 
    except Payment.DoesNotExist: 
        return JsonResponse({'message': 'The payment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment) 
        return JsonResponse(payment_serializer.data) 
 
    elif request.method == 'PUT': 
        payment_data = JSONParser().parse(request) 
        payment_serializer = PaymentSerializer(payment, data=payment_data) 
        if payment_serializer.is_valid(): 
            payment_serializer.save() 
            return JsonResponse(payment_serializer.data) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        payment.delete() 
        return JsonResponse({'message': 'The payment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def payment_list_active(request):
    payment = Payment.objects.filter(published=True)
        
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

###################################             SINGLE PRODUCT WEIGHING               ############################### 


 ###################################               SKU                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def sku_list(request):
    if request.method == 'GET':
        sku = Sku.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           sku = sku.filter(name__icontains=name)
        
        sku_serializer = SkuSerializer(sku, many=True)
        return JsonResponse(sku_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        sku_data = JSONParser().parse(request)
        sku_serializer = SkuSerializer(data=sku_data)
        if sku_serializer.is_valid():
            sku_serializer.save()
            return JsonResponse(sku_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(sku_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Sku.objects.all().delete()
        return JsonResponse({'message': '{} Skus were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def sku_detail(request, pk):
    try: 
        sku = Sku.objects.get(pk=pk) 
    except Sku.DoesNotExist: 
        return JsonResponse({'message': 'The sku does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        sku_serializer = SkuSerializer(sku) 
        return JsonResponse(sku_serializer.data) 
 
    elif request.method == 'PUT': 
        sku_data = JSONParser().parse(request) 
        sku_serializer = SkuSerializer(sku, data=sku_data)
        if sku_serializer.is_valid(): 
            sku_serializer.save() 
            return JsonResponse(sku_serializer.data) 
        return JsonResponse(sku_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        sku.delete() 
        return JsonResponse({'message': 'SKU was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def sku_list_active(request):
    sku = Sku.objects.filter(status="Active")
        
    if request.method == 'GET': 
        sku_serializer = SkuSerializer(sku, many=True)
        return JsonResponse(sku_serializer.data, safe=False)


 ###################################               PRODUCTS               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           products = products.filter(name__icontains=name)
        
        products_serializer = ProductsViewSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Products.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    try: 
        products = Products.objects.get(pk=pk) 
    except Products.DoesNotExist: 
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        products_serializer = ProductsViewSerializer(products) 
        return JsonResponse(products_serializer.data) 
 
    elif request.method == 'PUT': 
        products_data = JSONParser().parse(request) 
        products_serializer = ProductsSerializer(products, data=products_data)
        if products_serializer.is_valid(): 
            products_serializer.save() 
            return JsonResponse(products_serializer.data) 
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        products.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def products_list_active(request):
    products = Products.objects.filter(status="Active")
        
    if request.method == 'GET': 
        products_serializer = ProductsViewSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)


 ###################################               PRODUCT WEIGHTS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def productweights_list(request):
    if request.method == 'GET':
        productweights =  ProductWeights.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            productweights =  productweights.filter(name__icontains=name)
        
        productweights_serializer =  ProductweightsViewSerializer(productweights, many=True)
        return JsonResponse( productweights_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        productweights_data = JSONParser().parse(request)
        productweights_serializer = ProductweightsSerializer(data= productweights_data)
        if  productweights_serializer.is_valid():
            productweights_serializer.save()
            return JsonResponse(productweights_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse( productweights_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = ProductWeights.objects.all().delete()
        return JsonResponse({'message': '{} Tickets were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def  productweights_detail(request, pk):
    try: 
        productweights = ProductWeights.objects.get(pk=pk) 
    except ProductWeights.DoesNotExist: 
        return JsonResponse({'message': 'The Ticket does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        productweights_serializer = ProductweightsViewSerializer(productweights) 
        return JsonResponse(productweights_serializer.data) 
 
    elif request.method == 'PUT': 
        productweights_data = JSONParser().parse(request) 
        productweights_serializer = ProductweightsSerializer(productweights, data= productweights_data)
        if productweights_serializer.is_valid(): 
            productweights_serializer.save() 
            return JsonResponse(productweights_serializer.data) 
        return JsonResponse(productweights_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        productweights.delete() 
        return JsonResponse({'message': 'Ticket was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])
def productweights_list_active(request):
    productweights = ProductWeights.objects.filter(status="Active")
        
    if request.method == 'GET': 
        productweights_serializer = ProductweightsSerializer(productweights, many=True)
        return JsonResponse(productweights_serializer.data, safe=False)

    
 ###################################               ACCOUNTS               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def accounts_list(request):
    if request.method == 'GET':
        accounts = Accounts.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            accounts = accounts.filter(name__icontains=name) 
        accounts_serializer =AccountsSerializer(accounts, many=True)
        return JsonResponse(accounts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        accounts_data = JSONParser().parse(request)
        accounts_serializer = AccountsSerializer(data=accounts_data)
        if accounts_serializer.is_valid():
            accounts_serializer.save()
            return JsonResponse(accounts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Accounts.objects.all().delete()
        return JsonResponse({'message': '{} Accounts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def accounts_detail(request, pk):
    try: 
        accounts = Accounts.objects.get(pk=pk) 
    except Accounts.DoesNotExist: 
        return JsonResponse({'message': 'The Account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        accounts_serializer = AccountsSerializer(accounts) 
        return JsonResponse(accounts_serializer.data) 
 
    elif request.method == 'PUT': 
        accounts_data = JSONParser().parse(request) 
        accounts_serializer = AccountsSerializer(accounts, data=accounts_data) 
        if accounts_serializer.is_valid(): 
            accounts_serializer.save() 
            return JsonResponse(accounts_serializer.data) 
        return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        accounts.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def accounts_list_active(request):
    accounts = Accounts.objects.filter(Status="Active")
        
    if request.method == 'GET': 
        accounts_serializer = AccountsSerializer(accounts, many=True)
        return JsonResponse(accounts_serializer.data, safe=False)

 ###################################               TITLE                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def destination_list(request):
    if request.method == 'GET':
        destination = Destination.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            destination = destination.filter(name__icontains=name)
        
        destination_serializer = DestinationSerializer(destination, many=True)
        return JsonResponse(destination_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        destination_data = JSONParser().parse(request)
        destination_serializer = DestinationSerializer(data=destination_data)
        if destination_serializer.is_valid():
            destination_serializer.save()
            return JsonResponse(destination_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(destination_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Destination.objects.all().delete()
        return JsonResponse({'message': '{} Destination Records were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def destination_detail(request, pk):
    try: 
        destination = Destination.objects.get(pk=pk) 
    except Destination.DoesNotExist: 
        return JsonResponse({'message': 'The destination records does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        destination_serializer = DestinationSerializer(destination) 
        return JsonResponse(destination_serializer.data) 
 
    elif request.method == 'PUT': 
        destination_data = JSONParser().parse(request) 
        destination_serializer = DestinationSerializer(destination, data=destination_data) 
        if destination_serializer.is_valid(): 
            destination_serializer.save() 
            return JsonResponse(destination_serializer.data) 
        return JsonResponse(destination_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        destination.delete() 
        return JsonResponse({'message': 'Destination record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def destination_list_active(request):
    destination = Destination.objects.filter(status="Active")
        
    if request.method == 'GET': 
        destination_serializer = DestinationSerializer(destination, many=True)
        return JsonResponse(destination_serializer.data, safe=False)

 ###################################               Origin                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def origin_list(request):
    if request.method == 'GET':
        origin = Origin.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            origin = origin.filter(name__icontains=name)
        
        origin_serializer = OriginSerializer(origin, many=True)
        return JsonResponse(origin_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        origin_data = JSONParser().parse(request)
        origin_serializer = OriginSerializer(data=origin_data)
        if origin_serializer.is_valid():
            origin_serializer.save()
            return JsonResponse(origin_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(origin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Origin.objects.all().delete()
        return JsonResponse({'message': '{} Origin records were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def origin_detail(request, pk):
    try: 
        origin = Origin.objects.get(pk=pk) 
    except Origin.DoesNotExist: 
        return JsonResponse({'message': 'The Origin record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        origin_serializer = OriginSerializer(origin) 
        return JsonResponse(origin_serializer.data) 
 
    elif request.method == 'PUT': 
        origin_data = JSONParser().parse(request) 
        origin_serializer = OriginSerializer(origin, data=origin_data) 
        if origin_serializer.is_valid(): 
            origin_serializer.save() 
            return JsonResponse(origin_serializer.data) 
        return JsonResponse(origin_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        origin.delete() 
        return JsonResponse({'message': 'Origin Record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def origin_list_active(request):
    origin = Origin.objects.filter(status="Active")
        
    if request.method == 'GET': 
        origin_serializer = OriginSerializer(origin, many=True)
        return JsonResponse(origin_serializer.data, safe=False)

 ###################################               SUPPLIERS            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def suppliers_list(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            suppliers = suppliers.filter(name__icontains=name)
        
        suppliers_serializer = SuppliersViewSerializer(suppliers, many=True)
        return JsonResponse(suppliers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        suppliers_data = JSONParser().parse(request)
        suppliers_serializer = SuppliersSerializer(data=suppliers_data)
        if suppliers_serializer.is_valid():
            suppliers_serializer.save()
            return JsonResponse(suppliers_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(suppliers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Suppliers.objects.all().delete()
        return JsonResponse({'message': '{} Suppliers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def suppliers_detail(request, pk):
    try: 
        suppliers = Suppliers.objects.get(pk=pk) 
    except Suppliers.DoesNotExist: 
        return JsonResponse({'message': 'The supplier does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        suppliers_serializer = SuppliersSerializer(suppliers) 
        return JsonResponse(suppliers_serializer.data) 
 
    elif request.method == 'PUT': 
        suppliers_data = JSONParser().parse(request) 
        suppliers_serializer = SuppliersSerializer(suppliers, data=suppliers_data) 
        if suppliers_serializer.is_valid(): 
            suppliers_serializer.save() 
            return JsonResponse(suppliers_serializer.data) 
        return JsonResponse(suppliers_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        suppliers.delete() 
        return JsonResponse({'message': 'Supplier was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def suppliers_list_active(request):
    suppliers = Suppliers.objects.filter(published=True)
        
    if request.method == 'GET': 
        suppliers_serializer = SuppliersSerializer(suppliers, many=True)
        return JsonResponse(suppliers_serializer.data, safe=False)

 ###################################               WEIGHBRIDGES                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def weighbridges_list(request):
    if request.method == 'GET':
        weighbridges = Weighbridges.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            weighbridges = weighbridges.filter(name__icontains=name)
        
        weighbridges_serializer = WeighbridgesSerializer(weighbridges, many=True)
        return JsonResponse(weighbridges_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        weighbridges_data = JSONParser().parse(request)
        weighbridges_serializer = WeighbridgesSerializer(data=weighbridges_data)
        if weighbridges_serializer.is_valid():
            weighbridges_serializer.save()
            return JsonResponse(weighbridges_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(weighbridges_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Weighbridges.objects.all().delete()
        return JsonResponse({'message': '{} Weighbridges were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def weighbridges_detail(request, pk):
    try: 
        weighbridges = Weighbridges.objects.get(pk=pk) 
    except Weighbridges.DoesNotExist: 
        return JsonResponse({'message': 'The weighbridge does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        weighbridges_serializer = WeighbridgesSerializer(weighbridges) 
        return JsonResponse(weighbridges_serializer.data) 
 
    elif request.method == 'PUT': 
        weighbridges_data = JSONParser().parse(request) 
        weighbridges_serializer = WeighbridgesSerializer(weighbridges, data=weighbridges_data) 
        if weighbridges_serializer.is_valid(): 
            weighbridges_serializer.save() 
            return JsonResponse(weighbridges_serializer.data) 
        return JsonResponse(weighbridges_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        weighbridges.delete() 
        return JsonResponse({'message': 'Weighbridge was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def weighbridges_list_active(request):
    weighbridges = Weighbridges.objects.filter(published=True)
        
    if request.method == 'GET': 
        weighbridges_serializer = WeighbridgesSerializer(Weighbridges, many=True)
        return JsonResponse(weighbridges_serializer.data, safe=False)

 ###################################               CUSTOMERS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def customers_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            customers = customers.filter(name__icontains=name)
        
        customers_serializer = CustomersViewSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        customers_data = JSONParser().parse(request)
        customers_serializer = CustomersSerializer(data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse(customers_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Customers.objects.all().delete()
        return JsonResponse({'message': '{} Customers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    try: 
        customers = Customers.objects.get(pk=pk) 
    except Customers.DoesNotExist: 
        return JsonResponse({'message': 'The Customers do not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customers_serializer = CustomersSerializer(customers) 
        return JsonResponse(customers_serializer.data) 
 
    elif request.method == 'PUT': 
        customers_data = JSONParser().parse(request) 
        customers_serializer = CustomersSerializer(customers, data=customers_data) 
        if customers_serializer.is_valid(): 
            customers_serializer.save() 
            return JsonResponse(customers_serializer.data) 
        return JsonResponse(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customers.delete() 
        return JsonResponse({'message': 'Customers was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def customers_list_active(request):
    customers = Customers.objects.filter(status="Active")
        
    if request.method == 'GET': 
        customers_serializer = CustomersSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)

 ###################################               TRANSPORTERS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def transporters_list(request):
    if request.method == 'GET':
        transporters = Transporters.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            transporters = transporters.filter(name__icontains=name)
        
        transporters_serializer = TransportersViewSerializer(transporters, many=True)
        return JsonResponse(transporters_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        transporters_data = JSONParser().parse(request)
        transporters_serializer = TransportersSerializer(data=transporters_data)
        if transporters_serializer.is_valid():
            transporters_serializer.save()
            return JsonResponse(transporters_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(transporters_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Transporters.objects.all().delete()
        return JsonResponse({'message': '{} Transporters were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def transporters_detail(request, pk):
    try: 
        transporters = Transporters.objects.get(pk=pk) 
    except transporters.DoesNotExist: 
        return JsonResponse({'message': 'The Transporter does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        transporters_serializer = TransportersSerializer(transporters) 
        return JsonResponse(transporters_serializer.data) 
 
    elif request.method == 'PUT': 
        transporters_data = JSONParser().parse(request) 
        transporters_serializer = TransportersSerializer(transporters, data=transporters_data) 
        if transporters_serializer.is_valid(): 
            transporters_serializer.save() 
            return JsonResponse(transporters_serializer.data) 
        return JsonResponse(transporters_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        transporters.delete() 
        return JsonResponse({'message': 'Transporter was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def transporters_list_active(request):
    transporters = Transporters.objects.filter(Status="Active")
        
    if request.method == 'GET': 
       transporters_serializer = TransportersSerializer(transporters, many=True)
       return JsonResponse(transporters_serializer.data, safe=False)

 ###################################              VEHICLE               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def vehicle_list(request):
    if request.method == 'GET':
        vehicle = Vehicle.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            vehicle = vehicle.filter(name__icontains=name)
        
        vehicle_serializer = VehicleViewSerializer(vehicle, many=True)
        return JsonResponse(vehicle_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        vehicle_data = JSONParser().parse(request)
        vehicle_serializer = VehicleSerializer(data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse(vehicle_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Vehicle.objects.all().delete()
        return JsonResponse({'message': '{} Vehicles were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_detail(request, pk):
    try: 
        vehicle = Vehicle.objects.get(pk=pk) 
    except Vehicle.DoesNotExist: 
        return JsonResponse({'message': 'The vehicle does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        vehicle_serializer = VehicleSerializer(vehicle) 
        return JsonResponse(vehicle_serializer.data) 
 
    elif request.method == 'PUT': 
        vehicle_data = JSONParser().parse(request) 
        vehicle_serializer = VehicleSerializer(vehicle, data=vehicle_data) 
        if vehicle_serializer.is_valid(): 
            vehicle_serializer.save() 
            return JsonResponse(vehicle_serializer.data) 
        return JsonResponse(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        vehicle.delete() 
        return JsonResponse({'message': 'Vehicle was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def vehicle_list_active(request):
    vehicle = Vehicle.objects.filter(status="Active")
        
    if request.method == 'GET': 
        vehicle_serializer = VehicleSerializer(vehicle, many=True)
        return JsonResponse(vehicle_serializer.data, safe=False)

 ###################################               COMMODITY                ############################### 


@api_view(['GET', 'POST', 'DELETE'])
def commodity_list(request):
    if request.method == 'GET':
        commodity = Commodity.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            commodity = commodity.filter(name__icontains=name)
        
        commodity_serializer = CommoditySerializer(commodity, many=True)
        return JsonResponse(commodity_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        commodity_data = JSONParser().parse(request)
        commodity_serializer = CommoditySerializer(data=commodity_data)
        if commodity_serializer.is_valid():
            commodity_serializer.save()
            return JsonResponse(commodity_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(commodity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Commodity.objects.all().delete()
        return JsonResponse({'message': '{} Commodity were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def commodity_detail(request, pk):
    try: 
        commodity = Commodity.objects.get(pk=pk) 
    except Commodity.DoesNotExist: 
        return JsonResponse({'message': 'The commodity does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        commodity_serializer = CommoditySerializer(commodity) 
        return JsonResponse(commodity_serializer.data) 
 
    elif request.method == 'PUT': 
        commodity_data = JSONParser().parse(request) 
        commodity_serializer = CommoditySerializer(commodity, data=commodity_data) 
        if commodity_serializer.is_valid(): 
            commodity_serializer.save() 
            return JsonResponse(commodity_serializer.data) 
        return JsonResponse(commodity_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        commodity.delete() 
        return JsonResponse({'message': 'Commodity was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def commodity_list_active(request):
    commodity = Commodity.objects.filter(status="Active")
        
    if request.method == 'GET': 
        commodity_serializer = CommoditySerializer(commodity, many=True)
        return JsonResponse(commodity_serializer.data, safe=False)

 ###################################              EMPLOYEES               ############################### 
  
@api_view(['GET', 'POST', 'DELETE'])
def employees_list(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            employees = employees.filter(name__icontains=name)
        
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse(employees_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Employees.objects.all().delete()
        return JsonResponse({'message': '{} Employees were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def employees_detail(request, pk):
    try: 
        employees = Employees.objects.get(pk=pk) 
    except Employees.DoesNotExist: 
        return JsonResponse({'message': 'The employees data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        employees_serializer = EmployeesSerializer(employees) 
        return JsonResponse(employees_serializer.data) 
 
    elif request.method == 'PUT': 
        employees_data = JSONParser().parse(request) 
        employees_serializer = EmployeesSerializer(employees, data=employees_data) 
        if employees_serializer.is_valid(): 
            employees_serializer.save() 
            return JsonResponse(employees_serializer.data) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        employees.delete() 
        return JsonResponse({'message': 'Employee  was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def employees_list_active(request):
    employees = Employees.objects.filter(status="Active")
        
    if request.method == 'GET': 
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

 ###################################               SHIFTS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def shifts_list(request):
    if request.method == 'GET':
        shifts = Shifts.objects.all() 
        title = request.query_params.get('name', None)
        if title is not None:
            shifts = shifts.filter(title__icontains=title)
        
        shifts_serializer = ShiftsSerializer(shifts, many=True)
        return JsonResponse(shifts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        shifts_data = JSONParser().parse(request)
        shifts_serializer = ShiftsSerializer(data=tutorial_data)
        if shifts_serializer.is_valid():
            shifts_serializer.save()
            return JsonResponse(shifts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(shifts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Shifts.objects.all().delete()
        return JsonResponse({'message': '{} Shifts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def shifts_detail(request, pk):
    try: 
        shifts = Shifts.objects.get(pk=pk) 
    except Shifts.DoesNotExist: 
        return JsonResponse({'message': 'The shift does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        shifts_serializer = ShiftsSerializer(shifts) 
        return JsonResponse(shifts_serializer.data) 
 
    elif request.method == 'PUT': 
        shifts_data = JSONParser().parse(request) 
        shifts_serializer = ShiftsSerializer(shifts, data=shifts_data) 
        if shifts_serializer.is_valid(): 
            shifts_serializer.save() 
            return JsonResponse(shifts_serializer.data) 
        return JsonResponse(shifts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        shifts.delete() 
        return JsonResponse({'message': 'Shift was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def shifts_list_active(request):
    shifts = Shifts.objects.filter(status='Active')
        
    if request.method == 'GET': 
        shifts_serializer = ShiftsSerializer(shifts, many=True)
        return JsonResponse(shifts_serializer.data, safe=False)

 ###################################               OPERATORS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def operators_list(request):
    if request.method == 'GET':
        operators = Operators.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            operators = operators.filter(name__icontains=name)
        
        operators_serializer = OperatorsViewSerializer(operators, many=True)
        return JsonResponse(operators_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        operators_data = JSONParser().parse(request)
        operators_serializer = OperatorsSerializer(data=operators_data)
        if operators_serializer.is_valid():
            operators_serializer.save()
            return JsonResponse(operators_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(operators_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Operators.objects.all().delete()
        return JsonResponse({'message': '{} Operators were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def operators_detail(request, pk):
    try: 
        operators = Operators.objects.get(pk=pk) 
    except Operators.DoesNotExist: 
        return JsonResponse({'message': 'The operators does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if operators.method == 'GET': 
        operators_serializer = OperatorslSerializer(operators) 
        return JsonResponse(operators_serializer.data) 
 
    elif request.method == 'PUT': 
        operators_data = JSONParser().parse(request) 
        operators_serializer = OperatorsSerializer(operators, data=operators_data) 
        if operators_serializer.is_valid(): 
            operators_serializer.save() 
            return JsonResponse(operators_serializer.data) 
        return JsonResponse(operators_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        operators.delete() 
        return JsonResponse({'message': 'Operator was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def operators_list_active(request):
    operators = Operators.objects.filter(status="Active")
        
    if request.method == 'GET': 
        operators_serializer = OperatorsSerializer(operators, many=True)
        return JsonResponse(operators_serializer.data, safe=False)

 ###################################             SHIFTS RECORDS            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def shiftsrecords_list(request):
    if request.method == 'GET':
        shiftsrecords = Shiftsrecords.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            shiftsrecords = shiftsrecords.filter(name__icontains=name)
        
        shiftsrecords_serializer = shiftsrecordsViewSerializer(shiftsrecords, many=True)
        return JsonResponse(shiftsrecords_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        shiftsrecords_data = JSONParser().parse(request)
        shiftsrecords_serializer = ShiftsrecordsSerializer(data=shiftsrecords_data)
        if shiftsrecords_serializer.is_valid():
            shiftsrecords_serializer.save()
            return JsonResponse(shiftsrecords_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(shiftsrecords_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Shiftsrecords.objects.all().delete()
        return JsonResponse({'message': '{} Shiftsrecords were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def shiftsrecords_detail(request, pk):
    try: 
        shiftsrecords = ShiftsRecords.objects.get(pk=pk) 
    except ShiftsRecords.DoesNotExist: 
        return JsonResponse({'message': 'The shiftsrecord does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        shiftsrecords_serializer = ShiftsrecordsSerializer(shiftsrecords) 
        return JsonResponse(shiftsrecords_serializer.data) 
 
    elif request.method == 'PUT': 
        shiftsrecords_data = JSONParser().parse(request) 
        shiftsrecords_serializer = ShiftsrecordsSerializer(shiftsrecords, data=shiftsrecords_data) 
        if shiftsrecords_serializer.is_valid(): 
            shiftsrecords_serializer.save() 
            return JsonResponse(shiftsrecords_serializer.data) 
        return JsonResponse(shiftsrecords_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        shiftsrecords.delete() 
        return JsonResponse({'message': 'Shifts record  was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def shiftsrecords_list_active(request):
    shiftsrecords = ShiftsRecords.objects.filter(published=True)
        
    if request.method == 'GET': 
        shiftsrecords_serializer = ShiftsrecordsSerializer(shiftsrecords, many=True)
        return JsonResponse(shiftsrecords_serializer.data, safe=False)

 ###################################               WEIGHSTAGES               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def weighstages_list(request):
    if request.method == 'GET':
        weighstages = WeighStages.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            weighstages = weighstages.filter(name__icontains=name)
        
        weighstages_serializer = WeighstagesSerializer(weighstages, many=True)
        return JsonResponse(weighstages_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        weighstages_data = JSONParser().parse(request)
        weighstages_serializer = WeighstagesSerializer(data=weighstages_data)
        if weighstages_serializer.is_valid():
            weighstages_serializer.save()
            return JsonResponse(weighstages_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(weighstages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Weighstages.objects.all().delete()
        return JsonResponse({'message': '{} Weighstages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def weighstages_detail(request, pk):
    try: 
        weighstages = Weighstages.objects.get(pk=pk) 
    except Weighstages.DoesNotExist: 
        return JsonResponse({'message': 'The Weighstage does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        weighstages_serializer = WeighstagesSerializer(weighstages) 
        return JsonResponse(weighstages_serializer.data) 
 
    elif request.method == 'PUT': 
        weighstages_data = JSONParser().parse(request) 
        weighstages_serializer = WeighstagesSerializer(weighstages, data=weighstages_data) 
        if weighstages_serializer.is_valid(): 
            weighstages_serializer.save() 
            return JsonResponse(weighstages_serializer.data) 
        return JsonResponse(weighstages_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        weighstages.delete() 
        return JsonResponse({'message': 'Weighstage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def weighstages_list_active(request):
    weighstages = Weighstages.objects.filter(status="Active")
        
    if request.method == 'GET': 
        weighstages_serializer = WeighstagesSerializer(weighstages, many=True)
        return JsonResponse(weighstages_serializer.data, safe=False)

 ###################################               TICKETS                ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def tickets_list(request):
    if request.method == 'GET':
        tickets = Tickets.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           tickets = tickets.filter(name__icontains=name)
        
        tickets_serializer = TicketsViewSerializer(tickets, many=True)
        return JsonResponse(tickets_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tickets_data = JSONParser().parse(request)
        tickets_serializer = TicketsSerializer(data=tickets_data)
        if tickets_serializer.is_valid():
            tickets_serializer.save()
            return JsonResponse(tickets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tickets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tickets.objects.all().delete()
        return JsonResponse({'message': '{} Tickets were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tickets_detail(request, pk):
    try: 
        tickets = Tickets.objects.get(pk=pk) 
    except Tickets.DoesNotExist: 
        return JsonResponse({'message': 'The ticket does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tickets_serializer = TicketsViewSerializer(tickets) 
        return JsonResponse(tickets_serializer.data) 
 
    elif request.method == 'PUT': 
        tickets_data = JSONParser().parse(request) 
        tickets_serializer = TicketsSerializer(tickets, data=tickets_data)
        if tickets_serializer.is_valid(): 
            tickets_serializer.save() 
            return JsonResponse(tickets_serializer.data) 
        return JsonResponse(tickets_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tickets.delete() 
        return JsonResponse({'message': 'Ticket was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def tickets_list_active(request):
    tickets = Tickets.objects.filter(status="Active")
        
    if request.method == 'GET': 
        tickets_serializer = TicketsViewSerializer(tickets, many=True)
        return JsonResponse(tickets_serializer.data, safe=False)

 ###################################               CONNECTIONS SERIAL               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def connectionsserial_list(request):
    if request.method == 'GET':
        connectionsserial = Connectionsserial.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            connectionsserial = connectionsserial.filter(name__icontains=name)
        
        connectionsserial_serializer = ConnectionsserialSerializer(tutorials, many=True)
        return JsonResponse(connectionsserial_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        connectionsserial_data = JSONParser().parse(request)
        connectionsserial_serializer = ConnectionsserialSerializer(data=tutorial_data)
        if connectionsserial_serializer.is_valid():
            connectionsserial_serializer.save()
            return JsonResponse(connectionsserial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(connectionsserial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Connectionsserial.objects.all().delete()
        return JsonResponse({'message': '{} Serial Connections were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def  connectionsserial_detail(request, pk):
    try: 
        connectionsserial = Connectionsserial.objects.get(pk=pk) 
    except Connectionsserial.DoesNotExist: 
        return JsonResponse({'message': 'The serial connection does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        connectionsserial_serializer = ConnectionsserialSerializer(tutorial) 
        return JsonResponse(connectionsserial_serializer.data) 
 
    elif request.method == 'PUT': 
        connectionsserial_data = JSONParser().parse(request) 
        connectionsserial_serializer = ConnectionsserialSerializer(tutorial, data=tutorial_data) 
        if connectionsserial_serializer.is_valid(): 
            connectionsserial_serializer.save() 
            return JsonResponse(connectionsserial_serializer.data) 
        return JsonResponse(connectionsserial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        connectionsserial.delete() 
        return JsonResponse({'message': 'Serial Connections was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def connectionsserial_list_active(request):
    connectionsserial = Connectionsserial.objects.filter(status="Active")
        
    if request.method == 'GET': 
        connectionsserial_serializer = ConnectionsserialSerializer(connectionsserial, many=True)
        return JsonResponse(connectionsserial_serializer.data, safe=False)

 ###################################               ETHO CONNECTIONS               ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def connectionsetho_list(request):
    if request.method == 'GET':
        connectionsetho =  Connectionsetho.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            connectionsetho =  connectionsetho.filter(name__icontains=name)
        
        connectionsetho_serializer =  ConnectionsethoSerializer(connectionsetho, many=True)
        return JsonResponse( connectionsetho_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        connectionsetho_data = JSONParser().parse(request)
        connectionsetho_serializer =  ConnectionsethoSerializer(data=connectionsetho_data)
        if connectionsetho_serializer.is_valid():
            connectionsetho_serializer.save()
            return JsonResponse(connectionsetho_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(connectionsetho_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Connectionsetho.objects.all().delete()
        return JsonResponse({'message': '{} Ethernet connections were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def  connectionsetho_detail(request, pk):
    try: 
         connectionsetho =  Connectionsetho.objects.get(pk=pk) 
    except  Connectionsetho.DoesNotExist: 
        return JsonResponse({'message': 'The ethernet connection does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        connectionsetho_serializer =  ConnectionsethoSerializer(connectionsetho) 
        return JsonResponse(connectionsetho_serializer.data) 
 
    elif request.method == 'PUT': 
        connectionsetho_data = JSONParser().parse(request) 
        connectionsetho_serializer =  ConnectionsethoSerializer(connectionsetho, data= connectionsetho_data) 
        if connectionsetho_serializer.is_valid(): 
            connectionsetho_serializer.save() 
            return JsonResponse(connectionsetho_serializer.data) 
        return JsonResponse(connectionsetho_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        connectionsetho.delete() 
        return JsonResponse({'message': 'Ethernet connection was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def  connectionsetho_list_active(request):

    if request.method == 'GET': 
        connectionsetho_serializer = ConnectionsethoSerializer(connectionsetho, many=True)
        return JsonResponse( connectionsetho_serializer.data, safe=False)

 ###################################              EXPIRY DATES           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def expirydates_list(request):
    if request.method == 'GET':
        expirydates =  ExpiryDates.objects.all()
        title = request.query_params.get('name', None)
        if title is not None:
            expirydates =  expirydates.filter(name__icontains=name)
        expirydates_serializer =  ExpiryDatesSerializer(connectionsetho, many=True)
        return JsonResponse( expirydates_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        expirydates_data = JSONParser().parse(request)
        expirydates_serializer =  ExpiryDatesSerializer(data=tutorial_data)
        if expirydates_serializer.is_valid():
            expirydates_serializer.save()
            return JsonResponse(expirydates_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(expirydates_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
 
@api_view(['GET', 'PUT', 'DELETE'])
def  expirydates_detail(request, pk):
    try: 
         expirydates =  ExpiryDates.objects.get(pk=pk) 
    except ExpiryDates.DoesNotExist: 
        return JsonResponse({'message': 'Licence does not exists'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        expirydates_serializer =  ExpiryDatesSerializer(expirydates) 
        return JsonResponse(expirydates_serializer.data) 
 
    elif request.method == 'PUT': 
        expirydates_data = JSONParser().parse(request) 
        expirydates_serializer =  ExpiryDatesSerializer(expirydates, data= expirydates_data) 
        if expirydates_serializer.is_valid(): 
            expirydates_serializer.save() 
            return JsonResponse(expirydates_serializer.data) 
        return JsonResponse(expirydates_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
  
@api_view(['GET'])
def  expirydates_list_active(request):
    expirydates= ExpiryDates.objects.filter(status='Active')
        
    if request.method == 'GET': 
       expirydates_serializer = ExpiryDatesSerializer(expirydates, many=True)
       return JsonResponse( expirydates_serializer.data, safe=False)