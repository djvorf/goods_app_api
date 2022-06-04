from django.urls import include
from django.urls import path

urlpatterns = [
    path('v1/', include('goods.api.v1.urls'))
]