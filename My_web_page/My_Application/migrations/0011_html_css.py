# Generated by Django 3.1.4 on 2020-12-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0010_bigdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Html_css',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hname', models.CharField(max_length=20)),
                ('text6', models.TextField()),
            ],
        ),
    ]