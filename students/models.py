from django.db import models
from faker import Faker
import random

fake = Faker()


# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=10, blank=False)
    EmailAddress = models.EmailField(max_length=254)
    PhoneNumber = models.CharField(max_length=12)
    Address = models.TextField()
    Department = models.TextField()
    YearOfStudy = models.IntegerField()
    DateOfBirth = models.DateField()
    Gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)
    Status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=8)

    def __str__(self):
        return self.Name

    @classmethod
    def generate_fake_data(cls, count=30):
        for _ in range(count):
            cls.objects.create(
                Name=fake.name(),
                EmailAddress=fake.email(),
                PhoneNumber=fake.phone_number(),
                Address=fake.address(),
                Department=fake.job(),
                YearOfStudy=random.randint(1, 5),  # Assuming year of study ranges from 1 to 5
                DateOfBirth=fake.date_of_birth(),
                Gender=random.choice(['M', 'F']),
                Status=random.choice(['Active', 'Inactive'])
            )
