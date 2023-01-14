from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def aluno(request):
    return render(request, 'aluno.html')

# Create your views here.