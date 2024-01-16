# Generated by Django 5.0.1 on 2024-01-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_remove_album_songs_album_artist'),
        ('artists', '0004_remove_artist_albums_remove_artist_songs'),
        ('songs', '0003_remove_song_albums_remove_song_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(to='albums.album'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='artists.artist'),
        ),
    ]
