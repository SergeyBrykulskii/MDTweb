# Generated by Django 4.2.1 on 2023-09-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub_core', '0011_rename_customer_review_reviewer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewer_name',
            new_name='reviewer',
        ),
    ]
