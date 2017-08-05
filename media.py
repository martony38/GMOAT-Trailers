class Movie(object):
    """ This class provides a way to store movie related information.

    Attributes:
        title: A string that contains the movie title.
        storyline: A string that contains a short synopsis of teh movie.
        poster_image_url: A string that contains the url of a poster
                          image of the movie.
        trailer_youtube_url: A string that contains the url of a Youtube
                             trailer of the movie.
        year: An integer representing the year the movie came out.
        rating: A string representing the movie rating according to the
                Motion Picture Association of America film rating system.
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url,
                 year, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.rating = rating
