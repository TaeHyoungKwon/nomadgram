# Generated by Django 2.0.10 on 2019-02-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20190208_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='', verbose_name='이미지'),
        ),
    ]
