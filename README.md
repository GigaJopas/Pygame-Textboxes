# Pygame-Textboxes
Simple pre-made Pygame textbox class.

Example usage:
```
import pygame
import PygameTextboxes as PyTBs

pygame.init()

scrn_height = 500
scrn_width = 500

screen = pygame.display.set_mode((scrn_width, scrn_height))

textbox1 = PyTBs.TextBox(200, 200, 100, 50, 100, True, True)
# ^ create an object of the main textbox class, first 4 arguments are x, y, width and height.
# 5th argument is max symbols, 6th argument is resizing to text and last argument is cursor blinking (if you set this to True, you have to add a tiny bit more code later on)

clock = pygame.time.Clock()
running = True
while running:
	clock.tick(60)
	screen.fill((0, 0, 0))

	mouse_x, mouse_y = pygame.mouse.get_pos() 

	keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			textbox1.get_sym(event, (mouse_x, mouse_y)) # Main input-taking function, has to be under "if event.type == pygame.KEYDOWN:". pass event as first argument and mouse position as second argument.
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				textbox1.select(event) # Second (and last) mandatory function. it checks if you're selecting the textbox in order to write in it. Again, pass event as an argument and that's it
		if textbox1.cursor_flickering == True:
			if event.type == textbox1.flickerevent:
				textbox1.cursor_flicker() # Non-mandatory, only changes anything if you set cursor blinking to true. This and the 2 lines above it must look exactly like this, expect for your textbox's name.

	pygame.draw.rect(screen, (100, 100, 100), textbox1.rect) # draw the textbox itself
	screen.blit(textbox1.text, textbox1.rect) # blit the text from the textbox onto the rect

	pygame.display.flip()
```
![showcase gif](showcase.gif)
