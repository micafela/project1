from django.shortcuts import render
from .models import Pot


# Create your views here.


def pots(request):

    pots = Pot.objects.all()
    context = {
        'pots': pots
    }

    return render(request, 'pots.html', context)


def pot(request, name):

    # fetch pot
    pot = Pot.objects.get(name=name)
    context = {
        'pot': pot
    }

    return render(request, 'pot.html', context)
