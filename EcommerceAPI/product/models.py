from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title




# class Electronics(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='electronic', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Products'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title

class Products(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    

# class Mobiles(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='mobile', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Mobiles'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Furniture(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='furnitures', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Furniture'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Fashion_and_beauty(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='fashion_and_beauty', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Fashion_and_beauty'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Sports_and_hobbies(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='sports_and_hobbies', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Sports_and_hobbies'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Bikes(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='bike', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Bikes'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Vehicles(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category, related_name='vehicle', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Vehicles'
#         ordering = ['-date_created']

#     def __str__(self):
#         return self.title
    

# class Products(models.Model):
#     product_tag = models.CharField(max_length=10)
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     imageUrl = models.URLField()
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Products'
#         ordering = ['-date_created']

#     def __str__(self):
#         return '{} {}'.format(self.product_tag, self.product_name)
    


