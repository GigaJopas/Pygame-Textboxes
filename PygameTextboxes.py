import pygame

class TextBox():
	def __init__(self, x, y, width, height, maxlen, adjust_size, cursor_flickering):

		self.rect = pygame.Rect(x, y, width, height)

		self.textinput = ''
		self.adjust_size = adjust_size

		self.font = pygame.font.SysFont('Arial', int((height * 0.8) // 1))
		self.text = self.font.render(str(self.textinput), True, (0, 0, 0))

		self.maxlen = maxlen

		self.selected = False

		self.extra = ''
		self.cursor_flickering = cursor_flickering

		self.flickerstage = False
		
		if self.cursor_flickering == True:
			self.flickerevent = pygame.USEREVENT + 1
	def get_sym(self, event, mouse_pos):
		if self.selected == True:
			if event.key == pygame.K_BACKSPACE:
				if len(self.textinput) >= 1:
					self.textinput = self.textinput[:-1]
			elif event.key == pygame.K_RETURN:
				self.selected = False
				self.extra = ''
			else:
				if len(self.textinput) < self.maxlen:
					if self.textinput == '|':
						self.textinput = event.unicode
					else:
						if event.key in (pygame.K_ESCAPE, pygame.K_DELETE, pygame.K_TAB):
							pass
						elif event.unicode.isprintable():
							self.textinput = self.textinput + event.unicode
			self.text = self.font.render(f"{self.textinput}{self.extra}", True, (0, 0, 0))
			if self.adjust_size == True:
				if len(self.textinput) > 0:
					self.rect.width = self.text.get_rect().width + 7
	def select(self, event):
		if self.rect.collidepoint(event.pos):
			self.selected = True
			self.extra = '|'

			if self.cursor_flickering == True:
				pygame.time.set_timer(self.flickerevent, 0)
				pygame.time.set_timer(self.flickerevent, 500)
		else:
			self.selected = False
			self.extra = ''
		self.text = self.font.render(f"{self.textinput}{self.extra}", True, (0, 0, 0))
	def cursor_flicker(self):
		if self.selected == True:
			if self.cursor_flickering == True:

				if self.flickerstage == False:
					self.extra = '|'
					self.flickerstage = True

					self.text = self.font.render(f"{self.textinput}{self.extra}", True, (0, 0, 0))

				elif self.flickerstage == True:
					self.extra = ''
					self.flickerstage = False

					self.text = self.font.render(f"{self.textinput}{self.extra}", True, (0, 0, 0))