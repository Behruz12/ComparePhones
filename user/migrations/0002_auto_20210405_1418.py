# Generated by Django 3.1.7 on 2021-04-05 14:18

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=user.models.upload_file_name),
        ),
    ]
