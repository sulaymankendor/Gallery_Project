# Generated by Django 4.0.2 on 2022-12-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0004_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('-time',)},
        ),
    ]