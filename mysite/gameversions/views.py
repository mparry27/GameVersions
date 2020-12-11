from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/home.html', context)


def games(request):
    games_list = Game.objects.all()
    context = {
        'games_list': games_list,
    }
    return render(request, 'games/index.html', context)


def game_detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    game_versions = ConsoleGame.objects.filter(game=game)
    game_version_positives = {}
    game_version_negatives = {}
    for version in game_versions:
        game_version_positives[version] = ConsoleGamePositives.objects.filter(consolegame=version).values()
        game_version_negatives[version] = ConsoleGameNegatives.objects.filter(consolegame=version).values()
    context = {
        'game': game,
        'game_versions': game_versions,
        'positives': game_version_positives,
        'negatives': game_version_negatives,
    }
    return render(request, 'games/detail.html', context)


@login_required()
def create_game(request):
    form = GameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        game = Game.objects.latest('id')
        return redirect('/gameversions/games/%s' % game.id)
    return render(request, 'games/games-form.html', {'form': form})


@login_required()
def update_game(request, game_id):
    game = Game.objects.get(id=game_id)
    form = GameForm(request.POST or None, request.FILES or None, instance=game)

    if form.is_valid():
        form.save()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'games/games-form.html', {'form': form, 'game': game})


@login_required()
def delete_game(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method == "POST":
        game.delete()
        return redirect('games')

    return render(request, 'games/games-delete.html', {'game': game})


@login_required()
def create_console_game(request, game_id):
    game = Game.objects.get(id=game_id)
    form = ConsoleGameForm(request.POST or None, initial={'game': game.id})
    form.fields['game'].disabled = True
    if form.is_valid():
        form.save()

        return redirect('/gameversions/games/%s' % game.id)
    return render(request, 'console_games/console-games-form.html', {'form': form})


@login_required()
def update_console_game(request, game_id, console_game_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    form = ConsoleGameForm(request.POST or None, instance=consolegame)
    form.fields['game'].disabled = True

    if form.is_valid():
        form.save()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'console_games/console-games-form.html',
                  {'form': form, 'game': game, 'consolegame': consolegame})


@login_required()
def delete_console_game(request, game_id, console_game_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)

    if request.method == "POST":
        consolegame.delete()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'console_games/console-games-delete.html', {'consolegame': consolegame, 'game': game})


@login_required()
def create_console_game_positive(request, game_id, console_game_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    form = ConsoleGamePositivesForm(request.POST or None, initial={'consolegame': consolegame.id})
    form.fields['consolegame'].disabled = True
    if form.is_valid():
        form.save()

        return redirect('/gameversions/games/%s' % game.id)
    return render(request, 'positives/positives-form.html', {'form': form, 'game': game, 'consolegame': consolegame})


@login_required()
def update_console_game_positive(request, game_id, console_game_id, positive_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    positive = ConsoleGamePositives.objects.get(id=positive_id)
    form = ConsoleGamePositivesForm(request.POST or None, instance=positive)
    form.fields['consolegame'].disabled = True

    if form.is_valid():
        form.save()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'positives/positives-form.html', {'form': form, 'game': game, 'consolegame': consolegame,
                                                             'positive': positive})


@login_required()
def delete_console_game_positive(request, game_id, console_game_id, positive_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    positive = ConsoleGamePositives.objects.get(id=positive_id)

    if request.method == "POST":
        positive.delete()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'positives/positives-delete.html', {'positive': positive, 'game': game, 'consolegame': consolegame})


@login_required()
def create_console_game_negative(request, game_id, console_game_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    form = ConsoleGameNegativesForm(request.POST or None, initial={'consolegame': consolegame.id})
    form.fields['consolegame'].disabled = True
    if form.is_valid():
        form.save()

        return redirect('/gameversions/games/%s' % game.id)
    return render(request, 'negatives/negatives-form.html', {'form': form, 'game': game, 'consolegame': consolegame})


@login_required()
def update_console_game_negative(request, game_id, console_game_id, negative_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    negative = ConsoleGameNegatives.objects.get(id=negative_id)
    form = ConsoleGameNegativesForm(request.POST or None, instance=negative)
    form.fields['consolegame'].disabled = True

    if form.is_valid():
        form.save()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'negatives/negatives-form.html', {'form': form, 'game': game, 'consolegame': consolegame,
                                                             'negative': negative})


@login_required()
def delete_console_game_negative(request, game_id, console_game_id, negative_id):
    game = Game.objects.get(id=game_id)
    consolegame = ConsoleGame.objects.get(id=console_game_id)
    negative = ConsoleGameNegatives.objects.get(id=negative_id)

    if request.method == "POST":
        negative.delete()
        return redirect('/gameversions/games/%s' % game.id)

    return render(request, 'negatives/negatives-delete.html', {'negative': negative, 'game': game, 'consolegame': consolegame})