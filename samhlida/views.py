from samhlida.models import Entry
from samhlida.base_views import SamhlidaFilteredListView


class Biblian(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact='Biblían')
    extra_context = {'title': 'Samhliða Málheildin - Biblían'}


class Baekur(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact='Þýdd skáldverk')
    extra_context = {'title': 'Samhliða Málheildin - Þýdd skáldverk'}


class Eso(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact='Fréttatilkynningar ESO')
    extra_context = {'title': 'Samhliða Málheildin - Fréttatilkynningar ESO'}


class Fornritin(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact='Íslendingasögur')
    extra_context = {'title': 'Samhliða Málheildin - Íslendingasögur'}


class Hagstofan(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="Hagstofa Íslands")
    extra_context = {'title': 'Samhliða Málheildin - Hagstofa Íslands'}


class Kde4(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="KDE4")
    extra_context = {'title': 'Samhliða Málheildin - KDE4'}


class Ema(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="Lyfseðlar EMA")
    extra_context = {'title': 'Samhliða Málheildin - Lyfseðlar EMA'}


class Opensubtitles(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="OpenSubtitles")
    extra_context = {'title': 'Samhliða Málheildin - OpenSubtitles'}


class Ees(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="Skjöl EES")
    extra_context = {'title': 'Samhliða Málheildin - Skjöl EES'}


class Ubuntu(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="Ubuntu")
    extra_context = {'title': 'Samhliða Málheildin - Ubuntu'}


class Tatoeba(SamhlidaFilteredListView):
    queryset = Entry.objects.filter(corpus__name__iexact="Tatoeba")
    extra_context = {'title': 'Samhliða Málheildin - Tatoeba'}


class Samhlida(SamhlidaFilteredListView):
    extra_context = {'title': 'Samhliða Málheildin - Öll Gögn'}
