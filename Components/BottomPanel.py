import pygame
import os

from Components.TextModule import *
from Components.ButtonModule import *

class BottomPanel():
    selectedTower = None
    def __init__(self, screen, sf, width, height):
        self.screen = screen
        self.sf = sf

        self.screenSize = (self.screen.get_width(), self.screen.get_height())
        self.panelRect = pygame.Rect(0,
                                     self.screenSize[1] - height, 
                                     width, 
                                     height)


        self.panelBg = pygame.image.load(os.path.join(os.getcwd(), "wood_texture.jpeg"))
        self.panelBg = pygame.transform.scale(self.panelBg, (self.screenSize[0] - width, self.screenSize[0] - width))

        self.clearPanelSurface = pygame.Surface((self.panelRect.width, self.panelRect.height))

        i = 1
        currentBgBlitPos = [ self.panelRect.width - (i * (self. screenSize[0] - width)), 0 ]

        while True:
            self.clearPanelSurface.blit(self.panelBg, currentBgBlitPos)
            if (currentBgBlitPos[0] <= 0):
                break
            i += 1
            currentBgBlitPos = [ self.panelRect.width - (i * (self. screenSize[0] - width)), 0 ]


        self.currentSurface = self.clearPanelSurface.copy()


    def draw(self):
        self.screen.blit(self.currentSurface, self.panelRect)


    def drawSelectedTowerInfo(self, tower):
        self.towerName = Text(self.currentSurface, (0,0), tower.name, size=42)
        self.towerName.draw()

        self.towerImage = tower.frames[0]
        self.towerImageRect = self.towerImage.get_rect()

        self.currentSurface.blit(self.towerImage, (0,30)) 

        attackSpeedInSeconds = str(int(tower.attack_interval) / 1000) + '/s'

        self.attackSpeed = Text(self.currentSurface, 
                                (100,30), 
                                f"ATAK:  {attackSpeedInSeconds}", 
                                size=30) 
        self.attackSpeed.draw()

        self.damage = Text(self.currentSurface, 
                                (100,30 + self.attackSpeed.getPosition()[1]), 
                                f"OBR:  {tower.damage}", 
                                size=30) 
        self.damage.draw()


        self.sell = Button(self.currentSurface, (110, 35), (0,self.panelRect.height - 35), "red", "SPRZEDAJ", textSize=18)
        self.sell.draw()


        self.firstUpgradeName = 'Ulepszenie 1'
        self.secondUpgradeName = 'Ulepszenie 2'

        self.upgrade1 = upgradeButton(self.currentSurface, (120, 100), (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40, 
                                self.panelRect.height/2 - 100/2), 
                                "blue", text='', upgradeTitle=self.firstUpgradeName, image_path=os.path.join(os.getcwd(), 'assets', 'upgrades', 'upgrade1.png'), upgradeCost='100')
        #
        self.upgrade2 = upgradeButton(self.currentSurface, (120, 100), (self.upgrade1.getPosition()[0] + self.upgrade1.getSize()[0] + 30, 
                                                                        self.upgrade1.getPosition()[1]), 
        "green", text='', upgradeTitle=self.secondUpgradeName, image_path=os.path.join(os.getcwd(), 'assets', 'upgrades', 'upgrade1.png'), upgradeCost='300')

        self.upgrade1.draw()
        self.upgrade2.draw()






    def clearPanel(self): 
        self.currentSurface.blit(self.clearPanelSurface, (0,0))

        
