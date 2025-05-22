from django.contrib import admin
from django.urls import path
import core.views as core_views
import core.api as core_apis
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", core_views.login_view, name="login"),
    path("register/", core_views.register_view, name="register"),

    path("index/", core_views.index, name="index"),
    path("usuarios/", core_views.usuarios, name="usuarios"),
    path("crear_regulacion/", core_views.create_regulacion, name="create_regulacion"),
    path("lista_regulaciones/", core_views.lista_regulacion, name="lista_regulaciones"),
    path("estadisticas/", core_views.estadisticas, name="estadisticas"),
    path("editar/regulacion/<int:id>/", core_views.editar_regulacion, name="editar_regulacion"),
    path("ver/regulacion/<int:id>/", core_views.ver_regulacion, name="ver_regulacion"),
    
    path("api/get/dashboards/", core_apis.GetDashboards.as_view(), name="api/get/dashboards/"),


    path("api/get/usuarios/", core_apis.GetUsers.as_view(), name="api/get/usuarios/"),
    path("api/create/usuario/", core_apis.CreateUser.as_view(), name="api/create/usuario/"),
    path("api/edit/usuario/", core_apis.EditUser.as_view(), name="api/edit/usuario/"),
    path("api/change/status/user/", core_apis.CambiarStatusUsers.as_view(), name="api/change/status/user/"),
    path("api/change/password/", core_apis.ChangePassword.as_view(), name="api/change/password/"),
    path('api/core/accounts_profile/',  core_apis.GetAccountsProfile.as_view(), name='accounts_profile'),

    path("api/get/correlativo/", core_apis.GetCorrelativo.as_view(), name="api/get/correlativo/"),
    path("api/get/regulaciones/", core_apis.GetRegulaciones.as_view(), name="api/get/regulaciones/"),
    path("api/get/regulacion/", core_apis.GetRegulacion.as_view(), name="api/get/regulacion/"),
    path("api/get/historial/comentarios/", core_apis.GetHistorialComentarios.as_view(), name="api/get/historial/comentarios/"),
    path("api/create/regulacion/", core_apis.CreateRegulacion.as_view(), name="api/create/regulacion/"),
    path("api/editar/regulacion/", core_apis.EditarRegulacion.as_view(), name="api/editar/regulacion/"),
    path("api/editar/regulacion/status/", core_apis.EditarStatusRegulacion.as_view(), name="api/editar/regulacion/status/"),
    path("api/agregar/comentario/", core_apis.AgregarComentario.as_view(), name="api/agregar/comentario/"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))