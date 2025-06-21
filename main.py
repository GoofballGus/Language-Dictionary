import json
import pygame as pg
import rapidfuzz as fuzzy
import re
from search_bar import SearchBar

pg.font.init()

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Language Dictionary")

clock = pg.time.Clock()
run = True

font = pg.font.Font(None, 80)
searchBar = SearchBar(100, 150, 600, font)
group = pg.sprite.Group(searchBar)

with open('translations/english to german.json', 'r') as file:
	words = json.load(file)


def special_unicode_repr(text: str) -> str:
	return re.sub(r'U\+([0-9A-F]{4,6})', lambda m: chr(int(m.group(1), 16)), text)


def find_fuzzy_match(query: str, dictionary: dict[str, dict[str, str]], threshold: int = 60) -> str | None:
	result = fuzzy.process.extractOne(
		query,
		list(dictionary.keys()),
		scorer=fuzzy.fuzz.WRatio
	)
	if result and result[1] >= threshold:
		return result[0]
	return None


def draw():
	screen.fill((0, 0, 0))
	
	group.draw(screen)
	
	titleText = font.render("Language Dictionary", True, (0, 255, 0))
	screen.blit(titleText, ((800 - titleText.get_width()) // 2, 25))


def search(query):
	english_words = words["words"]
	
	match = find_fuzzy_match(query, english_words)
	if match:
		german = english_words[match]["translation"]
		print(f"Closest matched: {match} → {special_unicode_repr(german)}")
	else:
		print("No good match found.")


while run:
	eventList = pg.event.get()
	for event in eventList:
		if event.type == pg.QUIT:
			run = False
			pg.quit()
			quit()
		
		keys = pg.key.get_pressed()
		if keys[pg.K_RETURN] or keys[pg.K_KP_ENTER]:
			print(searchBar.text)
			search(searchBar.text)
	
	group.update(eventList, clock.tick(60))
	
	clock.tick(60)
	draw()
	pg.display.flip()
