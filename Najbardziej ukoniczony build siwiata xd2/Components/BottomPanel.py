import pygame
import os

from Components.TextModule import *
from Components.ButtonModule import *

class BottomPanel():
    selectedTower = None
    def __init__(self, screen, sf, width, height):
        self.screen = screen
        self.sf = sf
        self.Tower=None
        self.screenSize = (self.screen.get_width(), self.screen.get_height())
        self.panelRect = pygame.Rect(0,
                                     self.screenSize[1] - height, 
                                     width, 
                                     height)


        self.panelBg = pygame.image.load(os.path.join(os.getcwd(), "wood_texture.jpeg"))
        self.panelBg = pygame.transform.scale(self.panelBg, (self.screenSize[0] - width, self.screenSize[0] - width))
        self.Is=0
        self.Is2=0
        self.clearPanelSurface = pygame.Surface((self.panelRect.width, self.panelRect.height))
        self.drawn = False
        self.working=0
        self.price=0

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
        self.Is2=0
        print(tower.name)
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
        self.sell.onClick(self.sellFunction, tower)

        self.sell.draw()


        self.firstUpgradeName = 'Ulepszenie 1'
        self.secondUpgradeName = 'Ulepszenie 2'

        if tower.name == "Cannon":
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100), (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                self.panelRect.height/2 - 100/2),
                                "blue", text='', upgradeTitle=self.firstUpgradeName, image_path=os.path.join(os.getcwd(), 'assets', 'towers','Mortar', 'Mortar0.png'), upgradeCost='100', upgradedTower=tower)
        #
            self.upgrade2 = upgradeButton(self.currentSurface, (120, 100), (self.upgrade1.getPosition()[0] + self.upgrade1.getSize()[0] + 30,
                                                                        self.upgrade1.getPosition()[1]),"green", text='', upgradeTitle=self.secondUpgradeName, image_path=os.path.join(os.getcwd(), 'assets', 'upgrades', 'upgrade1.png'), upgradeCost='300')


            self.Is=1
            self.Tower=tower
            if self.Tower.max==0:
                self.upgrade1.draw()
                self.price=self.Tower.upPrice1
            #self.upgrade2.draw()
            self.working=1

        if tower.name == "MageTower":
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100),
                                              (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                               self.panelRect.height / 2 - 100 / 2),
                                              "blue", text='', upgradeTitle=self.firstUpgradeName,
                                              image_path=os.path.join(os.getcwd(), 'assets', 'towers', 'MageTower2.0',
                                                                      'MageTower0.png'), upgradeCost='100', upgradedTower=tower, upgradeRoute=0)
                #
            if tower.level2==0:
                self.upgrade2 = upgradeButton(self.currentSurface, (120, 100),
                                                  (self.upgrade1.getPosition()[0] + self.upgrade1.getSize()[0] + 30,
                                                   self.upgrade1.getPosition()[1]),
                                                  "green", text='', upgradeTitle=self.secondUpgradeName,
                                                  image_path=os.path.join(os.getcwd(), 'assets', 'towers','MageTower1.1',
                                                                          'MageTower0.png'), upgradeCost='300', upgradedTower=tower, upgradeRoute=1)
                self.Is2=1

            self.Is = 1
            self.Tower = tower
            if self.Tower.max == 0:
                self.upgrade1.draw()
            if tower.level2==0:
                self.upgrade2.draw()

            self.working=1


        if tower.name == "Archer":
            print("przycisk")
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100),
                                          (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                           self.panelRect.height / 2 - 100 / 2),
                                          "blue", text='', upgradeTitle=self.firstUpgradeName,
                                          image_path=os.path.join(os.getcwd(), 'assets', 'towers', 'Archer2',
                                                                  'Archer0.png'), upgradeCost='100', upgradedTower=tower)


            self.Is = 1
            self.Tower = tower
            if self.Tower.max==0:
                self.upgrade1.draw()

            self.working=1


        if tower.name == "Temple":
            #print("przycisk")
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100),
                                          (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                           self.panelRect.height / 2 - 100 / 2),
                                          "blue", text='', upgradeTitle=self.firstUpgradeName,
                                          image_path=os.path.join(os.getcwd(), 'assets', 'towers', 'Temple2',
                                                                  'Temple0.png'), upgradeCost='100', upgradedTower=tower)


            self.Is = 1
            self.Tower = tower
            if self.Tower.max ==0:
                self.upgrade1.draw()

            self.working=1

        if tower.name == "Witchhouse":
            #print("przycisk")
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100),
                                          (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                           self.panelRect.height / 2 - 100 / 2),
                                          "blue", text='', upgradeTitle=self.firstUpgradeName,
                                          image_path=os.path.join(os.getcwd(), 'assets', 'towers', 'Witchhouse',
                                                                  'Witchhouse0.png'), upgradeCost='100', upgradedTower=tower)
            self.Is = 1
            self.Tower = tower
            if self.Tower.max==0:
                self.upgrade1.draw()

            self.working=1
        if tower.name == "Factory":
                # print("przycisk")
            self.upgrade1 = upgradeButton(self.currentSurface, (120, 100),
                                              (self.attackSpeed.getPosition()[0] + self.attackSpeed.getSize()[0] + 40,
                                               self.panelRect.height / 2 - 100 / 2),
                                              "blue", text='', upgradeTitle=self.firstUpgradeName,
                                              image_path=os.path.join(os.getcwd(), 'assets', 'towers', 'Factory',
                                                                      'Factory1.png'), upgradeCost='100', upgradedTower=tower)


            self.Is = 1
            self.Tower = tower
            if self.Tower.max==0:
                self.upgrade1.draw()

            self.working=1


        self.drawn = True


    
    def sellFunction(self, tower): 
        return tower

    def clearPanel(self): 
        self.Tower=None
        self.drawn = False
        self.currentSurface.blit(self.clearPanelSurface, (0,0))
        self.working=0

    # def handle_event(self,event,mouse_pos):
        # """Obsługuje kliknięcia na przyciskach w panelu, w tym ulepszanie wieży."""
        # if self.Is:
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Sprawdzamy, czy kliknięto lewym przyciskiem myszy
        #         #print("rect",self.upgrade1.getRect())
        #         #print("pozycja",self.upgrade1.position)
        #         if self.upgrade1.clicked(event):
        #             print('dziala')
        #
        #             self.Tower.upgrade()
        #
        #             self.clearPanel()
        #         if self.Is2==1:
        #             if self.upgrade2.clicked(event):
        #                 self.Tower.upgrade2()
        #
        #                 self.Tower.upgrade()
        #                 self.clearPanel()



    def handle_event(self,event, mouse_pos):
        """Obsługuje kliknięcia na przyciskach w panelu, w tym ulepszanie wieży."""
        if (event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] > self.panelRect.y): 
            if self.Is:
                self.upgrade1ClickRect = self.upgrade1.getRect().copy()
                self.upgrade1ClickRect.y += self.screenSize[1] - self.panelRect.height
                self.upgrade1.clicked(event, self.upgrade1ClickRect)
                #self.clearPanel()
            if self.Is2: 
                self.upgrade2ClickRect = self.upgrade2.getRect().copy()
                self.upgrade2ClickRect.y += self.screenSize[1] - self.panelRect.height

                self.upgrade2.clicked(event, self.upgrade2ClickRect)

            if self.upgrade1.used == 1:
                self.clearPanel()




            if self.Is2:
                if self.upgrade2.used ==1:
                    self.clearPanel()






    def handle_sell(self, event, towers, sprites):
        if (self.drawn == True): 
            print('truerfdehdhrt')
            sellClickPos = self.sell.getRect().copy()
            sellClickPos.y += self.panelRect.y

            towerToSell = self.sell.clicked(event, sellClickPos)
            if towerToSell:
                sprites.remove(towerToSell)
                towers.remove(towerToSell)

                self.clearPanel()
                #Zwracamy 90% poczatkowej kwoty
                return towerToSell.price * 0.9


                








        
