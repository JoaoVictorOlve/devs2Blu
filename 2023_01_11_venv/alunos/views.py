from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Alunos



def index(request):

    dados = Alunos.objects.all()

    return render(request, "index.html", {'dados' : dados})
    

def aluno(request, aluno_id):
    alunos = get_object_or_404(Alunos, pk=aluno_id)
    aluno_a_exibir = {
        'aluno' : alunos
    }

    return render(request, 'aluno.html', aluno_a_exibir)




# Create your views here.