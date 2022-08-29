from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

def procedimentos(request):
    return render(request, 'home.html')