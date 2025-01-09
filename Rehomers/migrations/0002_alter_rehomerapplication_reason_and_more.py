# Generated by Django 5.1.2 on 2025-01-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rehomers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehomerapplication',
            name='reason',
            field=models.TextField(choices=[('Behavioural issues', 'Behavioural issues'), ('Busy schedule', 'Busy schedule'), ('Change in family circumstances', 'Change in family circumstances'), ('Does not get along with another pet', 'Does not get along with another pet'), ('Fostered', 'Fostered'), ('Found', 'Found or abandoned'), ('Human health issues', 'Human health issues (e.g., allergies, sickness)'), ('Infant, young children or pregnancy', 'Infant, young children or pregnancy'), ('Landlord permission issues', 'Landlord permission issues'), ('Ongoing costs', 'Ongoing costs (e.g., lost job)'), ('Pet medical expenses', 'Pet medical expenses (e.g., vet procedure)')], default='Busy schedule'),
        ),
        migrations.DeleteModel(
            name='RehomerReference',
        ),
    ]
