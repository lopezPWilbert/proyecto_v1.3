"""
Definition of views.
"""

from django.shortcuts import render

from django.views.generic import FormView,CreateView,TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
from django.core import serializers
from django.http import HttpResponse
from allauth.account.views import *



def Denuncia(request):
    form=Denuncia_Form(request.POST or None,request.FILES or None)
    if request.method=="POST":
        if form.is_valid():
            instance=form.save(commit=False)
            titulo = form.cleaned_data.get('titulo')
            descripcion = form.cleaned_data.get('descripcion')
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud")
            img = form.cleaned_data.get("img")
            video = form.cleaned_data.get("video")
            form.save()
    return render(request, 'app/denuncia.html',{'form':form})
	


class Mapa(TemplateView):
	template_name='app/mapa.html'

