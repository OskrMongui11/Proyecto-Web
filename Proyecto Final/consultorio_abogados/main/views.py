from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Proceso
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProcesoForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.profile.is_abogado:
                    return redirect('abogado_home')
                elif user.profile.is_cliente:
                    return redirect('cliente_home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def abogado_home(request):
    return render(request, 'main/abogado_home.html')

@login_required
def cliente_home(request):
    return render(request, 'main/cliente_home.html')

@login_required
def crear_proceso(request):
    if request.method == 'POST':
        form = ProcesoForm(request.POST)
        if form.is_valid():
            proceso = form.save(commit=False)
            proceso.abogado = request.user.abogado  # Asignar el abogado actual
            proceso.save()
            return redirect('abogado_home')
    else:
        form = ProcesoForm()
    return render(request, 'main/crear_proceso.html', {'form': form})

@login_required
def ver_procesos(request):
    procesos = Proceso.objects.filter(cliente=request.user.cliente)
    return render(request, 'main/ver_procesos.html', {'procesos': procesos})
