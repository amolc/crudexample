from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

class CustomerAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CustomerEdit(APIView):
    def put(self, request, id):
        try:
            customer = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=404)
            
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class CustomerDelete(APIView):
    def delete(self, request, id):
        try:
            customer = Customer.objects.get(id=id)
            customer.delete()
            return Response(status=204)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=404)

class CustomerLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        print(f"Login attempt - Username: {username}, Password: {password}")
        
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)
            
        customer = Customer.objects.filter(username=username, password=password).first()
        if customer:
            print(f"Login success for: {username}")
            customer_serializer = CustomerSerializer(customer)
            return Response({'message': 'Login successful', 'customer_data': customer_serializer.data})
        
        print(f"Login failed for: {username}")
        # Using 401 for invalid credentials is more standard than 400
        return Response({'message': 'Invalid credentials'}, status=401)