from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('games/', views.games, name="games"),
    path('games/<int:game_id>', views.game_detail, name="game_detail"),
    path('games/add', views.create_game, name="create_game"),
    path('games/update/<int:game_id>', views.update_game, name="update_game"),
    path('games/delete/<int:game_id>', views.delete_game, name="delete_game"),
    path('console_games/<int:game_id>/add', views.create_console_game, name="create_console_game"),
    path('console_games/<int:game_id>/update/<int:console_game_id>', views.update_console_game,
         name="update_console_game"),
    path('console_games/<int:game_id>/delete/<int:console_game_id>', views.delete_console_game,
         name="delete_console_game"),
    path('positives/<int:game_id>/<int:console_game_id>/add', views.create_console_game_positive,
         name="create_console_game_positive"),
    path('positives/<int:game_id>/update/<int:console_game_id>/update/<int:positive_id>', views.update_console_game_positive,
         name="update_console_game_positive"),
    path('positives/<int:game_id>/delete/<int:console_game_id>/delete/<int:positive_id>', views.delete_console_game_positive,
         name="delete_console_game_positive"),
    path('negatives/<int:game_id>/<int:console_game_id>/add', views.create_console_game_negative,
         name="create_console_game_negative"),
    path('negatives/<int:game_id>/update/<int:console_game_id>/update/<int:negative_id>', views.update_console_game_negative,
         name="update_console_game_negative"),
    path('negatives/<int:game_id>/delete/<int:console_game_id>/delete/<int:negative_id>', views.delete_console_game_negative,
         name="delete_console_game_negative"),
]