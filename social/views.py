from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'tanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'
