# Generated by Django 5.1.2 on 2024-11-02 12:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petcategory',
            name='category_image',
        ),
        migrations.AddField(
            model_name='petcategory',
            name='category_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]