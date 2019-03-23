import django_filters
from samhlida.models import Entry


class EntityFilterSet(django_filters.FilterSet):
    isl_text = django_filters.CharFilter(lookup_expr='icontains')
    other_text = django_filters.CharFilter(lookup_expr='icontains')

