from django.contrib import admin
from django.urls import path, include

from . import views

name = 'kyuyo'

urlpatterns = [
    path('', views.dashborad, name='dashborad'),
    path('list/', views.KyuyoListView.as_view(), name='syunyu_list'),
    path('update/', views.Syunyu_update.as_view(), name='syunyu_update'),
]
