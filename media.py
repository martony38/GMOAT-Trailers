class Movie():
	""" This class provides a way to store movie related information """

	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, year, US_rating):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.year = year
		self.rating = US_rating