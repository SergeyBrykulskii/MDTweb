# Generated by Django 4.2.1 on 2023-09-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='person_photo/'),
        ),
    ]
