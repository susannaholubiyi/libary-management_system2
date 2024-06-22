# Generated by Django 5.0.6 on 2024-06-22 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryManagementApp', '0002_remove_user_id_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(default=0, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('year_published', models.DateField()),
                ('status', models.CharField(choices=[('B', 'BORROWED'), ('AV', 'AVAILABLE')], default='B', max_length=6)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('date_borrowed', models.DateTimeField(blank=True, null=True)),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowed_books', to='libraryManagementApp.user')),
            ],
        ),
    ]
