from django.db import models

# Create your models here.

class Stat(models.Model):
    player_name = models.CharField(max_length=30)
    player_position = models.CharField(max_length=10)
    jersey_number = models.IntegerField()
    plays_from_scrimmage = models.IntegerField()
    yards_from_scrimmage = models.IntegerField()
    ave_yards_per_play_from_scrimmage = models.FloatField()
    tds_from_scrimmage = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.jersey_number, self.player_name, self.player_position)