from django.views.generic import TemplateView

from Us.models import Customer


class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        customers = Customer.objects.all()

        context['customers'] = customers

        return context
