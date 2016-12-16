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
american_history_x = media.Movie("American History X",
                                 "A brutal Neo Nazi skinhead named Derek Vinyard is tried and sent to prison for "
                                 "three years for the murder of two black guys who tried to steal his truck. When he "
                                 "returns from prison reformed, his younger brother Daniel Vinyard who idolizes him "
                                 "is on the brink of becoming a Neo Nazi himself.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                                 "https://www.youtube.com/watch?v=JsPW6Fj3BUI")
school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatoille = media.Movie("Ratatouille",
                         "Storyline",
                         "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")
hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch/v=PbA63a7H0bo")
#movies = [toy_story, avatar, american_history_x, school_of_rock, ratatoille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)

print (media.Movie.__name__)
print (media.Movie.__module__)
