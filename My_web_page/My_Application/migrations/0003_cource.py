# Generated by Django 3.1.4 on 2020-12-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image1', models.TextField()),
                ('image2', models.TextField()),
                ('image3', models.TextField()),
                ('image4', models.TextField()),
                ('image5', models.TextField()),
            ],
        ),
    ]
