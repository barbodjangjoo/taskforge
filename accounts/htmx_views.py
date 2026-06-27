from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('projects_htmx:home')
        return render(request, 'accounts/login.html', {'error': 'Wrong input'})