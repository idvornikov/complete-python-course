# Incomplete app!
from typing import Dict, List


movies_list = []


def append_movie(movies: List):
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({'title': title, 'director': director, 'year': year})


def list_movies(movies: List):
    for movie in movies:
        print_movie_info(movie)


def print_movie_info(movie):
    print(f'{movie["title"]}')
    print(f'\tdirector: {movie["director"]}')
    print(f'\tyear: {movie["year"]}')


def find_movie(movies: List):
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie['title'] == title:
            print_movie_info(movie)
            break
    else:
        print('There is no movie with this title')


def get_menu():
    menu_prompt = """
    Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, 
    or 'q' to quit:
    """

    selection = input(menu_prompt)
    while selection != 'q':
        if selection == "a":
            append_movie(movies_list)
        elif selection == "l":
            list_movies(movies_list)
        elif selection == "f":
            find_movie(movies_list)
        else:
            print('Unknown command. Please try again.')

        selection = input(menu_prompt)


get_menu()
