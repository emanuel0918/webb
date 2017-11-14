from django.http import HttpResponse, HttpResponseRedirect
from apli.forms import UserCreation
from django.views.generic import FormView,TemplateView, TemplateView, RedirectView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.core.urlresolvers import reverse_lazy


import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class fecha(TemplateView):
    template_name = "fecha.html"

class Registro(CreateView):
    form_class = UserCreation
    template_name = "registro.html"    
    

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url =  reverse_lazy("fecha")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'panel-login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
