# Generated by Django 3.2.16 on 2023-02-20 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(blank=True, upload_to='Uploaded Files/'),
        ),
    ]
