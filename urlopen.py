import sys
from urllib.request import urlopen

def fetch_words(url):
""" In our case url will be:   http://sixty-north.com/c/t.txt    
Check argparse and docopt modules"""
	with urlopen(url) as story:
		story_words =[]
		for line in story:
			#line_words = line.split() # here the data will transferred in BYTES from HTTP
			line_words =line.decode('utf-8').split() # now we deode BYTES using UTF-8
			for word in line_words:
				story_words.append(word)
	return story_words
	
def print_items(items):
	for items in items:
		print (item)

def main(url):
	url = sys.argv[1] # import Command Line Argument
	words = fetch_words(url)
	print_items(words)
		
if __name__ == '__main__':
	main(sys.argv[1])
