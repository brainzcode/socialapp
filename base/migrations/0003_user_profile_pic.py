# Generated by Django 3.2.12 on 2023-01-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230130_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
