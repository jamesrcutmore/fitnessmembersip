# Generated by Django 3.2.3 on 2023-07-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='contents',
            field=models.ManyToManyField(to='members.Content'),
        ),
    ]