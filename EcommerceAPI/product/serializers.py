from rest_framework import serializers
from . models import Category, Products
#  Mobiles, Furniture, Fashion_and_beauty, Sports_and_hobbies, Bikes, Vehicles, Products


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'
        )
        model = Products

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep


# class MobilesSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Mobiles


# class FurnitureSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Furniture 


# class Fashion_and_beautySerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Fashion_and_beauty


# class Sports_and_hobbiesSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Sports_and_hobbies


# class BikesSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Bikes



# class VehiclesSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'imageUrl',
#             'status',
#             'date_created'
#         )
#         model = Vehicles



# class ProductsSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = (
#             'id',
#             'product_tag',
#             'name',
#             'category',
#             'price',
#             'stock',
#             'imageUrl',
#             'status',
#             'date_created'

#         )
#         model = Products