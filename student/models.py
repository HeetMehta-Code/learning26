from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Admin(models.Model):
    adminid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin {self.userid.email}"

class Vendor(models.Model):
    vendorid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    shopname = models.CharField(max_length=100)

    def __str__(self):
        return self.shopname

class Customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.userid.email

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    vendorid = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=100)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

class Cart(models.Model):
    cartid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Cart {self.cartid}"


class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)
    totalAmount = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"Order {self.orderid}"

class Payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    paymentType = models.CharField(max_length=50)
    paymentStatus = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.paymentid}"

class Review(models.Model):
    reviewid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Review {self.reviewid}"
