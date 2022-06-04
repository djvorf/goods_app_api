from django_filters import rest_framework as filters

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    where_from = filters.CharFilter()
    price = filters.RangeFilter()
    weight = filters.RangeFilter()
    height = filters.RangeFilter()
    width = filters.RangeFilter()
    length = filters.RangeFilter()

    class Meta:
        model = Goods
        fields = ['where_from', 'price', 'weight', 'height', 'width', 'length']
