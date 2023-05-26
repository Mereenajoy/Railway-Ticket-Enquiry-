from django.db import models
from datetime import datetime
# Create your models here.
class Register(models.Model):
    rgid = models.IntegerField("Id Of User", primary_key=True)
    username = models.CharField("User Name", max_length=30)
    email = models.EmailField("email", max_length=30)
    phno = models.IntegerField("Phone no") 
    aadhar = models.CharField("aadhar",max_length=15 , null=True)   
    password = models.CharField("password", max_length=50)
    usertype = models.CharField(max_length=5, default="U")
    
    def __str__(self):
        return self.email


class Seat(models.Model):
    name=models.CharField(max_length=100)
    rate=models.IntegerField()

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Add_Train(models.Model):
    trainname = models.CharField(max_length=30,null=True)
    train_no = models.IntegerField(null=True)
    
    departuretime=models.CharField(max_length=30,null=True)
    arrivaltime=models.CharField(max_length=30,null=True)
    # trevaltime=models.CharField(max_length=100,null=True)
    # distance=models.IntegerField(null=True)
    max_seat=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.trainname+" "+str(self.train_no)
    
class Book_details(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    seat= models.ForeignKey(Seat,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=30,null=True)
    # route=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=30,null=True)
    date1 = models.DateField(default=datetime.now().date())
    fare = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    


class Passenger(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    seat= models.ForeignKey(Seat,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=30,null=True)
    # route=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=30,null=True)
    date1 = models.DateField(default=datetime.now().date())
    fare = models.IntegerField(null=True)
    cancel_request=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Train_shedulde(models.Model):
    from_city = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,related_name="from1")
    
    to_city = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,related_name='to_city1')
    date=models.DateField()
    train=models.ForeignKey(Add_Train,on_delete=models.CASCADE)
    remaining_seats = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.train.trainname} +{self.date}'
    
    def save(self, *args, **kwargs):
        if not self.remaining_seats:
            self.remaining_seats = self.train.max_seat
        super().save(*args, **kwargs)        
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    

    
