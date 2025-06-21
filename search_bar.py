import pygame as pg

pg.font.init()


class SearchBar(pg.sprite.Sprite):
	def __init__(self, x, y, w, font):
		super().__init__()
		self.caret_visible = True
		self.caret_timer = 0
		self.caret_interval = 300  # milliseconds
		self.rect = None
		self.image = None
		self.color = (255, 255, 255)
		self.backcolor = None
		self.pos = (x, y)
		self.width = w
		self.font = font
		self.active = False
		self.text = ""
		self.render_text()
	
	def render_text(self):
		t_surf = self.font.render(self.text, True, self.color, self.backcolor)
		self.image = pg.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10), pg.SRCALPHA)
		if self.backcolor:
			self.image.fill(self.backcolor)
		self.image.blit(t_surf, (5, 5))
		if self.active and self.caret_visible:
			caret_x = t_surf.get_width() + 5
			caret_y = 5
			caret_height = t_surf.get_height()
			pg.draw.line(self.image, self.color, (caret_x, caret_y), (caret_x, caret_y + caret_height), 2)
		pg.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
		self.rect = self.image.get_rect(topleft=self.pos)
	
	def update(self, event_list, dt):
		self.caret_timer += dt
		if self.caret_timer >= self.caret_interval:
			self.caret_visible = not self.caret_visible
			self.caret_timer = 0
			self.render_text()
		for event in event_list:
			if event.type == pg.MOUSEBUTTONDOWN and not self.active:
				self.active = self.rect.collidepoint(event.pos)
			if event.type == pg.KEYDOWN and self.active:
				if event.key == pg.K_RETURN:
					self.active = False
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				self.render_text()
