from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = "home.html"

class DecksPage(LoginRequiredMixin, TemplateView):
    template_name = "decks.html"

class ExpressionsPage(LoginRequiredMixin, TemplateView):   # <-- add this
    template_name = "expressions.html"
