# Generated by Django 3.2.25 on 2024-11-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='/media/img/noimage.webp', null=True, upload_to='pfiles/'),
        ),
    ]
