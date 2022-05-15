# Random anime choice 
from random import choice

 # list of anime!!
animeSeries = ['Shield Hero', 'Full Metal', 'The Cat One']
animeMovies = ['Mononoke Hime', 'One Peice Movie', 'Samuri X on Netflix']

# print a random anime from list
anime = input("Would you like to watch a Series or Movie?")

if anime == "Series":
    print(choice(animeSeries))

else:
    print(choice(animeMovies))

