# Generated by Django 5.0.2 on 2024-02-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('membership_start_date', models.DateField()),
                ('membership_end_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('fines', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('books_borrowed', models.ManyToManyField(blank=True, related_name='borrowed_by', to='books.book')),
            ],
        ),
    ]
