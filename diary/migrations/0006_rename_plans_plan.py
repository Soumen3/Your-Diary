# Generated by Django 5.0.6 on 2024-06-07 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_plans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plans',
            new_name='Plan',
        ),
    ]
