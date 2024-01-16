from django.db import models

class Song(models.Model):
	deezer_id = models.IntegerField()
	name = models.CharField(max_length=100)
	artist = models.ManyToManyField('artists.Artist')
	album = models.ManyToManyField('albums.Album')
	duration = models.IntegerField()
	preview = models.URLField(max_length=200)
	saved = models.BooleanField(default=False)
# Create your models here.
