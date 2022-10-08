from django.shortcuts import render
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
