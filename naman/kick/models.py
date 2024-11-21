from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Equipment(models.Model):
    CATEGORY_CHOICES = [
        ('football', 'Football'),
        ('cricket', 'Cricket'),
        ('badminton', 'Badminton'),
        ('tennis', 'Tennis'),
        ('volleyball', 'Volleyball'),
        ('basketball', 'Basketball'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('fair', 'Fair'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-Z0-9\s]+$', "Only alphanumeric characters are allowed.")]
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, "Price must be greater than zero.")]
    )
    phone = models.CharField(
        max_length=10,

    )

    address = models.TextField()
    image = models.ImageField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    pincode = models.CharField(
        max_length=10,

    )




    def __str__(self):
        return f"{self.name} - {self.user.username}"

