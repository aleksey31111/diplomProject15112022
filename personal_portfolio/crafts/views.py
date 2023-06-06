from django.shortcuts import render, redirect

from .models import Crafts
from .forms import CraftForm


# def signupuser(request):
#
#     return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})


def index(request):
    projects = Crafts.objects.all()
    return render(request, 'crafts/crafts_index.html', {'projects': projects})


def create(request):
    if request.method == 'GET':
        return render(request, 'crafts/create_craft.html', {'form': CraftForm()})
    else:
        try:
            form = CraftForm(request.POST)
            new_craft = form.save()
            new_craft.user = request.user
            new_craft.save()
            return redirect('crafts_index')
        except ValueError:
            return render(request, 'crafts/create_craft.html',
                          {'form': CraftForm(), 'error': 'Переданы неверные данныею Попробуйте еще Раз'})
