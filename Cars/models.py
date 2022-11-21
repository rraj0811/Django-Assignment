from django.db import models

# Create your models here.


class Cars(models.Model):

    CarName = models.CharField(max_length=30)
    ModelName = models.CharField(max_length=30)
    CarNumber = models.CharField(max_length=30)
    #CarRentPrice = db.Column(db.String(80), nullable=False)
    Features = models.TextField()
    IsAvailable = models.CharField(max_length=3)
    CarImage = models.ImageField(
        default='navimg.jpeg', upload_to='profile_pics')
    CostPerDay = models.IntegerField(default=5000)

    def __str__(self) -> str:
        return self.CarName


class otherDetails(models.Model):

    username = models.CharField(max_length=100)
    Address = models.TextField()
    phonenumber = models.CharField(max_length=10)
    NumberOfDays = models.IntegerField(default=1)

    def __str__(self):
        return self.username
