from django.db.models import Q
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context


class TempInfo(TemplateView):
    template_name = "Home/temp_info.html"
