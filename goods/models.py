import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


class Profile(TimeStampedModel):
    image = models.ImageField("Изображение", upload_to="prodile/", default=None, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField('Номер телефона', max_length=50, default='00000000000', null=True)
    rating = models.FloatField('Рейтинг', default=5.0)
    goodser = models.BooleanField("Исполнитель", default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Image(TimeStampedModel):
    image = models.ImageField("Изображение", upload_to="images/", default=None, null=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Goods(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ManyToManyField(Image, verbose_name="Изображение", related_name='goods_images')
    price = models.PositiveIntegerField('Цена', null=True)
    description = models.TextField('Описание')
    height = models.FloatField('Высота', default=0.0)
    width = models.FloatField('Ширина')
    length = models.FloatField('Длина')
    weight = models.FloatField('Вес')
    where_from = models.CharField('Откуда', max_length=200)
    where_to = models.CharField('Куда', max_length=200)
    date = models.DateField('Когда')
    time = models.TimeField('Во-сколько')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=2)
    goodser = models.ManyToManyField(User, verbose_name='Исполнители', related_name='goodser', default=user)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
