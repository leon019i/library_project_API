from django.db import models
from faker import Faker

fake = Faker()


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    @classmethod
    def generate_fake_data(cls, count=30):
        for _ in range(count):
            cls.objects.create(
                title=fake.sentence(nb_words=4),  # Generate a random sentence for the title
                subtitle=fake.sentence(nb_words=6),  # Generate a random sentence for the subtitle
                author=fake.name(),  # Generate a random name for the author
                isbn=fake.isbn13()  # Generate a random ISBN-13 code
            )
