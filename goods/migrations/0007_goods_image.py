# Generated by Django 3.1.6 on 2021-06-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_goods_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='actors/', verbose_name='Изображение'),
        ),
    ]
