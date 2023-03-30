from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import RegisterForm
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'oauth/register.html', context=context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
        else:
            context = {'form': form}
            render(request, 'oauth/register.html', context=context)


class UserLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'oauth/login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return redirect('main-page')

    def get_success_url(self):
        return reverse_lazy('main-page')

    def form_invalid(self, form):
        messages.error(self.request, 'Form is invalid')
        return self.render_to_response(self.get_context_data(form=form))
