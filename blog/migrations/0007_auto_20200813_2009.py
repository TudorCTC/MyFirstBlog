# Generated by Django 2.2.14 on 2020-08-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_bookreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='coverArt',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]