# This allows python to handle properly the movie titles and links with French accents: 
# encoding: utf-8 

import media
import gmoat

# add movies instances here (see what are the required arguments in media.py)
man_bites_dog = media.Movie(
	"C'est arrivé près de chez vous",
    "A crew of filmmakers follows a serial killer.",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Man_Bites_Dog_-_censored_poster.jpg",
    "https://www.youtube.com/watch?v=bcPhaieTg4o",
    1992,
    "NC-17")
dark_star = media.Movie(
	"Dark Star",
	"A satiric look at the problems experienced by a crew of bumbling astronauts on a mission to destroy rogue planets.",
	"https://upload.wikimedia.org/wikipedia/en/9/98/DarkStarposter.jpg",
	"https://www.youtube.com/watch?v=gSccwmmrS5A",
	1974,
	"G")
alien = media.Movie(
	"Alien",
	"A highly aggressive extraterrestrial creature stalks and attacks the crew of a spaceship.",
	"https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
	"https://www.youtube.com/watch?v=bEVY_lonKf4",
	1979,
	"R")
predator_2 = media.Movie(
	"Predator 2",
	"A predatory extraterrestrial creature in the middle of a drug cartel turf war.",
	"https://upload.wikimedia.org/wikipedia/en/b/b5/Predator_two.jpg",
	"https://www.youtube.com/watch?v=6yPdBVUP5Zw",
	1993,
	"R")
lord_of_the_rings_1 = media.Movie(
	"The Fellowship of The Ring",
	"Hobbits, Elves, Dwarfs and Wizards!!!",
	"https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=V75dMMIW2B4",
	2001,
	"PG-13")
la_cite_de_la_peur = media.Movie(
	"La Cité de la peur",
	"A killer copies a movie villain's modus operandi at the Cannes Film Festival, attended by the star, his publicist and an inept bodyguard.",
	"https://upload.wikimedia.org/wikipedia/en/a/ac/La_Cité_de_la_peur.jpg",
	"https://www.youtube.com/watch?v=CItygwB9mfY",
	1994,
	"Not rated")

# edit this list to add or remove movies listed on the web app 
movies = [lord_of_the_rings_1, man_bites_dog, dark_star, alien, predator_2, la_cite_de_la_peur]

# this creates the html file and open it in default browser
gmoat.open_movies_page(movies)

