from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Fotografia

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "q" in request.GET:
        nome_a_buscar = request.GET['q']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": fotografias})

@login_required(login_url='login')
def nova_imagem(request):
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)

        if form.is_valid():
            foto = form.save(commit=False)
            foto.usuario = request.user
            foto.save()

            messages.success(request, 'Imagem cadastrada com sucesso!')

            return redirect('index')

    else:
        form = FotografiaForms()
            
    return render(request, "galeria/nova_imagem.html", {'form':form})

@login_required(login_url='login')
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        
        if form.is_valid():
            foto = form.save(commit=False)
            foto.usuario = request.user
            foto.save()

        messages.success(request, 'Imagem editada com sucesso!')

        return redirect('index')
    else:
        form = FotografiaForms(instance=fotografia)
    
    return render(request, "galeria/editar_imagem.html", {"form":form, "foto_id":foto_id})
    
@login_required(login_url='login')   
def deletar_imagem(request, foto_id):
    fotografia =Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Imagem deletada com sucesso")
    return redirect('index')

def filtro(request, categoria):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})