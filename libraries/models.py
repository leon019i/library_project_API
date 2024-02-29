from django.db import models
from books.models import Book
from faker import Faker
import random

fake = Faker()


# Create your models here.

class LibraryMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    membership_start_date = models.DateField()
    membership_end_date = models.DateField()
    status = models.CharField(max_length=20)
    books_borrowed = models.ManyToManyField(Book, related_name='borrowed_by', blank=True)
    fines = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    @classmethod
    def generate_fake_data(cls, count=30):
        for _ in range(count):
            member = cls.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_birth=fake.date_of_birth(),
                membership_start_date=fake.date_this_decade(),  # Assuming membership started within this decade
                membership_end_date=fake.future_date(end_date="+1y"),  # Assuming membership ends within 1 year
                status=random.choice(['Active', 'Inactive']),
                fines=random.uniform(0, 1000)  # Assuming fines can range from 0 to 1000
            )
            # Add some random books borrowed by the member
            books = Book.objects.order_by('?')[:random.randint(0, 5)]  # Assuming a member can borrow up to 5 books
            member.books_borrowed.set(books)
