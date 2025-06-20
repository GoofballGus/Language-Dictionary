import json
import pygame as pg
import rapidfuzz as fuzzy
import re

pg.font.init()

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("German Dictionary")

clock = pg.time.Clock()
run = True

font = pg.font.Font(None, 80)

with open('german_words.json', 'r') as file:
	words = json.load(file)


def special_unicode_repr(text: str) -> str:
	# Matches U+XXXX or U+XXXXXX and replaces with the actual character
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
	
	titleText = font.render("German Dictionary", True, (0, 255, 0))
	screen.blit(titleText, ((800 - titleText.get_width()) // 2, 25))


query = input("English word: ").lower()
english_words = words["words"]

match = find_fuzzy_match(query, english_words)
if match:
	german = english_words[match]["translation"]
	print(f"Matched: {match} → {special_unicode_repr(german)}")
else:
	print("No good match found.")

while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
			pg.quit()
			quit()
		
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			mousePos = pg.mouse.get_pos()
			print("Yay!")
	
	clock.tick(60)
	draw()
	pg.display.flip()
