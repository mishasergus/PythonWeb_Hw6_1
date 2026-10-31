from  django.contrib import messages
from  django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Hello {user.username}")
        return redirect("menu:menu_list")
    return render(request, "accounts/register.html", {"form": form})
