"""
7.	Spoopify

You are tasked to create three classes: a Song class, an Album class, and a Band class.

The Album class should receive a name (string) upon initialization and might receive one or more songs.
It also has instance attributes: published (False by default) and songs (an empty list).

It has four methods:
-	add_song(song: Song)
o	Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
o	If the song is single, returns "Cannot add {song_name}. It's a single"
o	If the album is published, returns "Cannot add songs. Album is published."
o	If the song is already added, return "Song is already in the album."

-	remove_song(song_name: str)
o	Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
o	If the song is not in the album, returns "Song is not in the album."
o	If the album is published, returns "Cannot remove songs. Album is published."

-	publish()
o	Publishes the album (set to True) and returns "Album {name} has been published."
o	If the album is published, returns "Album {name} is already published."

-	details()
o	Returns the information of the album, with the songs in it, in the format:
"Album {name}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"
"""

from project.song import Song


class Album:
    PUBLISHED_INITIAL = False

    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name

        self.published = Album.PUBLISHED_INITIAL
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return 'Cannot add songs. Album is published.'

        for album_song in self.songs:
            if song.name == album_song.name:
                return 'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'

        for album_song in self.songs:
            if album_song.name == song_name:
                self.songs.remove(album_song)
                return f'Removed song {song_name} from album {self.name}.'

        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        result = f'Album {self.name}\n'

        for song in self.songs:
            result += f'== {song.get_info()}\n'

        return result