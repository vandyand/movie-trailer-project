# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:58:55 2018

@author: dell
"""

import webbrowser

#Parent class used in Movie and TVShow classes. 
class Video():
    """This class is the parent to Movie and TVShow. It's used to define
    the title and run time of Movie and TVShow objects. It also contains 
    show_trailer and show_poster methods."""
    def __init__(self, title, run_time):
        self.title = title
        self.run_time = run_time

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    def show_poster(self):
        webbrowser.open(self.poster_image_url)


class Movie(Video):
    """This class provides a way to store movie related information.""" 
    
    VALID_RATINGS = ['G','PG','PG-13','R']
    
    def __init__(self,title,movie_storyline,movie_runtime,poster_image,trailer_youtube):
        Video.__init__(self, title, movie_runtime)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    

class TVShow(Video):
    """This class creates a TVShow object which contains information for 
    TV shows."""
    def __init__(self, title, tvshow_storyline, season, episode, tvshow_runtime, poster_image,trailer_youtube):
        Video.__init__(self, title, tvshow_runtime)
        self.storyline = tvshow_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.season = season
        self.episode = episode





