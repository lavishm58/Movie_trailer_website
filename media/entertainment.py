import movie
import fresh_tomatoes
school_of_rock=movie.Movie(poster="https://upload.wikimedia.org/wikipedia/en/4/4e/School_of_Rock_%28Cast_Cd%29.jpg",
						trailer_link="https://www.youtube.com/watch?v=XCwy6lW5Ixc",
						title="School of Rock",
						storyline="After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band."
									)
#school_of_rock.movie_trailor()
sex_tape=movie.Movie(poster="https://upload.wikimedia.org/wikipedia/en/8/86/Sex_Tape_%28film%29.jpg",
					trailer_link="https://www.youtube.com/watch?v=MPXtf621NxI",
					title="Sex Tape",
					storyline="A married couple wake up to discover that the sex tape they made the evening before has gone missing, leading to a frantic search for its whereabouts.")

guardians=movie.Movie(poster="http://i.imgur.com/nHIPzI1.jpg",
					storyline="Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that R",
								title="guardians of the galaxy",
								trailer_link="https://www.youtube.com/watch?v=2cv2ueYnKjg")

thor3=movie.Movie(poster="http://www.celebitchy.com/wp-content/uploads/2013/08/thor3.jpg",
				storyline="Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally. Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.",
				trailer_link="https://www.youtube.com/watch?v=fVnBBjjjAnY",
				title="Thor3")

list=[sex_tape,guardians,thor3,school_of_rock]

#fresh_tomatoes.open_movies_page(list)
print(movie.Movie.__name__)
#print(movie.Movie.VALID_RATINGS)