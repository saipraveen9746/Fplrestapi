from django.db import models
from account.models import User


class Player(models.Model):
    web_name = models.CharField(max_length=100,blank=True)
    first_name = models.CharField(max_length=100,blank=True)
    second_name = models.CharField(max_length=100,blank=True)
    team = models.IntegerField(default=0)
    element_type = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    assists= models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    photo= models.ImageField(default='default_photo.jpg')
    position= models.CharField(max_length=200,blank=True)
    team_name= models.CharField(max_length=200,blank=True)
    influence = models.DecimalField(decimal_places=3,max_digits=7,default=0.0)
    total_points = models.IntegerField(default=0)
    selected_by_percent = models.CharField(max_length=200,blank=True)
    value_form = models.CharField(max_length=200,blank=True)
    value_season = models.CharField(max_length=200,blank=True)

class MyTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forwards = models.ManyToManyField(Player, related_name='forwards_players', limit_choices_to={'position': 'Forward'}, blank=True)
    midfielders = models.ManyToManyField(Player, related_name='midfielders_players', limit_choices_to={'position': 'Midfielder'}, blank=True)
    defenders = models.ManyToManyField(Player, related_name='defenders_players', limit_choices_to={'position': 'Defender'}, blank=True)
    gk = models.OneToOneField(Player,on_delete=models.SET_NULL ,related_name='goalkeeper_player', limit_choices_to={'position': 'Goalkeeper'}, blank=True, null=True)
    captain = models.ForeignKey(Player, on_delete=models.SET_NULL, blank=True, null=True)
    total_points = models.IntegerField(default=0)




