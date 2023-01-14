# import required libraries
import spacy

# load the language model
nlp = spacy.load('en_core_web_md')

# example description to be used for testing the function instead of the user input
example ="""Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in 
peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"""

def watch_next(watched_description):
    """A function that returns the most similar movie in the movies.txt
    based on a give description of a movie watched recently.

    Args:
        watched_description (str): a description of a movie to which the comparison will be made
    """
    
    to_watch = {}
    # reading "movies.txt" and assigning the lines values to "lines" list 
    with open("movies.txt","r") as f:
        lines = []
        for line in f:
            line.split("\n")
            lines.append(line.replace("\n",''))
    f.close()

    # updating "to_watch" dict where the key is the movie title and 
    # the value is the movie description
    for line in lines:
        line = line.split(" :")
        to_watch[line[0]] = line[1]

    watched_description.replace("\n",'')

    scores = {}

    # generating the similarity scores and
    # adding each title and it's similarity score to the "scores" dict
    for title, description in to_watch.items():    
        similarity = nlp(description).similarity(nlp(watched_description))
        scores[title] = similarity

    # checking which movie from the list has the highest similarity and
    # returning it to the user
    for title, similarity in scores.items():
        if similarity == max(scores.values()):
            print(f"You should watch {title} next")

# requesting the user movie description input
user_description = input("Type in the description of a recently watched movie:\n")

# running the function with the user input
watch_next(user_description)


