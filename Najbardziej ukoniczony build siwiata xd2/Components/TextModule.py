import pygame
import os

class Text:
    def __init__(self, screen, position, text, size=12, color = (255,255,255), fontFamily='ARCADECLASSIC.TTF', centerX=False):
        self.screen = screen
        self.size = size
        self.fontFamily = os.path.join(os.getcwd(), "Fonts", fontFamily)
        self.text = text
        self.color = color
        self.position = position

        self.font = pygame.font.Font(self.fontFamily, self.size)
        self.textSurface = self.font.render(self.text, True, self.color)
        # pygame.draw.rect(self.textSurface, "white", (0,0,self.textSurface.get_width(),self.textSurface.get_height()), width=1)


    def draw(self):
        self.screen.blit(self.textSurface, self.position)

    def drawOn(self, surface):
       surface.blit(self.textSurface, self.position)
        
    def getSize(self):
        return [self.textSurface.get_width(), self.textSurface.get_height()]

    def getPosition(self): 
        return self.position

    def setPosition(self, pos):
        self.position = pos

    def setText(self, text):
        self.text = text 
        self.textSurface = self.font.render(self.text, True, self.color)
