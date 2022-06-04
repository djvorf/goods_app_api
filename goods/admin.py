from django.contrib import admin

from .models import Goods, Profile, Image

admin.site.register((Goods, Profile, Image))
