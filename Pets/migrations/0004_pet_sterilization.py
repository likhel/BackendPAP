# Generated by Django 5.1.2 on 2025-01-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0003_alter_pet_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='sterilization',
            field=models.CharField(max_length=255, null=True),
        ),
    ]