# Generated by Django 4.1.7 on 2023-03-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
