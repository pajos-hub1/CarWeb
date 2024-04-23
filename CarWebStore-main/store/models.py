from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Your existing fields...
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    car_status = models.CharField(max_length=20)
    mileage = models.IntegerField()  # Use IntegerField for mileage
    year = models.PositiveIntegerField()
    description = models.TextField(default='')
    engine_type = models.CharField(max_length=100, default='')
    transmission_type = models.CharField(max_length=50, default='')
    fuel_type = models.CharField(max_length=30, default='')
    cooling_system = models.CharField(max_length=50, default='')
    engine_condition = models.CharField(max_length=10, default='')
    transmission_condition = models.CharField(max_length=10, default='')
    suspension_condition = models.CharField(max_length=10, default='')
    custom_duty = models.CharField(max_length=10, default='')

    # New field for kms classification
    kms_classification = models.CharField(max_length=10, default='', editable=False)

    def save(self, *args, **kwargs):
        # Determine the kms classification based on mileage
        if self.mileage <= 5000:
            self.kms_classification = 'Low Kms'
        else:
            self.kms_classification = 'High Kms'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name  
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart for {self.user.username if self.user else 'Anonymous'}"