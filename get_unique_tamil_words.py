import re
import os

wiki_dump_file = "tawiki-latest-pages-articles.xml"
tamil_chars_only_tmpfile = "py_only_tamil_chars.txt"
unique_words_output_file = "only_uniq_tamil_words.txt"

tamil_characters = ('\u0B82', '\u0B83', '\u0B85', '\u0B86', '\u0B87', '\u0B88', '\u0B89', '\u0B8A', '\u0B8E', '\u0B8F', '\u0B90', '\u0B92', '\u0B93', '\u0B94', '\u0B95', '\u0B99', '\u0B9A', '\u0B9C', '\u0B9E', '\u0B9F', '\u0BA3', '\u0BA4', '\u0BA8', '\u0BA9', '\u0BAA', '\u0BAE', '\u0BAF', '\u0BB0', '\u0BB1', '\u0BB2', '\u0BB3', '\u0BB4', '\u0BB5', '\u0BB6', '\u0BB7', '\u0BB8', '\u0BB9', '\u0BBE', '\u0BBF', '\u0BC0', '\u0BC1', '\u0BC2', '\u0BC6', '\u0BC7', '\u0BC8', '\u0BCA', '\u0BCB', '\u0BCC', '\u0BCD')

punctuation=(':', ';', '.', ',', '!','|','/','(',')') #We need to keep these punctuation marks in order to prevent words separated by these symbols from getting joined during the removal of non-whitelisted characters.

tamil_words_set = set()

with open(wiki_dump_file) as infile:
	for line in infile:
		line_only_tamil_chars = ''.join(c for c in line if ( c in tamil_characters or c.isspace() or c in punctuation ) ) #Remove all characters which are not tamil characters or spaces.
		line_only_tamil_chars = re.split('[\s'+''.join(punctuation)+']', line_only_tamil_chars)
		for word in line_only_tamil_chars:
			if len(word)>0: #Filter out empty strings
				tamil_words_set.add(word)

with open(unique_words_output_file,'w') as uniq_words:
	for word in tamil_words_set:
		uniq_words.write(word)
		uniq_words.write("\n")
