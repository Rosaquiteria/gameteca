from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:jogo_id>', jogo, name='jogo'),
    path('buscar', buscar, name= 'buscar'),
    path('criar/jogo', criar_jogo, name='criar_jogo'),
    path('deleta/<int:jogo_id>', deleta_jogo, name='deleta_jogo'),
    path('edita/<int:jogo_id>', edita_jogo, name='edita_jogo'),
    path('atualiza_jogo', atualiza_jogo, name='atualiza_jogo'),
    path('criar/desenvolvedores', cria_desenvolvedores, name='cria_desenvolvedores')

]
