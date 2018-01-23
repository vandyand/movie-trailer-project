# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:04:42 2018

@author: dell
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

lotr_fotr = media.Movie("Lord of the Rings - Fellowship of the Ring",
                       "A hobbit embarks on a journey to defeat an evil lord",
                       "http://people.exeter.ac.uk/wp222/Lord%20of%20the%20Rings/The%20Lord%20of%20the%20Rings%20-%20The%20Fellowship%20of%20the%20Ring%20(HD).jpg",
                       "https://www.youtube.com/watch?v=V75dMMIW2B4")

we_were_soldiers = media.Movie("We Were Soldiers",
                               "A movie about the Vietnam War",
                               "http://ftpmirror.your.org/pub/wikimedia/images/wikipedia/sr/9/9d/Weweresoldiers_poster.jpg",
                               "https://www.youtube.com/watch?v=VfGSCaSmKTM")

the_shop_around_the_corner = media.Movie("The Shop Around the Corner",
                                         "Two people fall in love",
                                         "https://static1.squarespace.com/static/52310575e4b0996e8e2d0554/5705e3d6e32140f77f3d67e3/5705e95e20c64764a01dd2aa/1460005215914/shoparoundthecorner.jpg?format=500w",
                                         "https://www.youtube.com/watch?v=du-BSYQETlk")

pacific_rim = media.Movie("Pacific Rim",
                          "Big robots fight giant alien monsters",
                          "https://images-na.ssl-images-amazon.com/images/I/51oN05yMs3L.jpg",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

#movies = [toy_story, avatar, lotr_fotr, we_were_soldiers, 
#          the_shop_around_the_corner, pacific_rim]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)






