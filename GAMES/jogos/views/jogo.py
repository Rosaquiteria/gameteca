from django.shortcuts import render, get_object_or_404, redirect
from jogos.models import Jogo, Empresa, Usuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    jogo= Jogo.objects.filter(publicado=True)
    dados= {
        'jogos': jogo
    }
    return render(request, 'index.html', dados)

def jogo(request, jogo_id):
    jogo= get_object_or_404(Jogo, pk=jogo_id)
    jogo_a_exibir={
        'jogo': jogo
    }
    return render(request, 'jogo.html', jogo_a_exibir)

def buscar(request):
    lista_jogo = Jogo.objects.filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar= request.GET['buscar']
        if nome_a_buscar:
            lista_jogo= lista_jogo.filter(nome__icontains=nome_a_buscar)

    dados = {
        'jogos': lista_jogo
    }
    return render(request, 'buscar.html', dados)


def criar_jogo(request):
    empresa = Empresa.objects.all()
    usuario = Usuario.objects.all()

    dados= {
        'empresa': empresa,
        'usuario': usuario,
    }
    if request.method == 'POST':
        print(request.POST)
        usuario = get_object_or_404(User, pk=request.user.id)
        nome = request.POST['nome']
        criador = request.POST['criador']
        datadelancamento = request.POST['datadelancamento']
        generos = request.POST['genero']
        plataformas = request.POST['plataformas']
        enredo = request.POST['enredo']
        critica = request.POST['critica']
        avaliacao = request.POST['avaliacao']
        desenvolvedores_id = request.POST.getlist('desenvolvedores')
        lista_desenvolvedores=[]
        for id in desenvolvedores_id:
            desenvolvedor= get_object_or_404(Empresa, pk=request.user.id)
            lista_desenvolvedores.append(desenvolvedor)
        capa = request.FILES['capa']
        jogo=Jogo.objects.create(usuario=usuario, nome=nome, criador=criador, datadelancamento=datadelancamento, generos=generos, plataformas=plataformas, enredo=enredo, critica=critica, avaliacao=avaliacao, capa=capa)
        jogo.desenvolvedores.set(lista_desenvolvedores)
        jogo.save()
        messages.error(request, 'Jogo cadastrado com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'jogos/cria_jogo.html', dados)


def deleta_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    jogo.delete()
    messages.error(request, 'deletado com sucesso')
    return redirect('dashboard')

def edita_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    empresa = Empresa.objects.all()
    usuario = Usuario.objects.all()

    dados= {
        'empresa': empresa,
        'usuario': usuario,
        'jogo': jogo
    }
    return render(request, 'jogos/edita_jogo.html', dados)



def atualiza_jogo(request):
    if request.method == 'POST':
        jogo_id = request.POST['jogo_id']
        j = get_object_or_404(Jogo, pk=jogo_id)
        j.nome = request.POST['nome']
        j.criador = request.POST['criador']
        j.datadelancamento = request.POST['datadelancamento']
        j.generos = request.POST['genero']
        j.plataformas = request.POST['plataformas']
        j.enredo = request.POST['enredo']
        j.critica = request.POST['critica']
        j.avaliacao = request.POST['avaliacao']
        j.desenvolvedores_id = request.POST.getlist('desenvolvedores')
        desenvolvedores_id = request.POST.getlist('desenvolvedores')
        lista_desenvolvedores = []
        for id in desenvolvedores_id:
            desenvolvedores = get_object_or_404(Empresa, pk=id)
            lista_desenvolvedores.append(desenvolvedores)
        usuario_id = request.POST['usuario']
        j.Usuario = get_object_or_404(Usuario, pk=usuario_id)
        j.desenvolvedores.set(lista_desenvolvedores)
        if 'capa' in request.FILES:
            j.capa = request.FILES['capa']
        j.save()
        messages.error(request, 'Jogo atualizado com sucesso!')
        return redirect('dashboard')


