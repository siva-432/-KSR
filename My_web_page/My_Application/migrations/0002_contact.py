# Generated by Django 3.1.4 on 2020-12-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
    ]