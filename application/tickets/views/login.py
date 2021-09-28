# -*- coding: utf-8 -*-

# Python
from __future__                import unicode_literals

# Django
from django.shortcuts          import render
from django.contrib.auth       import login as auth_login
from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.http               import HttpResponseRedirect
from django.template.response  import TemplateResponse

# App

class LoginView(LoginView):
    authentication_form = AuthenticationForm
    #success_url = '/home/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
