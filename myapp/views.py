from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from django.urls import reverse
from django.http import HttpResponse
from .models import Usuario
import qrcode
from io import BytesIO

# Create your views here.
def principal(request):
    return render(request, 'index.html')

def noauth(request):
    return render(request, 'home0.html')

def respiracion(request):
    return render(request, 'respiracion.html')

def about(request):
    return render(request, 'about.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('new_user')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def new_user(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = request.user
            perfil.save()
            return redirect(reverse('home'))
    else:
        form = RegistroUsuarioForm()
    return render(request, "new_user.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect("home0")

@login_required
def profile(request):
    perfil = get_object_or_404(Usuario, user=request.user)
    return render(request, 'profile.html', {'perfil': perfil})

@login_required
def edit_profile(request):
    perfil = get_object_or_404(Usuario, user=request.user)
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.qr_code = ''  # Esto forzará la regeneración del QR
            perfil.save()
            return redirect('profile')
    else:
        form = RegistroUsuarioForm(instance=perfil)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def home(request):
    perfil = get_object_or_404(Usuario, user=request.user)
    return render(request, 'home.html', {'perfil': perfil})

@login_required
def qr_code(request):
    perfil = get_object_or_404(Usuario, user=request.user)
    return render(request, 'qr_code.html', {'perfil': perfil})

@login_required
def download_qr(request):
    perfil = get_object_or_404(Usuario, user=request.user)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    num_contacto= str(perfil.num_contacto)
    texto_qr = f"{perfil.name} {perfil.apellido}\n{perfil.contacto}: {num_contacto}\nMensaje de ayuda: {perfil.texto}"
    qr.add_data(texto_qr)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    response = HttpResponse(content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
    
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    response.write(img_io.getvalue())
    
    return response
def info(request):
    return render(request, "info.html")

def tut(request):
    return render(request, "tutorial.html")


