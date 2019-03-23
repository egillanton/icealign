from django.views.generic import ListView
from samhlida.models import Entry
from samhlida.filters import EntityFilterSet

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class SamhlidaFilteredListView(FilteredListView):
    filterset_class = EntityFilterSet
    model = Entry
    template_name = 'samhlida/samhlida_entries_list.html'
    context_object_name = 'entries'
    paginate_by = 250
