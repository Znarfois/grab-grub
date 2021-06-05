from django.db import models

class User (models.Model):

    #Initializing attributes
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=1000)
    objects = models.Manager()

    #Defining methods
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def __str__(self):
        # Concatenating strings to give desired output
        output = "Username: {}, Password: {}".format( self.getUsername(), self.getPassword() )  
        return output

class Food (models.Model):

    #Initializing attributes
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    price = models.FloatField()
    created_at = models.DateTimeField()
    objects = models.Manager()

    #Defining methods
    def getName(self):
        return self.name
    
    def getDesc(self):
        return self.description
    
    def getPrice(self):
        return self.price

    def __str__(self):
        output =  "{}: {} - {}, {} created at: {}".format(self.pk, self.getName(), self.getPrice(), self.getDesc(), self.created_at)  
        return output

class Customer (models.Model):
    #Initializing attributes
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=300)
    objects = models.Manager()

    #Defining methods
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def __str__(self):
        # Concatenating strings to give desired output
        output = "{}: {} - {}, {}".format( self.pk, self.getName(), self.getAddress(), self.getCity() )
        return output

class Order (models.Model):
    #Initializing attributes
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.FloatField(max_length=100)
    ordered_at = models.DateTimeField()
    cust_order = models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=4)
    objects = models.Manager()

    #Defining methods
    def getMode(self):
        return self.payment_mode
    
    def getQuantity(self):
        return self.qty

    def __str__(self):
        # Concatenating strings to give desired output
        output = "{}: Order {}: {} ({}). For {}: {}, {}. {}, ordered at {}".format(self.pk, self.pk, self.food.getName(), self.getQuantity(), self.cust_order.getName(), self.cust_order.getAddress(), self.cust_order.getCity(), self.getMode(), self.ordered_at)
        return output