# Next movie recommendation

## Description
This script is a simple recommendation engine that suggests a movie to watch based on a description of a movie that you recently watched. The script utilizes the spaCy library to compute the similarity between the descriptions of the movies you've watched and the movies stored in the `movies.txt` file.

## Requirements
- spaCy
- en_core_web_md (spaCy language model)

## Usage
1. Clone the repository to your local machine
2. Make sure you have spaCy and the en_core_web_md language model installed
3. Run the script by running the following command in your terminal: `python script_name.py`
4. Input the description of a recently watched movie when prompted
5. The script will output the title of the movie that is most similar to the description provided

## Note
- The script expects a `movies.txt` file in the same directory as the script, containing the list of movies and their descriptions in the format `"Title : Description"`
