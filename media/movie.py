import webbrowser

class Video():
	def __init__(self,title,duration):
		self.title=title
		self.duration=duration

class Movie(Video):
	VALID_RATINGS=["GOOD","BAD","AVG","MINDBLOWING"]
	def __init__(self,poster,trailer_link,title,storyline,duration):
		Video.__init__(self,title,duration)
		self.poster=poster
		self.trailer_link=trailer_link
		self.storyline=storyline

	def movie_trailor(self):
		webbrowser.open(self.trailer_link)

class Tvshow(Video):
	def __init__(self,season,episode,title,duration):
		Video.__init__(self,title,duration)
		self.season=season
		self.episode=episode
