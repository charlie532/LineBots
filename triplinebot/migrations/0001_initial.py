# Generated by Django 4.1.3 on 2022-11-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
