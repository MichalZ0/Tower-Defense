import pygame
from Components.ButtonModule import *
from defenders import *
import os


class SidePanel:
    def __init__(self, screen, width, height, sf, health:int, money:int, width_size=150): 
        self.width_size = width_size
        self.screen = screen
        self.width = width
        self.height = height
        self.health = health
        self.money = money
        self.heart = pygame.transform.scale(pygame.image.load("assets/miscelanneous/heart.png"), (330*sf, 330*sf))
        self.coin = pygame.transform.scale(pygame.image.load("assets/miscelanneous/coin.png"), (305*sf, 305*sf))
        self.sf = sf
        self.color = (30, 30, 30)  # Kolor panelu
        self.pixel_font = pygame.font.Font("Fonts/Pixeltype.ttf",int(33*self.sf))
        #self.pixel_font.set_bold(True)
        self.button_color = (70, 130, 180)  # Kolor przycisku
        self.button_hover_color = (100, 160, 210)
        self.button_pressed_color = (50, 90, 130)
        self.button_rect = pygame.Rect(self.width - 134 * sf, self.height - 100 * sf, 120 * sf, 50 * sf)
        self.button_text = "Start Wave"
        self.button_text2 = "Running..."
        self.button_font = pygame.font.Font(None, int(24 * sf))
        self.button_pressed = False

        # Załadowanie obrazu do panelu
        self.panel_image = pygame.image.load("wood_texture.jpeg")
        self.panel_image = pygame.transform.scale(self.panel_image,
                                                  (self.width_size * self.sf, self.height))


        self.itemPath = os.path.join(os.getcwd(), "assets", "towers") 
        self.itemSize = (40, 40)
        
        self.towerCount = 10
        self.towerColumnCount = 3
        self.towerButtons = []
        self.itemGap = 5 

        self.towerPanelRect = pygame.Rect(
                self.width - width_size,
                300,
                self.towerColumnCount * self.itemSize[0] + (self.towerColumnCount + 1) * self.itemGap, 
                int(self.towerCount / self.towerColumnCount) * self.itemSize[0] + (self.towerColumnCount + 1) * self.itemGap, 
                )

        self.towerPanelRect.x += int(width_size / 2 - self.towerPanelRect.width / 2)


        self.towerPanel = pygame.Surface((self.towerPanelRect.width, self.towerPanelRect.height))
        self.towerPanel.fill("brown")


        for i in range(0, int(self.towerCount/self.towerColumnCount)):
            for j in range(0, self.towerColumnCount):
                self.item = Button(self.towerPanel, 
                                   self.itemSize, 
                                   (j * self.itemSize[0] + ((j+1) * self.itemGap), i * self.itemSize[1] + ((i +1) * self.itemGap)),
                                   'green', "Cannon", image_path=os.path.join(self.itemPath, 'Cannon', 'Cannon0.png'))

                self.item.onClick(self.placeItem)
                self.towerButtons.append(self.item)


        self.newTower = None
        self.towerImage = None
        self.towerClicked = False
        self.drawTowerPosition = [101,101]



    def draw(self, wave_num, max_waves, wave_running, won:bool, lost:bool):
        if not won and not lost:
            self.screen.blit(self.panel_image, (self.width - self.width_size * self.sf, 0))

            wave_text = f"{wave_num}/{max_waves}"
            wave_surface = self.pixel_font.render(wave_text, True, 'white')
            wave_rect = wave_surface.get_rect(center=(self.width - 141 * self.sf // 2, 20*self.sf))
            self.screen.blit(wave_surface, wave_rect)

            # Rysowanie przycisku
            button_color = self.button_color
            if self.button_pressed and not wave_running and not won:
                button_color = self.button_pressed_color
            elif self.button_rect.collidepoint(pygame.mouse.get_pos()) and not wave_running and not won:
                button_color = self.button_hover_color

            pygame.draw.rect(self.screen, button_color, self.button_rect, border_radius=10)
            self.screen.blit(self.heart, (469 * self.sf, -25 * self.sf))
            self.screen.blit(self.coin, (572 * self.sf, -55 * self.sf))
            self.screen.blit(self.pixel_font.render(str(self.money), True, 'white'), (722 * self.sf, 57 * self.sf))
            self.screen.blit(self.pixel_font.render(str(self.health), True, 'white'), (722 * self.sf, 109 * self.sf))

        # Dodawanie tekstu na przycisk
            if not wave_running:
                text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
            else:
                text_surface = self.button_font.render(self.button_text2, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.button_rect.center)
            self.screen.blit(text_surface, text_rect)

            self.drawTowerPanel()



    def placeItem(self):
        return True


    def drawTowerPanel(self):
        for towerIcon in self.towerButtons:
            towerIcon.draw()
            

        self.screen.blit(self.towerPanel, self.towerPanelRect)

        if self.towerImage != None:
            self.screen.blit(self.towerImage, self.drawTowerPosition)


    def handle_event(self, event, sprites):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                    self.button_pressed = True
                    return True  # Przycisnięcie wykryte
            elif event.type == pygame.MOUSEBUTTONUP:
                self.button_pressed = False
            return False

    def handleTowerSelection(self, event, sprites):
        towerMap = {'Cannon': Cannon,
                    'Temple': Cannon, 
                    'Archer': Cannon,
                    'Wizard': Cannon}

        print(self.drawTowerPosition)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] >= self.towerPanelRect.x and 
                event.pos[1] >= self.towerPanelRect.y):
            
                for towerButton in self.towerButtons:
                    clickRect = towerButton.getRect()
                    clickRect.x += self.width - self.width_size
                    clickRect.y += self.towerPanelRect.y

                    self.towerClicked = towerButton.clicked(event, clickRect, checkFullRect=True)
                    

                    if (self.towerClicked == True):
                        self.newTower = towerMap[towerButton.getText()](self.drawTowerPosition,
                                                                        self.itemPath,
                                                                        300,
                                                                        100,
                                                                        1)
                        break 

        if (event.type == pygame.MOUSEMOTION and self.towerClicked == True):


            if (event.pos[0] > 0 and
                event.pos[0] - self.newTower.getRect().width/2 > 0 and 
                event.pos[0] <= self.towerPanelRect.x): 

                sprites.add(self.newTower)
                
                self.drawTowerPosition = [event.pos[0], event.pos[1]]
                self.newTower.setPosition(event.pos)

                self.newTower.showRadius()
            

            elif (event.pos[0] > self.towerPanelRect.x):
                sprites.remove(self.newTower)

            if (event.buttons[0] == 0):
                self.towerClicked = False
                self.newTower.hideRadius()
                
                return True


    
    def getTower(self):
        if (self.newTower != None): 
            return self.newTower
        

