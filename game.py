from creatures import *
from defenders import *
from Components.SidePanel import SidePanel
from Components.BottomPanel import BottomPanel
import os
from waves import Waves


class Game:
    def __init__(self, screen, sf, difficulty='easy'):
        pygame.init()
        if difficulty == 'easy':
            self.health = 200
            self.max_waves = 50
            self.money = 1000
        elif difficulty == 'challenging':
            pass
        elif difficulty == 'nightmare':
            pass
        self.side_panel_width = 150
        self.bottom_panel_height = 130

        self.side_panel = SidePanel(screen, screen.get_width(), screen.get_height(), sf, health=self.health, money=self.money, width_size=self.side_panel_width)
        self.bottom_panel = BottomPanel(screen, sf, screen.get_width() - self.side_panel_width, self.bottom_panel_height)

        self.screen = screen
        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        self.bgPath = os.path.join(os.getcwd(), 'assets', 'background.png')
        self.background = pygame.image.load(self.bgPath)
        self.windmill = pygame.transform.scale(pygame.image.load("assets/map/blacksmith.png"), (250*sf, 250*sf))
        self.windmill = pygame.transform.flip(self.windmill, True, False)
        self.heart = pygame.transform.scale(pygame.image.load("assets/miscelanneous/heart.png"), (350, 350))
        self.sf = sf # Wspolczynnik wielkosci ekranu wzgledem bazowej rozdzielczosci (800x600)
        print("Sf", self.sf)
        self.background = pygame.transform.scale(self.background, (800*self.sf-self.side_panel.width_size*sf, 600*self.sf))
        # Inicjalizacja grupy potworów
        self.monsters = pygame.sprite.Group()
        self.current_wave = 1
        self.waves = Waves(self.sf, self.screen)


        self.waypoints = [(580/8*self.sf, 3100/6*self.sf), (580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 1275/6*self.sf), (4500/8*self.sf, 1275/6*self.sf)]

        '''
        self.waypoints2 = []
        for i in range(len(self.waypoints) - 1):
            x1, y1 = self.waypoints[i]
            x2, y2 = self.waypoints[i+1]
            middle_x = (x1 + x2) / 2
            middle_y = (y1 + y2) / 2
            self.waypoints2.append((middle_x, middle_y))
        '''

        self.tower = None
        self.tower_group = pygame.sprite.Group()
        self.tower_image_path = os.path.join(os.getcwd(), 'assets', 'towers')

        self.towers = []

    def start_wave(self):
        self.waves.create_wave()
        self.monsters = self.waves.getMonsters()

    def get_color_at_mouse_click(self, event):
        mouse_x, mouse_y = event
        print(mouse_x, mouse_y)

        # Sprawdzanie koloru piksela w tym miejscu
        color = self.screen.get_at((mouse_x, mouse_y))
        #print(f"Kolor w miejscu kliknięcia: {color}")
        R, G, B, A = color  # Przypisanie wartości składowych koloru
        brightness = 0.2126 * R + 0.7152 * G + 0.0722 * B  # Obliczanie jasności

        # Jeśli jasność jest powyżej pewnego progu (np. 128), uznajemy kolor za jasny
        print(brightness)
        return brightness > 128

    def take_damage(self, damage):
        self.health -= damage
        self.side_panel.health -= damage
        if self.health < 1:
            self.waves.wave_running = False
            self.waves.lose()


    def get_robbed(self): #zlodziej bedzie to uruchamial xd
        self.money -= 100
        self.side_panel.money -= 100

    def run(self):
        self.Is=0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return [False, None]

                # Obsługa panelu bocznego
                if self.side_panel.handle_event(event, self.tower_group):
                    if not self.waves.wave_running and not self.waves.won and not self.waves.lost:
                        print("Fala rozpoczęta")
                        self.start_wave()

                if self.side_panel.handleTowerSelection(event, self.tower_group): 
                    self.towers.insert(0, self.side_panel.getTower()) 
                    self.Is = 1


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return [True, 0]

                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:  # Lewy przycisk myszy
                    mouse_position = pygame.mouse.get_pos()  # Pobierz współrzędne myszy
                    print(mouse_position)
                    self.tower = Cannon(position=mouse_position, image_path=self.tower_image_path,range=100,damage=100,animation_speed=100, name="Cannon", updateSidePanel=self.bottom_panel.drawSelectedTowerInfo)
                    if (len(self.towers) == 1): 
                        self.towers[0].hideRadius()

                    self.towers.insert(0, self.tower)

                    if self.get_color_at_mouse_click(mouse_position):
                        self.tower_group.add(self.tower)
                        self.Is=1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] < self.width - self.side_panel_width): 
                        clicked = False
                        for tower in self.towers:
                            if tower.getRect().collidepoint(event.pos): 
                                self.clickPos = (event.pos[0] - tower.getRect().x,  event.pos[1] - tower.getRect().y)
                                if (tower.getMask().get_at(self.clickPos) == 1 and clicked == False ):  
                                    tower.showRadius()
                                    # self.bottom_panel.drawSelectedTowerInfo(tower)
                                    clicked = True 
                                else:
                                    tower.hideRadius()
                                    # self.bottom_panel.clearPanel()

                            else:
                                tower.hideRadius()

                        # if (clicked == False):
                        #     self.bottom_panel.clearPanel()


            self.draw()

            for monster in self.waves.monsters:
                if monster.reached_end:
                    self.take_damage(monster.damage)
                    if monster.name == "Thief":
                        self.get_robbed()
                    monster.kill()
                monster.draw_health_bar(self.screen, monster.image_size)

            pygame.display.flip()

    def draw(self):

        self.screen.blit(self.background, (0, 0))
        self.tower_group.draw(self.screen)
        # Rysowanie linii łączących waypoints
        # if len(self.waypoints) > 1:
        #     pygame.draw.lines(self.screen, (0, 255, 0), False, self.waypoints2, 3)  # Zielona linia o grubości 3 pikseli
        self.screen.blit(self.windmill, (-10 * self.sf, -150 * self.sf))
        self.monsters.update()  # Aktualizuje wszystkie potwory w grupie

        if self.Is ==1:
            for tower in self.towers:
                tower.update(self.monsters)

                bullets = tower.getBullets()
                for i in range(0, len(bullets)): 
                    self.screen.blit(bullets[i].getSprite(), bullets[i].getPosition())
                    bullets[i].update()
                    if (bullets[i].checkCollision()):
                        bullets.pop(i)


        
        self.waves.update()


        self.side_panel.draw(self.waves.wave_num, self.max_waves, self.waves.wave_running, self.waves.won, self.waves.lost)
        self.bottom_panel.draw()


