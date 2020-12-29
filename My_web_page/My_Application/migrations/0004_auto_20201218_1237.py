# Generated by Django 3.1.4 on 2020-12-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0003_cource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='text1',
        ),
        migrations.AddField(
            model_name='contact',
            name='mail',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cource',
            name='text1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]