# Generated by Django 2.1.7 on 2019-06-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190611_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to='post1_image'),
        ),
    ]