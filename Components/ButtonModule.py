from os import walk
import pygame
import math
from os import getcwd, path

from Components import TextModule 


def isHovered(event): 
    # for button in Button.buttons:
    #     if (button.buttonRect.collidepoint(event.pos)):
    #         button.hover()
    #     else:
    #         button.color = 'blue'
        
    pass

class Button:
    buttons = []
    def __init__(self, screen, size, position, color, text, padding=30, contentPosition=None, borderRadius=0, hover=False, hoverBg = None, image_path=None, textSize = 24):
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

        self.font = pygame.font.Font("Fonts/Pixeltype.ttf", textSize)
        self.textObject = self.font.render(self.text, True, (255,255,255))
        self.buttonSurface = pygame.Surface(( self.buttonRect.width, self.buttonRect.height ), pygame.SRCALPHA)
        self.hovered = 0

        self.contentPosition = contentPosition
        if (self.contentPosition==None):
            self.contentPosition = [ self.buttonSurface.get_width() / 2 - self.textObject.get_width() / 2, self.buttonSurface.get_height() / 2 - self.textObject.get_height() / 2 ]


        if (hover == True): 
            self.hoverBg = hoverBg
            Button.buttons.append(self)

        self.buttonRect = pygame.draw.rect(self.buttonSurface, self.color, (0,0,self.buttonSurface.get_width(), self.buttonSurface.get_height()), 
                         width=0, border_radius=self.borderRadius)

    
    def setPosition(self, pos):
        self.position = pos

    def draw(self):
        self.buttonRect.x = self.position[0]
        self.buttonRect.y = self.position[1]

        if (self.image_path == None): 
            self.buttonSurface.blit(self.textObject, self.contentPosition)
        else:
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


class upgradeButton(Button):
    def __init__(self, screen, size, position, color, text, image_path, upgradeTitle, upgradeCost):
        Button.__init__(self, screen, size, position, color, text)
        self.image_path = image_path


        self.upgradeTitle = upgradeTitle
        self.upgradeCost = upgradeCost

        self.textSize = 18
        self.font = pygame.font.Font("Fonts/OpenSans-Regular.ttf", self.textSize)

        self.upgradeTitle = self.font.render(self.upgradeTitle, True, (255,255,255))
        self.upgradeCost = self.font.render(self.upgradeCost, True, (255,255,255))

        self.upgradeImage = pygame.image.load(image_path)
        self.upgradeImage = pygame.transform.scale(self.upgradeImage, (40, 40))
    
    def draw(self):
        self.buttonRect = pygame.draw.rect(self.buttonSurface, self.color, (0,0,self.buttonSurface.get_width(), self.buttonSurface.get_height()), 
                         width=0, border_radius=self.borderRadius)

        self.buttonRect.x = self.position[0]
        self.buttonRect.y = self.position[1]

        self.buttonSurface.blit(self.upgradeTitle, (self.buttonRect.width/2 - self.upgradeTitle.get_width()/2, 0))
        self.buttonSurface.blit(self.upgradeCost, (self.buttonRect.width/2 - self.upgradeCost.get_rect().width/2, self.buttonRect.height-self.upgradeCost.get_height()))

        
        self.buttonSurface.blit(self.upgradeImage, (self.buttonRect.width/2 - self.upgradeImage.get_rect().width/2, 
                                                    (self.upgradeTitle.get_height() + (self.buttonRect.height - self.upgradeTitle.get_height() - self.upgradeCost.get_height())/2  - self.upgradeImage.get_height()/2) 
                                                    ))

        self.screen.blit(self.buttonSurface, (self.position[0], self.position[1]))

    
class difficultyButton(Button): 
    def __init__(self, screen):
        super().__init__(screen, (600, 100), (0,0), "blue", "EASY", textSize=60)
    
        self.diffIcon = pygame.image.load(path.join(getcwd(), "creatures", "dragon.png"))
        self.diffIcon = pygame.transform.scale(self.diffIcon, (100, 100))

        self.contentPosition = (self.diffIcon.get_width() + (((self.size[0] - self.diffIcon.get_width())/2) - self.textObject.get_width()/2),
                                0)

        self.desc = TextModule.Text(self.buttonSurface, (0,self.textObject.get_height()), "PODSTAWOWY TRYB GRY", size=24)
        self.descRect = pygame.Rect(self.diffIcon.get_width() + (((self.size[0] - self.diffIcon.get_width())/2) - self.desc.getSize()[0]/2), 
                                    self.contentPosition[1] + self.textObject.get_height(),
                                    self.desc.getSize()[0],
                                    self.desc.getSize()[1])

        self.desc.setPosition((self.descRect.x, self.descRect.y))

        self.heartIcon = pygame.image.load(path.join(getcwd(), "assets", "miscelanneous", "heart_trim.png"))
        self.heartIcon = pygame.transform.scale(self.heartIcon, (30,30))
        self.heartIconRect = pygame.Rect(self.descRect.x, self.descRect.height + self.descRect.y, self.heartIcon.get_width(), self.heartIcon.get_height())

        self.heartsNumber = TextModule.Text(self.buttonSurface, (0,0), "100", 30) 
        self.heartsNumber.setPosition((self.heartIconRect.x + self.heartIconRect.width, self.heartIconRect.y + (self.heartIconRect.height/2)-(self.heartsNumber.getSize()[1]/2)))

        self.coinIcon = pygame.image.load(path.join(getcwd(), "assets", "miscelanneous", "coin_trim.png"))
        self.coinIcon = pygame.transform.scale(self.coinIcon, (30,30))
        self.coinIconRect = pygame.Rect(self.heartIconRect.x + self.heartIconRect.width + self.heartsNumber.getSize()[0] + 25, self.heartIconRect.y, self.coinIcon.get_width(), self.coinIcon.get_height())


        self.coinsNumber = TextModule.Text(self.buttonSurface, (0,0), "1000", 30)
        self.coinsNumber.setPosition((self.coinIconRect.x + self.coinIconRect.width, self.heartsNumber.getPosition()[1]))



                     

    def draw(self):
        super().draw()
        self.buttonSurface.blit(self.diffIcon, (0,0))
        self.desc.draw()

        self.buttonSurface.blit(self.heartIcon, (self.heartIconRect.x,self.heartIconRect.y))
        self.heartsNumber.draw()
        
        self.buttonSurface.blit(self.coinIcon, (self.coinIconRect.x, self.coinIconRect.y))
        self.coinsNumber.draw()

        self.screen.blit(self.buttonSurface, (0,0))


