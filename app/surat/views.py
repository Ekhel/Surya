from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import surat_masuk

@login_required
def index(request):
    return render(request,'master/dashboard.html')

@login_required
def suratmasuk(request):
    contex = {
        'item':surat_masuk.objects.all()
    }
    return render(request,'surat_masuk/r-surat-masuk.html',contex)

@login_required
def createsuratmasuk(request):
    return render(request, 'surat_masuk/c-surat-masuk.html')
