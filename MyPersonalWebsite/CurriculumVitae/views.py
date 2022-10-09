from django.views.generic.base import TemplateView
from .utilities import DataMixin
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from .utilities import menu_1, menu_2


def index(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'Главная страница'
    }
    return render(request, 'CurriculumVitae/main.html', context=context)


def about(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'О сайте'
    }
    return render(request, 'CurriculumVitae/about.html', context=context)


def contact_me(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'Обратная связь'
    }
    return render(request, 'CurriculumVitae/contact_me.html', context=context)


def smth_1(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'Что-нибудь 1'
    }
    return render(request, 'CurriculumVitae/smth_1.html', context=context)


def smth_2(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'Что-нибудь 2'
    }
    return render(request, 'CurriculumVitae/smth_2.html', context=context)


def smth_3(request):
    context = {
        'menu_1': menu_1,
        'menu_2': menu_2,
        'title': 'Что-нибудь 3'
    }
    return render(request, 'CurriculumVitae/smth_3.html', context=context)


# https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#view


# class Smth_3(DataMixin, TemplateView):
#     templates_name = 'CurriculumVitae\smth_3.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Главная страница")
#         return dict(list(context.items()) + list(c_def.items()))
