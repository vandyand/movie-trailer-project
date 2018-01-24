# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:04:42 2018

@author: dell
"""

import media
import fresh_tomatoes

#Create Movie objects from the movie class in module.py
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "1h 21m",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "2h 42m",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

lotr_fotr = media.Movie("Lord of the Rings - Fellowship of the Ring",
                       "A hobbit embarks on a journey to defeat an evil lord",
                       "3h 48m",
                       "http://people.exeter.ac.uk/wp222/Lord%20of%20the%20Rings/The%20Lord%20of%20the%20Rings%20-%20The%20Fellowship%20of%20the%20Ring%20(HD).jpg",
                       "https://www.youtube.com/watch?v=V75dMMIW2B4")

we_were_soldiers = media.Movie("We Were Soldiers",
                               "A movie about the Vietnam War",
                               "2h 23m",
                               "http://ftpmirror.your.org/pub/wikimedia/images/wikipedia/sr/9/9d/Weweresoldiers_poster.jpg",
                               "https://www.youtube.com/watch?v=VfGSCaSmKTM")

the_shop_around_the_corner = media.Movie("The Shop Around the Corner",
                                         "Two people fall in love",
                                         "1h 39m",
                                         "https://static1.squarespace.com/static/52310575e4b0996e8e2d0554/5705e3d6e32140f77f3d67e3/5705e95e20c64764a01dd2aa/1460005215914/shoparoundthecorner.jpg?format=500w",
                                         "https://www.youtube.com/watch?v=du-BSYQETlk")

pacific_rim = media.Movie("Pacific Rim",
                          "Big robots fight giant alien monsters",
                          "2h 12m",
                          "https://images-na.ssl-images-amazon.com/images/I/51oN05yMs3L.jpg",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

#Create TVShow objects from the TVShow class in module.py
new_girl = media.TVShow("New Girl",
                        "New girl moves to LA",
                        "Season 1",
                        "Episode 3",
                        "22m",
                        "https://borgdotcom.files.wordpress.com/2011/09/new-girl-banner.jpg?w=640",
                        "https://www.youtube.com/watch?v=D1NDNFZGY7k")

parks_and_rec = media.TVShow("Parks and Rec",
                             "Small town Indiana Parks and Rec dept. comedy",
                             "Season 2",
                             "Episode 1",
                             "21m",
                             "http://media.cleveland.com/ent_impact_movies/photo/parksandrecreationax046-261c-9jpg-b4a6ce89719e0e21.jpg",
                             "https://www.youtube.com/watch?v=5uThxAizA3o")

breaking_bad = media.TVShow("Breaking Bad",
                            "Chemistry teacher becomes meth dealer",
                            "Season 1",
                            "Episode 1",
                            "58m",
                            "https://cdn.slidesharecdn.com/ss_thumbnails/breakingbadpilotscriptforeducationalpurposes-141112024044-conversion-gate01-thumbnail-4.jpg?cb=1415760297",
                            "https://www.youtube.com/watch?v=EkHTPHQKFPo")

#Make a list of movie objects to send to fresh tomatoes module
movies = [toy_story, avatar, lotr_fotr, new_girl, we_were_soldiers, 
          the_shop_around_the_corner, pacific_rim, parks_and_rec, breaking_bad]

#Fresh tomatoes creates the html file and opens it in a browser
fresh_tomatoes.open_movies_page(movies)





