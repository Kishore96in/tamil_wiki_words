import re
import os
import collections

wiki_dump_file = "tawiki-latest-pages-articles.xml" #input file

#Output files. Set any of the below variables to None if you are not interested in the particular file.
unique_words_output_file = "only_uniq_tamil_words.txt" #This will contain just the words, separated by newlines
unique_words_with_frequency_output_file = "tamil_words_with_frequency.txt" #This will contain the words, with frequencies listed beside them

cutoff = 100 #In unique_words_output_file, only save words which appear more than this many times in the input file.

tamil_characters = ('\u0B82', '\u0B83', '\u0B85', '\u0B86', '\u0B87', '\u0B88', '\u0B89', '\u0B8A', '\u0B8E', '\u0B8F', '\u0B90', '\u0B92', '\u0B93', '\u0B94', '\u0B95', '\u0B99', '\u0B9A', '\u0B9C', '\u0B9E', '\u0B9F', '\u0BA3', '\u0BA4', '\u0BA8', '\u0BA9', '\u0BAA', '\u0BAE', '\u0BAF', '\u0BB0', '\u0BB1', '\u0BB2', '\u0BB3', '\u0BB4', '\u0BB5', '\u0BB6', '\u0BB7', '\u0BB8', '\u0BB9', '\u0BBE', '\u0BBF', '\u0BC0', '\u0BC1', '\u0BC2', '\u0BC6', '\u0BC7', '\u0BC8', '\u0BCA', '\u0BCB', '\u0BCC', '\u0BCD')

punctuation=(':', ';', '.', ',', '!','|','/','(',')') #We need to keep these punctuation marks in order to prevent words separated by these symbols from getting joined during the removal of non-whitelisted characters.

tamil_words_set = collections.Counter()

with open(wiki_dump_file) as infile:
	for line in infile:
		line_only_tamil_chars = ''.join(c for c in line if ( c in tamil_characters or c.isspace() or c in punctuation ) ) #Remove all characters which are not tamil characters or spaces.
		line_only_tamil_chars = re.split('[\s'+''.join(punctuation)+']', line_only_tamil_chars)
		for word in line_only_tamil_chars:
			if len(word)>0: #Filter out empty strings
				tamil_words_set[word] += 1

tamil_words_sorted = sorted(tamil_words_set, key=lambda x: tamil_words_set[x], reverse=True) #Sort the words in order of frequency. See https://stackoverflow.com/a/25815414

if unique_words_output_file is not None:
	uniq_words = open(unique_words_output_file,'w')
if unique_words_with_frequency_output_file is not None:
	uniq_words_with_freq = open(unique_words_with_frequency_output_file,'w')

for word in tamil_words_sorted:
	if unique_words_output_file is not None:
		if tamil_words_set[word] > cutoff:
			uniq_words.write(word)
			uniq_words.write("\n")
	if unique_words_with_frequency_output_file is not None:
		uniq_words_with_freq.write(word)
		uniq_words_with_freq.write('\t')
		uniq_words_with_freq.write(str(tamil_words_set[word]))
		uniq_words_with_freq.write("\n")

if unique_words_output_file is not None:
	uniq_words.close()
if unique_words_with_frequency_output_file is not None:
	uniq_words_with_freq.close()
