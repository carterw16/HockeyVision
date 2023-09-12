from django.db import models
from django.contrib.postgres.fields import ArrayField

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
        db_column='game_id',
        related_name='videos')
    fps = models.FloatField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)

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
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, related_name="clusters")

class Track(models.Model):
    pred_cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="pred_tracks")
    true_cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="true_tracks", null=True)
    bboxes = ArrayField(ArrayField(models.IntegerField()), null=True)
    lifetime = ArrayField(models.IntegerField(), null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='tracks')
