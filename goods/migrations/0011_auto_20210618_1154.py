# Generated by Django 3.1.6 on 2021-06-18 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0010_auto_20210618_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goodser',
            field=models.ManyToManyField(default=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), related_name='goodser', to=settings.AUTH_USER_MODEL, verbose_name='Исполнители'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]