import spacy

nlp = spacy.load('en_core_web_md')

example ="""Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in 
peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"""

def watch_next(watched_description):
    to_watch = {}

    with open("movies.txt","r") as f:
        lines = []
        for line in f:
            line.split("\n")
            lines.append(line.replace("\n",''))
    f.close()

    for line in lines:
        line = line.split(" :")
        to_watch[line[0]] = line[1]

    watched_description.replace("\n",'')

    scores = {}

    for title, description in to_watch.items():    
        similarity = nlp(description).similarity(nlp(watched_description))
        scores[title] = similarity

    for title, similarity in scores.items():
        if similarity == max(scores.values()):
            print(f"You should watch {title} next")

user_description = input("Type in the description of a recently watched movie:\n")

watch_next(user_description)


