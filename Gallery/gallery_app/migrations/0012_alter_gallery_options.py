# Generated by Django 4.0.2 on 2022-12-30 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0011_alter_gallery_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-id']},
        ),
    ]
