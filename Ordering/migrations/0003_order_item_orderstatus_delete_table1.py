# Generated by Django 4.2.1 on 2023-08-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='table1',
        ),
    ]
