from django import forms
from .models import *


class GameForm(forms.ModelForm):
    class Meta:
        model = Game;
        fields = ['name', 'developer', 'publisher', 'description', 'cover']


class ConsoleGameForm(forms.ModelForm):
    class Meta:
        model = ConsoleGame;
        fields = ['game', 'console', 'edition', 'release_date', 'collection', 'original_release', 'recommended_version']


class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Console;
        fields = ['name', 'abbreviation', 'release_date', 'games', 'developer']


class ConsoleGamePositivesForm(forms.ModelForm):
    class Meta:
        model = ConsoleGamePositives;
        fields = ['consolegame', 'name', 'description']


class ConsoleGameNegativesForm(forms.ModelForm):
    class Meta:
        model = ConsoleGameNegatives;
        fields = ['consolegame', 'name', 'description']
