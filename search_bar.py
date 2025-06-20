import pygame as pg


class SearchBar:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	
	def draw(self, screen: pg.Surface):
		surface = pg.Surface((self.width, self.height))
		screen.blit(surface, (self.x, self.y))
