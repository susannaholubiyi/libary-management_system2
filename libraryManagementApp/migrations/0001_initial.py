# Generated by Django 5.0.6 on 2024-06-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date_of_membership', models.DateTimeField(auto_now=True)),
                ('number_of_books_borrowed', models.IntegerField(default=0)),
                ('max_book_limit', models.IntegerField(default=3)),
                ('address', models.CharField(max_length=255)),
                ('is_signed_up', models.BooleanField(default=False)),
            ],
        ),
    ]