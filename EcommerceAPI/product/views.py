from django.shortcuts import render
from rest_framework import generics
from .models import Category, Products
# Mobiles, Furniture, Fashion_and_beauty, Sports_and_hobbies, Bikes, Vehicles, Products
from .serializers import CategorySerializer, ProductsSerializer
#  MobilesSerializer, FurnitureSerializer, Fashion_and_beautySerializer, Sports_and_hobbiesSerializer, BikesSerializer, VehiclesSerializer, ProductsSerializer
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Electronics
class ListProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class DetailProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

#Mobiles
# class ListMobiles(generics.ListCreateAPIView):
#     queryset = Mobiles.objects.all()
#     serializer_class = MobilesSerializer

# class DetailMobiles(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Mobiles.objects.all()
#     serializer_class = MobilesSerializer

# #Furniture
# class ListFurniture(generics.ListCreateAPIView):
#     queryset = Furniture.objects.all()
#     serializer_class = FurnitureSerializer

# class DetailFurniture(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Furniture.objects.all()
#     serializer_class = FurnitureSerializer

#Fashion_and_beauty
# class ListFashion_and_beauty(generics.ListCreateAPIView):
#     queryset = Fashion_and_beauty.objects.all()
#     serializer_class = Fashion_and_beautySerializer

# class DetailFashion_and_beauty(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Fashion_and_beauty.objects.all()
#     serializer_class = Fashion_and_beautySerializer

# #Sports_and_hobbies
# class ListSports_and_hobbies(generics.ListCreateAPIView):
#     queryset = Sports_and_hobbies.objects.all()
#     serializer_class = Sports_and_hobbiesSerializer

# class DetailSports_and_hobbies(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sports_and_hobbies.objects.all()
#     serializer_class = Sports_and_hobbiesSerializer


# #Bikes
# class ListBikes(generics.ListCreateAPIView):
#     queryset = Bikes.objects.all()
#     serializer_class = BikesSerializer

# class DetailBikes(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Bikes.objects.all()
#     serializer_class = BikesSerializer


# #Bikes
# class ListVehicles(generics.ListCreateAPIView):
#     queryset = Vehicles.objects.all()
#     serializer_class = VehiclesSerializer

# class DetailVehicles(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vehicles.objects.all()
#     serializer_class = VehiclesSerializer


# #Products
# class ListProducts(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# class DetailProducts(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer






