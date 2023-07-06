# Generated by Django 3.2.3 on 2023-07-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categary',
            field=models.CharField(choices=[('nutrition', 'Nutrition plan'), ('gym', 'Gym plan')], default='nutrition', max_length=50),
        ),
    ]