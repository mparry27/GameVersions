from django.db import models


class Game(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, db_index=True)
    developer = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    cover = models.ImageField(upload_to='images/games/cover', default='images/games/cover/Default_No_Cover.png')


class Console(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, db_index=True)
    abbreviation = models.CharField(max_length=10)
    release_date = models.DateField()
    games = models.ManyToManyField(Game, through='ConsoleGame', through_fields=('console', 'game'))
    developer = models.CharField(max_length=100)


class ConsoleGame(models.Model):

    def __str__(self):
        return_string = self.game.name
        if self.edition is not None:
            return_string += (": " + self.edition + " Edition")
        return_string += " (" + self.console.name + ", " + str(self.release_date.year) + ")"
        if self.collection is not None:
            return_string += " [" + self.collection.name + "]"
        return return_string

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    edition = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField()
    collection = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="collection", null=True, blank=True)
    original_release = models.BooleanField(default=False)
    recommended_version = models.BooleanField(default=False)


class ConsoleGamePositives(models.Model):

    def __str__(self):
        return self.name

    consolegame = models.ForeignKey(ConsoleGame, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)


class ConsoleGameNegatives(models.Model):

    def __str__(self):
        return self.name

    consolegame = models.ForeignKey(ConsoleGame, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
