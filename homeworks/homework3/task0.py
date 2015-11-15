# -*- coding: utf-8 -*-
class Song:
    def __init__(self, artist, name, album, position, year, length):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.length = length

    def __repr__(self):
        return "%s by %s track № %s from %s; %s; %s" % (self.name,
                                                         self.artist,
                                                         self.position,
                                                         self.album,
                                                         self.year,
                                                         self.length)

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False




def import_songs(file_name):
    with open(file_name, 'r') as f:
        songs = []
        for line in f:
            song_inf = (line.split('\t'))
            print(line)
            song = Song(song_inf[0], song_inf[1], song_inf[2],
                        song_inf[3], song_inf[4], song_inf[5])
            songs.append(song)
    return songs


def export_songs(songs, file_names):
    with open(file_name, 'w') as f:
        line = (Song.name + '/t' + Song.artist + '/t' + Song.album + '/t' +
                Song.position + '/t' + Song.year + '/t' + Song.length)
        f.write(line)


a = import_songs("songs1.txt")
print(a[0])

