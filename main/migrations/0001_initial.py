# Generated by Django 3.1.7 on 2021-04-28 15:06

import ComparePhones.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Display_dioganal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Display_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Memory_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ram_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=ComparePhones.helpers.upload_file_name)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('colors', models.CharField(max_length=100)),
                ('Approximate_price', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('battery_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.battery_type')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.brand')),
                ('display_dioganal', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.display_dioganal')),
                ('display_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.display_type')),
                ('memory_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.memory_type')),
                ('ram_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.ram_type')),
            ],
        ),
    ]
