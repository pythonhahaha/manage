# coding=utf-8
import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.home_viewx),
    url(r'^a/',views.a_view),
    url(r'^b/',views.b_view),
    url(r'^c',views.c_view),
    url(r'^d/',views.d_view),
    url(r'^center',views.centera_view)
]