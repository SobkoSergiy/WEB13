# Generated by Django 5.0.1 on 2024-02-01 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='tag',
            new_name='tags',
        ),
    ]
