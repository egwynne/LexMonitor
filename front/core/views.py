from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login_f
from django.conf import settings
from core.models import *
from django.db.models import Case, When, Value
from django.shortcuts import render, get_object_or_404
from core.decorators import *
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    template_name = "login.html"
    context = {}
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        # Obtener el valor de la opción "Recuérdame"
        remember_me = request.POST.get('remember-me')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            else:
                request.session.set_expiry(0)
            login_f(request, user)
            url = reverse("index") + "?param="+ "1" if user.profile.cambiar_pass else "0"
            return HttpResponseRedirect(url)
            #elif request.user.profile.tipo_usuario == "1":
            #    return redirect("index_ejecutivo")
            #else:
            #    print(request.user.profile.tipo_usuario)
            #    return redirect("index")
        else:
            logout(request)
    context['remember_me'] = request.POST.get('remember-me')
    return render(request,template_name, context)

def register_view(request, id=None):
    template_name = "register.html"
    context = {}
    return render(request,template_name, context)

@login_required(login_url='login')
def index(request):
    template_name = "index.html"
    context = {}
    param = request.GET.get("param", "")
    context['cambiar_pass'] = False
    if param == '1':
        context['cambiar_pass'] = True
    print(context)
    return render(request, template_name, context)

@login_required(login_url='login')
@allowed_user_types(["0"])
def usuarios(request):
    template_name = "usuarios.html"
    user_types = [{
        "id": tipo[0], "nombre": tipo[1]
        } for tipo in USER_TYPES ]
    users = Profile.objects.all()
    usuarios = [
        {"id": usuario.id,
         "nombre": usuario.user.first_name + " " +usuario.user.last_name,
         "status": usuario.status} for usuario in users
    ]
    context = {"user_types": user_types,"usuarios":usuarios}
    return render(request, template_name, context)

@login_required(login_url='login')
@allowed_user_types(["0","1"])
def create_regulacion(request):
    template_name = "create_regulacion.html"
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def lista_regulacion(request):
    template_name = "lista_regulacion.html"
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
@allowed_user_types(["0","1","2"])
def editar_regulacion(request, id=None):
    template_name = "editar_regulacion.html"
    context = {}
    context["id"] = id
    if id is None:
        context["id"] = 0
        print("id none pendiente error")
    return render(request, template_name, context)

@login_required(login_url='login')
def ver_regulacion(request, id=None):
    template_name = "ver_regulacion.html"
    context = {}
    context["id"] = id
    if id is None:
        context["id"] = 0
        print("id none pendiente error")
    return render(request, template_name, context)

@login_required(login_url='login')
def estadisticas(request):
    template_name = "estadisticas.html"
    context = {}
    return render(request, template_name, context)
