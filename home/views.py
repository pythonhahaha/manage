# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_viewx(request):
    return render(request,'index.html')


def a_view(request):
    return render(request,'top.html')


def b_view(request):
    return render(request, 'left.html')


def c_view(request):
    return render(request, 'down.html')


def centera_view(request):
    return render(request,'index1.html')


def d_view(request):
    return render(request,'center.html')