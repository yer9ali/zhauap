# Generated by Django 3.2.15 on 2022-09-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='username'),
        ),
    ]
