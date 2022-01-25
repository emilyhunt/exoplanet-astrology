import sys

from . import dirtywords


this_module = sys.modules[__name__]

def _setup():
	"""Create lists in this module with both "clean" & dirty words."""
	for name in dir(dirtywords):
		if name[:1] == "_":
			continue

		named_object = getattr(dirtywords, name)
		if isinstance(named_object, list):
			clean_list = getattr(this_module, name)
			dirty_list = clean_list + named_object
			dirty_name = "dirty_" + name
			setattr(this_module, dirty_name, dirty_list)


def wordlist(name, dirty=False, prefix=""):
	"""Get a word list by name, with optional filth."""
	name = prefix + name
	dirty_name = "dirty_" + name
	if dirty and hasattr(this_module, dirty_name):
		return getattr(this_module, dirty_name)
	return getattr(this_module, name)


# Astrological words
planets = ["WASP-12 b", "WASP-121 b", "WASP-76 b", "AU Mic b", "55 Cnc e", "KELT-9 b", "GJ 3470 b", "HD 152843 b",
		   "beta Pic b", "PDS 70 b", "WASP-18 b", "TOI-849 b", "GJ 436 b", "51 Eri b", "WASP-107 b", "eps Indi Ab"]
stars = ["HD 209458 b", "WASP-43 b", "LHS 1140 b", "Nu2-Lupi d", "51 Pegasi b", "K2-18b", "LHS 3844 b", "HR 8799 b",
		 "WD 1856 b", "GJ 1214 b", "TRAPPIST-1 e", "MOA-477 b", "HD 189733 b", "Proxima b", "WASP-33 b",
		 "Kepler 1704 b"]

aspects = ["conjunction", "opposition", "transit", "eclipse", "observation", "orbit", "M sin i", "temperature",
		   "tidal forces", "atmosphere", "hidden exomoon", "chemical composition", "oxygen biosignature",
		   "precession", "inclination",]

wanky_events = ["a large Electromagnetic disturbance", "Quantum Flux", "stellar activity",
		"the upcoming stellar transit", "Unusual radial motion", "candidate Exomoon discovery"]


# Time words
beginnings = ["arrival", "beginning", "start"]
endings = ["end", "death", "passing"]

time_periods = ["interlude", "period", "week", "day"]

# Feeling adjectives
good_feeling_adjs = ["romantic", "emotional", "reflective", "irreverent",
			"subversive", "spiritual", "creative", "intellectual",
			"adventurous", "enlightening", "fantastic"]

bad_feeling_adjs = ["bitter", "disappointing", "frustrating"]


good_emotive_adjs = ["cathartic", "healing", "mystical",]

bad_emotive_adjs = ["anti-climactic"]

# Intensifiers for use in front of feeling adjectives
good_degrees = ["ridiculously", "amazingly"]
neutral_degrees = ["a little bit", "fairly", "pretty", "curiously"]
bad_degrees = ["worringly", "distressingly"]

# Emotive nouns
good_feeling_nouns = ["love", "reflection", "romance", "enlightenment",
			"joy", "desire", "creativity"]

good_emotive_nouns = ["healing", "catharsis", "mysticism", "transcendence",
			"metamorphisis"]

bad_feeling_nouns = ["bitterness", "disappointment", "sadness", "frustration",
			"anger", "failure", "boredom", "tension"]

bad_emotive_nouns = ["bad luck", "misfortune", "déjà vu", "scoop"]

# Misc
prediction_verbs = ["heralds", "marks", "foreshadows", "signifies"]

# You would be well advised to avoid...
avoid_list = [
	"going on the AAS jobs register",
	"starting a new paper",
	"networking at a workshop",
	"data reduction",
	"submitting an observing proposal",
	"staying inside for extended periods of time",
	"IDL",
	"making life-changing decisions",
	"Astrotwitter",
	"the rumormill",
	"other horoscopes",
	"drinking this weekend",
	"making a new figure",
	"submitting that pull request",
	"checking the arXiv",
	"submitting a paper",
	"reading a paper",
	"installing a new Python package",
	"planning an observation",
	"coffee",
	"tea",
	"caffeine",
	"writing code",
	"working on your next paper",
	"checking your emails",
	"speaking to superiors",
	"spectroscopy",
	"power laws",
	"hot Jupiters",
	"cold Jupiters",
	"brown dwarfs",
	"M dwarfs",
	"publishing papers about atmospheric phosphine",
]

# People you may meet
familiar_people = [
	"your office-mate",
	"your supervisor",
	"your closest friend",
	"a postdoc you can count on for Python questions",
	"your co-author",
	"your mentor",
]

strange_people = [
	"a lecturer",
	"a professor",
	"a staff scientist",
	"an astronaut",
	"a musical friend",
	"a mathematical friend",
	"an acquaintance",
	"someone from high school",
	"someone from university",
	"a science communicator",
	"a collaborator",
	"a distant collaborator",
	"a journalist",
	"a reviewer",
]

# Locations for various events
locations = [
	("at", "an observatory"),
	("in", "the office"),
	("in", "a dream"),
	("in", "a carpark"),
	("at", "your house"),
	("in", "your street"),
	("near", "where you studied for your undergraduate degree"),
	("in", "a bar"),
	("on top of", "a telescope dome"),
	("on", "Zoom"),
	("at", "a conference"),
	("at", "a workshop"),
	("on", "a bus"),
	("on", "a train"),
	("at", "a library")
]

# Types of discussions
neutral_discussions = [
	"discussion",
	"talk",
	"conversation",
	"meeting",
	"debate",
]

good_discussions = [
	"chat",
	"intimate conversation",
	"presentation",
	"productive meeting",
]

bad_discussions = [
	"argument",
	"fight",
	"heated debate",
	"altercation",
	"terse chat",
	"misunderstanding",
]

# Conversation topics (good or bad)
conversation_topics = [
	"the past",
	"the future",
	"your career",
	"your future",
	"exomoons",
	"JWST",
	"historical injustices of the Nobel Prize",
	"Twitter followers",
	"Python",
	"your work",
	"coffee",
	"bugs",
	"IDL",
	"data reduction",
	"habitable exoplanets",
	"alien life",
	"life on Mars",
	"life on Venus",
	"phosphine molecules",
	"your publications",
	"other fields of astronomy",
	"worm food",
	"whether astronomy and astrophysics are the same thing",
	"whether astrology is a real science",
	"Bayesian statistics",
	"machine learning",
	"conference preparation",
	"your most recent talk",
] + stars[:6]

# Run the setup function once all names have been loaded
_setup()
