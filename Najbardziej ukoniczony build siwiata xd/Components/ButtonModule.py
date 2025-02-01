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
        self.buttonRect.x = self.position[0]
        self.buttonRect.y = self.position[1]


    def draw(self):
        self.buttonRect.x = self.position[0]
        self.buttonRect.y = self.position[1]

        if (self.image_path == None): 
            self.buttonSurface.blit(self.textObject, self.contentPosition)
        else:
            self.buttonImg = pygame.image.load(self.image_path)
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
    def __init__(self, screen, size, position, color, text, image_path, upgradeTitle, upgradeCost, upgradedTower=None, upgradeRoute=0):
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
        self.used=0
        self.clickFunction = lambda: self.upgrade(upgradedTower, upgradeRoute)

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
    
       
    def upgrade(self, tower, upgradeRoute):
        #print('here he upgrade')
        if (upgradeRoute == 0): 

            tower.upgrade()
        else:
            if tower != None:
                tower.upgrade2()

        self.used=1
        




class difficultyButton(Button): 
    def __init__(self, screen, size, pos, color, icon, text, desc, health, coin, waves):
        super().__init__(screen, size, pos, color, "", textSize=0, borderRadius=25)

        self.iconNumberSpacing = 8 
        self.valueGap = 50
        self.header = TextModule.Text(None, (0,0), text, size=48)    

        self.diffIcon = pygame.transform.scale(icon, (75, 75))

        self.desc = TextModule.Text(None, (0,self.textObject.get_height()),desc, size=24)
        self.desc.setPosition((0, self.header.getPosition()[1] + self.header.getSize()[1]))
        #
        self.heartIcon = pygame.image.load(path.join(getcwd(), "assets", "miscelanneous", "heart_trim.png"))
        self.heartIcon = pygame.transform.scale(self.heartIcon, (30,30))
        self.heartIconRect = pygame.Rect(self.desc.getPosition()[0], self.desc.getPosition()[1] + self.desc.getSize()[1], self.heartIcon.get_width(), self.heartIcon.get_height())

        self.heartsNumber = TextModule.Text(None, (0,0), health, 30) 
        self.heartsNumber.setPosition((self.heartIconRect.x + self.heartIconRect.width + self.iconNumberSpacing, self.heartIconRect.y + (self.heartIconRect.height/2)-(self.heartsNumber.getSize()[1]/2)))
        #
        self.coinIcon = pygame.image.load(path.join(getcwd(), "assets", "miscelanneous", "coin_trim.png"))
        self.coinIcon = pygame.transform.scale(self.coinIcon, (30,30))
        self.coinIconRect = pygame.Rect(self.heartIconRect.x + self.heartIconRect.width + self.heartsNumber.getSize()[0] + self.valueGap, self.heartIconRect.y, self.coinIcon.get_width(), self.coinIcon.get_height())

        self.coinsNumber = TextModule.Text(None, (0,0), coin, 30)
        self.coinsNumber.setPosition((self.coinIconRect.x + self.coinIconRect.width + self.iconNumberSpacing, self.heartsNumber.getPosition()[1]))

        self.roundsIcon = pygame.image.load(path.join(getcwd(), "assets", "miscelanneous", "coin_trim.png")) 
        self.roundsIcon = pygame.transform.scale(self.roundsIcon, (30,30))
        self.roundsIconRect = pygame.Rect(self.coinIconRect.x + self.coinIconRect.width + self.coinsNumber.getSize()[0] + self.valueGap, self.heartIconRect.y, self.roundsIcon.get_width(), self.roundsIcon.get_height())
        #
        #
        self.roundsNumber = TextModule.Text(None, (0,0), waves, 30)
        self.roundsNumber.setPosition((self.roundsIconRect.x + self.roundsIconRect.width + self.iconNumberSpacing, self.heartsNumber.getPosition()[1]))
        #



        self.finalSize = (self.roundsNumber.getPosition()[0] + self.roundsNumber.getSize()[0] - self.heartIconRect.x, 
                          self.heartIconRect.y + self.heartIconRect.height - self.header.getPosition()[1]) 


        self.centerSurface = pygame.Surface(self.finalSize, pygame.SRCALPHA)

        self.header.setPosition((self.centerSurface.get_width()/2 - (self.header.getSize()[0]/2) , self.header.getPosition()[1]))
        self.desc.setPosition((self.centerSurface.get_width()/2 - (self.desc.getSize()[0]/2) , self.desc.getPosition()[1]))

        self.desc.screen = self.centerSurface
        self.header.screen = self.centerSurface
        self.coinsNumber.screen = self.centerSurface
        self.heartsNumber.screen = self.centerSurface
        self.roundsNumber.screen = self.centerSurface

        self.header.draw()
        self.desc.draw()

        self.centerSurface.blit(self.heartIcon, (self.heartIconRect.x,self.heartIconRect.y ))
        self.heartsNumber.draw()

        self.centerSurface.blit(self.coinIcon, (self.coinIconRect.x,self.coinIconRect.y ))
        self.coinsNumber.draw()

        self.centerSurface.blit(self.roundsIcon, (self.roundsIconRect.x,self.roundsIconRect.y ))
        self.roundsNumber.draw()

        self.diffIconPos = (self.size[0]/2 - ((self.diffIcon.get_width() + self.centerSurface.get_width())/2 + 30),
                            (self.size[1]/2) - (self.diffIcon.get_height()/2))
        


    def draw(self):
        # super().draw()
        self.buttonSurface.blit(self.diffIcon, self.diffIconPos)
        self.buttonSurface.blit(self.centerSurface, (self.diffIconPos[0] + self.diffIcon.get_width() + 30,
                                                     self.size[1]/2  - (self.centerSurface.get_height()/2)))
                                                     
        self.screen.blit(self.buttonSurface, self.position)


