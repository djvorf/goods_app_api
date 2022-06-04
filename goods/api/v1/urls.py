from django.urls import path

from .views import ListGoodsCreateApi, GoodsDetailApi, MyListGoodsCreateApi, request_user_activation, save_user, \
    CreateGoods, reset_user_password, AddGoodser, BecomeGoodser, ListGoodser, UnBecomeGoodser

urlpatterns = [
    path('goods/', ListGoodsCreateApi.as_view()),
    path('my_goods/', MyListGoodsCreateApi.as_view()),
    path('goods/<uuid:uuid>', GoodsDetailApi.as_view()),
    path('auth/<str:uid>/<str:token>', request_user_activation),
    path('auth/save_user', save_user),
    path('goods/create', CreateGoods.as_view()),
    path('reset_user_password/<str:uid>/<str:token>', reset_user_password),
    path('goods/add_goodser', AddGoodser.as_view()),
    path('goods/become_goodser', BecomeGoodser.as_view()),
    path('goods/un_become_goodser', UnBecomeGoodser.as_view()),
    path('goods/list_goodser', ListGoodser.as_view()),
]
