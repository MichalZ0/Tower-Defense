from os import walk
import pygame
import math

from Components import TextModule 


def isHovered(event): 
    for button in Button.buttons:
        if (button.buttonRect.collidepoint(event.pos)):
            button.hover()
        else:
            button.color = 'blue'
        

class Button:
    buttons = []
    def __init__(self, screen, size, position, color, text, padding=30, contentPosition=None, borderRadius=0, hover=False, hoverBg = None, image_path=None):
        self.screen = screen
        self.position = position
        self.color = color
        self.text = text
        self.padding = padding
        self.size = size
        self.borderRadius = borderRadius
        self.buttonRect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.image_path = image_path
        self.clickFunction = lambda: print('') 

        self.font = pygame.font.Font("Fonts/OpenSans-Regular.ttf", 24)
        self.textObject = self.font.render(self.text, True, (255,255,255))
        self.buttonSurface = pygame.Surface(( self.buttonRect.width, self.buttonRect.height ), pygame.SRCALPHA)
        self.hovered = 0

        if (contentPosition==None):
            self.contentPosition = (self.buttonSurface.get_width() / 2 - self.textObject.get_width() / 2, self.buttonSurface.get_height() / 2 - self.textObject.get_height() / 2)


        if (hover == True): 
            self.hoverBg = hoverBg

        Button.buttons.append(self)

    
    def setPosition(self, pos):
        self.position = pos

    def draw(self):
        self.buttonRect = pygame.draw.rect(self.buttonSurface, self.color, (0,0,self.buttonSurface.get_width(), self.buttonSurface.get_height()), 
                         width=0, border_radius=self.borderRadius)

        self.buttonRect.x = self.position[0]
        self.buttonRect.y = self.position[1]

        if (self.image_path == None): 
            self.buttonSurface.blit(self.textObject, self.contentPosition)
        else:
            self.buttonImg = pygame.image.load(self.image_path)
            # self.buttonImg.fill('blue')
            self.buttonImg = pygame.transform.scale(self.buttonImg, self.size)
            self.buttonSurface.blit(self.buttonImg, (0,0)) 

        self.screen.blit(self.buttonSurface, (self.position[0], self.position[1]))


    def getSize(self):
        return [self.buttonSurface.get_width(), self.buttonSurface.get_height()]
    
    def getText(self): 
        return self.text



    def getPosition(self):
        return self.position

    def getSurface(self):
        return self.buttonSurface

    def getRect(self):
        return self.buttonRect

    def onClick(self, function, *args): 
        self.clickFunction = lambda: function(*args)

    def getClickFunction(self): 
        return self.clickFunction


    def clicked(self, event, rect=None, checkFullRect=False):
        self.buttonMask = pygame.mask.from_surface(self.buttonSurface)

        if (rect != None):
            self.buttonClickRect = rect
        else:
            self.buttonClickRect = self.buttonRect



        if (self.buttonClickRect.collidepoint(event.pos)):
            if (checkFullRect == True):
                pos = (event.pos[0]-self.buttonClickRect.x,event.pos[1]-self.buttonClickRect.y)
                if (self.buttonMask.get_at(pos) == 1):
                    return self.clickFunction()
            return self.clickFunction()

    def hover(self):
        self.color = 'gray'
