"""Bullshit Generator, by Michael Sproul."""
import datetime
import random
import emoji
import numpy as np


vowels = {"a", "e", "i", "o", "u"}

def choose_uniq(exclude, *args):
	"""Choose a unique random item from a variable number of lists."""
	item = choose_from(*args)
	while item in exclude:
		item = choose_from(*args)
	return item


def choose_from(*args):
	"""Choose a random item from a variable number of lists."""
	num_words = sum([len(x) for x in args])

	# Take the ith item from the lists
	i = random.randint(0, num_words - 1)
	for (j, x) in enumerate(args):
		if i < len(x):
			return x[i]
		i -= len(x)


def sentence_case(sentence, exciting=False):
	"""Capitalise the first letter of the sentence and add a full stop."""
	sentence = sentence[0].upper() + sentence[1:]

	if sentence[-1] in {'.', '!', '?'}:
		return sentence
	elif exciting:
		return sentence + "!"
	else:
		return sentence + "."


def ing_to_ed(word):
	"""Convert `ing' endings to `ed' endings."""
	if word[-3:] == "ing":
		return (word[:-3] + "ed")
	else:
		return word


def an(word):
	"""Prefix with 'a' or 'an', as appropriate."""
	if word[0] in vowels:
		return "an %s" % word
	else:
		return "a %s" % word


def twitter_character_count(string):
	"""Counts the number of characters in a string in the same way as Twitter (i.e. an emoji is worth two.)"""
	return len(string) + emoji.emoji_count(string)


def split_string(string, characters=280):
	"""Splits a string into chunks for Twitter (of 280 characters.) Will try to split at spaces."""
	length = twitter_character_count(string)

	# We can quit if it's already fine
	if length < characters:
		return [string]

	# Otherwise, think of how to split...
	# Firstly, make a string where we remove all whitespace
	split_up_string = np.asarray(string.split())
	character_counts = [twitter_character_count(a_string) + 1 for a_string in split_up_string]

	# Work out how many times we'll have to split it up
	cumulative_n_characters = np.cumsum(character_counts)
	string_indexes = cumulative_n_characters // (characters - 6)

	# Rejoin the strings together at the identified points
	unique_indexes = np.unique(string_indexes)
	to_return = [" ".join(split_up_string[string_indexes == an_index]) for an_index in unique_indexes]

	# And add ellipses
	n_tweets = len(to_return)
	for i in range(n_tweets):

		if i != n_tweets - 1:
			to_return[i] = to_return[i] + "..."
		if i != 0:
			to_return[i] = "..." + to_return[i]

	return to_return


space_emojis = [':full_moon:', ':first_quarter_moon:', ':last_quarter_moon:', ':milky_way:', ':telescope:',
				':sparkles:', ':star:', ':star2:', ':dizzy:']


def random_space_emoji():
	return random.choice(space_emojis)


def add_random_space_emoji_to_string(string, chance=0.5):
	if random.random() <= chance:
		return string + " " + random_space_emoji() + " "
	else:
		return string


def nice_date():
	today = datetime.date.today()
	day_unit = today.day % 10

	if day_unit == 1:
		text = "st"
	elif day_unit == 2:
		text = "nd"
	elif day_unit == 3:
		text = "rd"
	else:
		text = "th"

	return today.strftime(f"%A %d{text} %B")

