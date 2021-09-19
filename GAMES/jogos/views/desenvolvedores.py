from django.shortcuts import render, redirect, get_object_or_404
from jogos.models import Empresa
from django.contrib import messages

def cria_desenvolvedores(request):
    if request.method == 'POST':
        nome= request.POST['nome']
        if not nome.strip():
            print('nome não pode ficar em branco')
            return redirect('cria_desenvolvedores')
        cidade= request.POST['cid']
        if not cidade.strip():
            print('cidade não pode ficar em branco')
            return redirect('cria_desenvolvedores')
        estado= request.POST['nacionalidades']
        if not estado.strip():
            print('estado não pode ficar em branco')
            return redirect('cria_desenvolvedores')
        pais= request.POST['nacionalidade']
        if not pais.strip():
            print('pais não pode ficar em branco')
            return redirect('cria_desenvolvedores')
        desenvolvedor= Empresa.objects.create(nome= nome, cidade= cidade, estado=estado, pais= pais)
        desenvolvedor.save()
        return redirect('dashboard')
    else:
        return render(request, 'desenvolvedor/cria_desenvolvedores.html')


