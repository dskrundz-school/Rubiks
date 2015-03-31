import pygame
from pygame import Color
from cubemoverenderer import CubeMoveRenderer
import cube

class Button:
	def __init__(self, rect, action):
		self.rect = rect
		self.action = action
		self.enabled = True

	def activate(self, arg=None):
		if self.enabled:
			self.action(arg)

	def render(self, screen):
		pygame.draw.rect(screen, Color(40, 40, 40), self.rect, 0)
		pygame.draw.rect(screen, Color(80, 80, 80), self.rect, 1)

class TextButton(Button):
	def __init__(self, rect, text, action):
		Button.__init__(self, rect, action)
		self.text = text
		self.font = pygame.font.Font(None, 20)

	def render(self, screen):
		Button.render(self, screen)
		textBitmap = self.font.render(self.text, True, Color(255,255,255))
		w, h = textBitmap.get_size()
		x = self.rect[0] + self.rect[2]/2 - w/2
		y = self.rect[1] + self.rect[3]/2 - h/2
		screen.blit(textBitmap, (x, y))

class ImageButton(Button):
	def __init__(self, rect, image, action):
		Button.__init__(self, rect, action)
		self.image = image

	def render(self, screen):
		Button.render(self, screen)
		w, h = self.image.get_size()
		x = self.rect[0] + self.rect[2]/2 - w/2
		y = self.rect[1] + self.rect[3]/2 - h/2
		screen.blit(self.image, (x, y))

class MoveButton(Button):
	def __init__(self, x, y, cube, move, offsets):
		Button.__init__(self, (x, y, CubeMoveRenderer.size(cube.N), CubeMoveRenderer.size(cube.N)), self.cubeAction)
		self.move = move
		self.offsets = offsets
		self.cube = cube

	def cubeAction(self, arg=None):
		if self.move == cube.Cube.Top:
			cube.Cube.U(self.cube, self.offsets)
		elif self.move == cube.Cube.Top_:
			cube.Cube.U_(self.cube, self.offsets)
		elif self.move == cube.Cube.Bottom:
			cube.Cube.D(self.cube, self.offsets)
		elif self.move == cube.Cube.Bottom_:
			cube.Cube.D_(self.cube, self.offsets)
		elif self.move == cube.Cube.Left:
			cube.Cube.L(self.cube, self.offsets)
		elif self.move == cube.Cube.Left_:
			cube.Cube.L_(self.cube, self.offsets)
		elif self.move == cube.Cube.Right:
			cube.Cube.R(self.cube, self.offsets)
		elif self.move == cube.Cube.Right_:
			cube.Cube.R_(self.cube, self.offsets)
		elif self.move == cube.Cube.Front:
			cube.Cube.F(self.cube, self.offsets)
		elif self.move == cube.Cube.Front_:
			cube.Cube.F_(self.cube, self.offsets)

	def render(self, screen):
		CubeMoveRenderer.render(screen, self.rect[0], self.rect[1], self.cube.N, self.move, self.offsets)
