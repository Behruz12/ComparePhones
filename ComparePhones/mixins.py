from django.shortcuts import redirect
from django.contrib import messages


class LogoutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            messages.warning(request, "{} sizga bu tizimga kirish xuquqi yo'q. ".format(request.user.username))

            return redirect('main:index')

        return super().dispatch(request, *args, **kwargs)
