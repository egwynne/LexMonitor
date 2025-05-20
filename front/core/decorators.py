from functools import wraps
from django.http import HttpResponseForbidden


def allowed_user_types(user_types):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            user_type = user.profile.tipo_usuario 
            if str(user_type) in user_types:  
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Acceso denegado.")
        return _wrapped_view
    return decorator