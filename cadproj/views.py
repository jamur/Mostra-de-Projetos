# Create your views here.
from django.http import HttpResponse
from cadproj.models import Projeto
from django.shortcuts import render_to_response, get_object_or_404

def show(self, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render_to_response('projetos/show.html', {'p':projeto})
    #return HttpResponse(Projeto.objects.get(id=projeto_id).titulo)
    #return HttpResponse("Ok! Parametro: %s." % projeto_id) #    pass
