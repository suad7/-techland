# Generated by Django 3.0.7 on 2020-06-23 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]