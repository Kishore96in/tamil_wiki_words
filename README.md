# Tamil Wikipedia Words
A simple Python 3 script to get a list of unique words from the Tamil Wikipedia, sorted in descending order of frequency.

## Usage
* Download `https://dumps.wikimedia.org/tawiki/latest/tawiki-latest-pages-articles.xml.bz2` and extract it using a tool of your choice.
* Copy the script to the location where you extracted the dump.
* Run `python3 get_unique_tamil_words.py` in the aforementioned directory.

## Output
One can generate either

* A list of words sorted in descending order of frequency, with each line of the output file containing a single word.
* A list as above, but with each word accompanied by the number of occurrences in the input file (a tab character separates the number and the word).

## Acknowledgments
Inspired by https://github.com/tshrinivasan/tamil-wikipedia-word-list
