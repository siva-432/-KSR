# Generated by Django 3.1.4 on 2020-12-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0009_datascience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bigdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=20)),
                ('text5', models.TextField()),
            ],
        ),
    ]