from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from ComparePhones.mixins import LogoutRequiredMixin


class RegistrationView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Ro'xatdan o'tish"

    def get(self, request):
        return render(request, 'user/registration.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, "{} siz ro'yxatdan o'ydingiz. ".format(user.username))

            return redirect('main:index')

        return render(request, 'user/registration.html', {
            'form': form
        })


class LoginView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Tizimga kirish"

    def get(self, request):
        return render(request, 'user/login.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, "{} sizga tizimga kirdingiz. ".format(user.username))


                return redirect('main:index')

            form.add_error('password', "Login va/yoki parrol noto'g'ri!")

        return render(request, 'user/login.html', {
            'form': form
        })


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):

        logout(request)

        messages.success(request, "{} sizga tizimdan chiqdingiz. ".format(request.user.username))

        return redirect('main:index')


class ProfileView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Profile: {}".format(request.user.username)
        request.button_title = "Saqlash"

    def get(self, request):
        return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=request.user)
        })

    def post(self, request):
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, "sizni profile malumotlaringiz saqlandi.")
            return redirect('user:profile')

        return render(request, 'user/profile.html', {
            'form': form
        })



