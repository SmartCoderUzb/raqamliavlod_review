# Generated by Django 5.1.3 on 2024-11-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontest', '0005_userkontestrelation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='kirish',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='output',
            field=models.TextField(),
        ),
    ]
