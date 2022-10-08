
menu_1 = [{'title': "Главная страница", 'url_name': 'home'},
          {'title': "О сайте", 'url_name': 'about'},
          {'title': "Обратная связь", 'url_name': 'contact_me'},
          ]

menu_2 = [{'title': "Что-нибудь 1", 'url_name': 'smth_1'},
          {'title': "Что-нибудь 2", 'url_name': 'smth_2'},
          {'title': "Что-нибудь 3", 'url_name': 'smth_3'},
          ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu_1'] = menu_1
        context['menu_2'] = menu_2

        return context
