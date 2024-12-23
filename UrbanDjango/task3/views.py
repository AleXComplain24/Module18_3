from django.shortcuts import render

# Create your views here.

def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    games = {
        'Игра 1': 500,
        'Игра 2': 800,
        'Игра 3': 1200,
    }
    return render(request, 'third_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'third_task/cart.html')