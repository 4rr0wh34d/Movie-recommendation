# *******     Task 38            *******
# *******  Compulsory task 2     *******
# *******   watch_next.py        *******
# ------------- xxx --------------------

# This program determines the similarity in the movies description and presents you with a recommendation about what
# to watch next

# importing the spacy module
import spacy

# Loading one of the spacy's similarity comparing model to a variable.
nlp = spacy.load("en_core_web_md")


# Defining a function which takes movie description as an argument and compare it to a list of movies description
# and returns the title of most similar movie

def recommend_movie(description):
    high_similarity = 0
    next_movie = ""

    # Opening text file to compare the description passed as arguments to list of movies description on the file
    with open("movies.txt", 'r', encoding='utf-8') as movie_file:
        for line in movie_file:
            # Splitting each line into movies title and movie description
            split_line = line.strip('\n').split(':')

            # Comparing similarity between movie descriptions and checking if the similarity is the highest of all.
            # If so, assigning the variable next_movie the title of the movie to be returned.
            similarity = nlp(description).similarity(nlp(split_line[1]))

            if similarity > high_similarity:
                high_similarity = similarity
                # Assigning the movie title with the highest similarity to next_movie.
                next_movie = split_line[0]

    return next_movie


# Defining a main function where a function that returns a recommended movies is called by passing the current movie
# description as an arguments.
def main():
    # Description of Planet Hulk movie to be passed later on as an argument.
    movie_description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
    the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

    # Calling the function
    get_movie = recommend_movie(movie_description)
    print(f"The next movie recommended for you is : {get_movie}")


# Calling the main function
if __name__ == "__main__":
    main()
