import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import GoodsSerializer, UserSerializer
from .services import GoodsFilter
from ...models import Goods, Image


@permission_classes((AllowAny,))
def reset_user_password(request, uid, token):
    if request.POST:
        password = request.POST.get('password1')
        payload = {'uid': uid, 'token': token, 'new_password': password}

        url = 'http://161.35.25.79:8000/auth/users/reset_password_confirm/'

        response = requests.post(url, data=payload)
        if response.status_code == 204:
            # Give some feedback to the user. For instance:
            # https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
            messages.success(request, 'Your password has been reset successfully!')
            return JsonResponse({"ok": "True"})
        else:
            return Response(response.json())
    else:
        return render(request, '../templates/reset_password.html')


@api_view(["GET"])
@permission_classes((AllowAny,))
def request_user_activation(request, uid, token):
    """
    Intermediate view to activate a user's email.
    """
    post_url = "http://161.35.25.79:8000/auth/users/activation/"
    post_data = {"uid": uid, "token": token}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def save_user(request):
    user = User.objects.get(username=request.data['username'])
    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    user.profile.phone_number = request.data['phone_number']
    user.save()
    return Response(HTTP_200_OK)


@permission_classes((AllowAny,))
class CreateGoods(APIView):

    def post(self, request):
        goods = Goods.objects.create(
            user=request.user, height=float(request.data['height']),
            description=request.data['description'], width=float(request.data['width']),
            length=float(request.data['length']), weight=float(request.data['weight']),
            where_from=request.data['where_from'], where_to=request.data['where_to'],
            date=request.data['date'], time=request.data['time'],
            price=float(request.data['price']),
        )
        goods.goodser.add(request.user)
        goods.save()
        return JsonResponse({"id": goods.id})


@permission_classes((AllowAny,))
class ListGoodser(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(profile__goodser=True)
        return queryset


class BecomeGoodser(APIView):
    def get(self, request):
        user = User.objects.get(username=request.user)
        user.profile.goodser = True
        user.save()
        return JsonResponse({"id": user.first_name})


class UnBecomeGoodser(APIView):
    def get(self, request):
        user = User.objects.get(username=request.user)
        user.profile.goodser = False
        user.save()
        return JsonResponse({"id": user.first_name})


class AddGoodser(APIView):
    def post(self, request):
        goods = Goods.objects.get(id=request.data['id'])
        goods.goodser.add(request.user)
        goods.save()
        return JsonResponse({"id": goods.id})


class MyListGoodsCreateApi(generics.ListCreateAPIView):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        queryset = Goods.objects.select_related('user').filter(user=self.request.user)
        return queryset


@permission_classes((AllowAny,))
class ListGoodsCreateApi(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GoodsFilter
    queryset = Goods.objects.prefetch_related('image').select_related('user')
    serializer_class = GoodsSerializer


@permission_classes((AllowAny,))
class GoodsDetailApi(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'uuid'
    queryset = Goods.objects.select_related('user')
    serializer_class = GoodsSerializer
