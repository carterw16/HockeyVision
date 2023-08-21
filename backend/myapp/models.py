from django.db import models



class Game(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=500)

class Video(models.Model):
    name = models.CharField(max_length=500)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column='game_id')

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.TextField()
    team = models.TextField()

class Cluster(models.Model):
    predicted = models.BooleanField()
    junk = models.BooleanField()
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, null=True)

class Track(models.Model):
    pred_cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="pred_tracks")
    true_cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="true_tracks", null=True)
    frame_name = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
