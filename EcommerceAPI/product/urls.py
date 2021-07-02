from django.urls import path
from . views import ListCategory, DetailCategory,ListProducts, DetailProducts
# ListElectronics, DetailElectronics, ListMobiles, DetailMobiles, ListFurniture, DetailFurniture, ListFashion_and_beauty, DetailFashion_and_beauty, ListSports_and_hobbies, DetailSports_and_hobbies, ListBikes, DetailBikes, ListVehicles, DetailVehicles, ListProducts, DetailProducts

urlpatterns = [ 
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    #Basically for electronics
    path('', ListProducts.as_view(), name='addproduct'),
    path('<int:pk>/', DetailProducts.as_view(), name='singleaddproduct'),

    # path('mobiles', ListMobiles.as_view(), name='mobiles'),
    # path('mobiles/<int:pk>/', DetailMobiles.as_view(), name='singlemobile'),

    # path('furnitures', ListFurniture.as_view(), name='furnitures'),
    # path('furnitures/<int:pk>/', DetailFurniture.as_view(), name='singlefurniture'),

    # path('fashion_and_beauty', ListFashion_and_beauty.as_view(), name='fashion_and_beauty'),
    # path('fashion_and_beauty/<int:pk>/', DetailFashion_and_beauty.as_view(), name='singlefashion_and_beauty'),

    # path('sports_and_hobbies', ListSports_and_hobbies.as_view(), name='sports_and_hobbies'),
    # path('sports_and_hobbies/<int:pk>/', DetailSports_and_hobbies.as_view(), name='singlesport_and_hobby'),

    
    # path('bikes', ListBikes.as_view(), name='bikes'),
    # path('bikes/<int:pk>/', DetailBikes.as_view(), name='singlebike'),

    
    # path('vehicles', ListVehicles.as_view(), name='vehicles'),
    # path('vehicles/<int:pk>/', DetailVehicles.as_view(), name='singlevehicle'),


    # path('products', ListProducts.as_view(), name='products'),
    # path('products/<int:pk>/', DetailProducts.as_view(), name='singleproduct'),


    

    

]


