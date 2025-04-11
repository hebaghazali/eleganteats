from django.shortcuts import redirect, render
from django.contrib import messages

from users.decorators import anonymous_required
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView

@anonymous_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'The user has been created successfully.')
            return redirect('menu:menu_list')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@method_decorator(anonymous_required, name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

@login_required
def profile(request):
    return render(request, 'users/profile.html')
