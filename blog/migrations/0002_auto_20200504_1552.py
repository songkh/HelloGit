# Generated by Django 3.0.5 on 2020-05-04 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cretaed_date',
            new_name='created_date',
        ),
    ]
