# Generated by Django 4.2.16 on 2024-11-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masala',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
    ]
