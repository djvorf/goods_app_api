from django.contrib.auth.models import User
from rest_framework import serializers

from goods.models import Goods, Profile, Image


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'rating', 'image', 'goodser']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile', ]


class GoodsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    image = ImageSerializer(many=True, read_only=True)
    goodser = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Goods
        fields = ['user', 'id', 'height', 'description', 'width', 'length', 'weight', 'where_from', 'where_to', 'date',
                  'time', 'price', 'image', 'goodser']
