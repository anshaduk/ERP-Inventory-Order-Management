from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Product,Supplier
from . serializers import ProductSerializer,ProductCreateSerializer,SupplierSerializer

class ProductListCreateView(APIView):
    def get(self,request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request):
        try:
            serializer = ProductCreateSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                return Response(ProductSerializer(product).data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SupplierListCreateView(APIView):
    def get(self, request):
        try:
            suppliers = Supplier.objects.all()
            serializer = SupplierSerializer(suppliers, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = SupplierSerializer(data=request.data)
            if serializer.is_valid():
                supplier = serializer.save()
                return Response(SupplierSerializer(supplier).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)