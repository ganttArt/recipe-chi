from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'groceries_app/_base.html'
