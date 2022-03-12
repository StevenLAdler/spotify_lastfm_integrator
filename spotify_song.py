import json
from spotipy import Spotify
        
class SpotifySong:
    def __init__(self, spotify_session: Spotify, song_url=None, title=None, artist=None, album=None):
        
        self.song_url = song_url
        self.title = title
        self.artist = artist
        self.album = album
        self.track = None
        self.spotify_session = spotify_session

    def set_track(self):
        if self.track:
            return

        if not self.song_url and not (self.title and self.artist):
            print("song url and song attributes not set")
            return 

        if self.song_url:
            self.track = self.spotify_session.track(track_id = self.song_url)
            return

        if self.title and self.artist:
            q=f"track:{self.title} artist:{self.artist}"

            if self.album:
                q+=f" album:{self.album}"

            song_search = self.spotify_session.search(q=q, type='track')
            try:
                self.track = self.spotify_session.track(track_id = song_search['tracks']['items'][0]['external_urls']['spotify'])
            except IndexError:
                print(f"Failed to find track {self.artist} - {self.title}")


    @property
    def get_track(self):
        if self.track:
            return self.track

    @property
    def get_attributes(self):
        if self.track:
            return self.track
        
    @property
    def acousticness(self):
        if self.track:
            pass