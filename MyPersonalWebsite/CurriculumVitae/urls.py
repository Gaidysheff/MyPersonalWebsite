from django.urls import path

from .views import about, contact_me, index, smth_1, smth_2, smth_3


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact_me/', contact_me, name='contact_me'),
    path('smth_1/', smth_1, name='smth_1'),
    path('smth_2/', smth_2, name='smth_2'),
    path('smth_3/', smth_3, name='smth_3'),
]
