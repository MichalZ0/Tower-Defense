from pygments.styles.dracula import background

from creatures import *
from defenders import *
from Components.SidePanel import SidePanel
from Components.BottomPanel import BottomPanel
import os
from waves import Waves


class Game:
    def __init__(self, screen, sf, difficulty="easy", level='Greenfield'):
        pygame.init()
        if difficulty == "easy":
            self.health = 100
            self.max_waves = 30
            self.money = 1500
        elif difficulty == "challenging":
            self.health = 75
            self.max_waves = 40
            self.money = 1200
        elif difficulty == "nightmare":
            self.health = 50
            self.max_waves=45
            self.money=1000
        self.side_panel_width = 150
        self.bottom_panel_height = 130
        self.difficulty=difficulty
        self.level=level
        self.side_panel = SidePanel(
            screen,
            screen.get_width(),
            screen.get_height(),
            sf,
            health=self.health,
            money=self.money,
            width_size=self.side_panel_width,
            bottom_panel_height=self.bottom_panel_height,
            game_size=(
                screen.get_width() - self.side_panel_width,
                screen.get_height() - self.bottom_panel_height,
            ),
        )
        self.bottom_panel = BottomPanel(
            screen,
            sf,
            screen.get_width() - self.side_panel_width,
            self.bottom_panel_height,
        )
        self.vol=0
        self.screen = screen
        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        self.bgPath = os.path.join(os.getcwd(), "assets", "background.png")

        if (level == 'Greenfield'):
            self.background = pygame.image.load("assets/map/background.png")
            self.windmill = pygame.transform.scale(
                pygame.image.load("assets/map/blacksmith.png"), (250 * sf, 250 * sf)
            )
            self.windmill = pygame.transform.flip(self.windmill, True, False)

        if (level == 'Desert'): 
            self.background = pygame.image.load("assets/map/map_desert.png")

        if (level == 'Cave'): 
            self.background = pygame.image.load("assets/map/map_cave.png")


        self.heart = pygame.transform.scale(
            pygame.image.load("assets/miscelanneous/heart.png"), (350, 350)
        )
        self.sf = sf  # Wspolczynnik wielkosci ekranu wzgledem bazowej rozdzielczosci (800x600)
        #print("Sf", self.sf)
        self.background = pygame.transform.scale(
            self.background,
            (800 * self.sf - self.side_panel.width_size * sf, 600 * self.sf),
        )
        # Inicjalizacja grupy potworów
        self.monsters = pygame.sprite.Group()
        self.current_wave = 1
        self.waves = Waves(self.sf, self.screen, difficulty=difficulty, mapName=level,max_waves=self.max_waves)

        # DO MAPY 1
        # self.waypoints = [(580/8*self.sf, 3100/6*self.sf), (580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 1275/6*self.sf), (4500/8*self.sf, 1275/6*self.sf)]

        """
        self.waypoints2 = []
        for i in range(len(self.waypoints) - 1):
            x1, y1 = self.waypoints[i]
            x2, y2 = self.waypoints[i+1]
            middle_x = (x1 + x2) / 2
            middle_y = (y1 + y2) / 2
            self.waypoints2.append((middle_x, middle_y))
        """

        self.tower = None
        self.tower_group = pygame.sprite.Group()
        self.tower_image_path = os.path.join(os.getcwd(), "assets", "towers")

        self.towers = []

    def start_wave(self):
        self.waves.create_wave()
        self.monsters = self.waves.getMonsters()


    def get_color_at_mouse_click(self, event):
        mouse_x, mouse_y = event
        if (mouse_x > 0 and mouse_x < self.background.get_width() and
            mouse_y > 0 and mouse_y < self.background.get_height()): 

            #print("ev in collision", mouse_x, mouse_y)

            # Sprawdzanie koloru piksela w tym miejscu
            color = self.background.get_at((mouse_x, mouse_y))
            # print(f"Kolor w miejscu kliknięcia: {color}")
            R, G, B, A = color  # Przypisanie wartości składowych koloru
            brightness = 0.2126 * R + 0.7152 * G + 0.0722 * B  # Obliczanie jasności

            for t in self.towers:
                if t.rectWithoutRadius.collidepoint(event):
                    return False

            # Jeśli jasność jest powyżej pewnego progu (np. 128), uznajemy kolor za jasny
            #print(brightness)
            return brightness > 128

    def take_damage(self, damage):
        self.health -= damage
        self.side_panel.health -= damage
        if self.health < 1:
            self.waves.wave_running = False
            self.waves.lose()

    def get_robbed(self):  # zlodziej bedzie to uruchamial xd
        self.money -= 100
        self.side_panel.money -= 100

    def run(self):
        self.Is = 0
        running = True
        while running:
            # print(self.towers)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return [False, None]

                # Obsługa panelu bocznego
                if self.side_panel.handle_event(event, self.tower_group):
                    if (
                        not self.waves.wave_running
                        and not self.waves.won
                        and not self.waves.lost
                    ):
                        #print("Fala rozpoczęta")
                        self.start_wave()

                if self.side_panel.handleTowerSelection(
                    event,
                    self.tower_group,
                    self.get_color_at_mouse_click,
                    self.bottom_panel.drawSelectedTowerInfo,
                    self.bottom_panel.clearPanel
                ):

                    TOWER=self.side_panel.getTower(self.money)
                    if TOWER != None:
                        self.towers.insert(0,TOWER)



                    self.money=self.side_panel.pay()
                    self.side_panel.money=self.money
                    for i in self.towers:
                        i.money = (self.money)
                        i.game=self
                    self.Is = 1
                    self.bottom_panel.clearPanel()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.waves.won == True or self.waves.lost==True):
                        self.bottom_panel.clearPanel()
                        for monster in self.monsters:
                            monster.kill()
                        for tower in self.towers:
                            tower.kill()
                        if (self.waves.restartButton.clicked(event)):
                            self.__init__(self.screen, self.sf,self.difficulty, self.level)
                        elif (self.waves.menuButton.clicked(event)):
                            return [True, 0] 
                
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return [True, 0]

                if (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_1
                ):  # Lewy przycisk myszy
                    mouse_position = pygame.mouse.get_pos()  # Pobierz współrzędne myszy
                    #print(mouse_position)
                    self.tower = Cannon(
                        position=mouse_position,
                        image_path=self.tower_image_path,
                        range=100,
                        damage=100,
                        animation_speed=100,
                        name="Cannon",
                        updateSidePanel=self.bottom_panel.drawSelectedTowerInfo,
                    )

                    if len(self.towers) == 1:
                        self.towers[0].hideRadius()


                    self.towers.insert(0, self.tower)

                    if self.get_color_at_mouse_click(mouse_position):
                        self.tower_group.add(self.tower)
                        self.Is = 1

                        # ??????????????????????????????
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Prawy przycisk myszy
                #
                #     for tower in self.towers:
                #         if tower.getRect().collidepoint(event.pos):  # Sprawdzenie, czy kliknięto na wieżę
                #             clicked_pos = (event.pos[0] - tower.getRect().x, event.pos[1] - tower.getRect().y)
                #             if tower.getMask().get_at(clicked_pos) == 1:
                #                 print("tak")
                #                 # Przekazanie obiektu wieży do funkcji upgrade innej klasy
                #
                #                 self.bottom_panel.clearPanel()
                #                 self.bottom_panel.drawSelectedTowerInfo(tower)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        event.button == 1
                    ):  # Lewy przycisk myszy (kliknięcie na przyciski ulepszeń)
                        mouse_pos = pygame.mouse.get_pos()
                        self.bottom_panel.handle_event(event, mouse_pos)
                        #self.bottom_panel.drawSelectedTowerInfo()
                        #self.bottom_panel.clearPanel()

                        self.soldTowerReturn = self.bottom_panel.handle_sell(event, self.towers, self.tower_group)
                        if self.soldTowerReturn:
                            self.money += round(self.soldTowerReturn)
                            self.side_panel.money = round(self.money)


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        event.pos[0] < self.width - self.side_panel_width
                        and event.pos[1] < self.height - self.bottom_panel_height
                    ):
                        clicked = False
                        for tower in self.towers:
                            #print(tower.rectWithoutRadius)
                            if tower.rect.collidepoint(event.pos):
                                #print(tower.rectWithoutRadius)
                                #print("detected click ")
                                self.clickPos = (
                                    event.pos[0] - tower.rect.x,
                                    event.pos[1] - tower.rect.y,
                                )
                                if (
                                    tower.getMask().get_at(self.clickPos) == 1
                                    and clicked == False
                                ):
                                    tower.showRadius()
                                    self.bottom_panel.drawSelectedTowerInfo(tower)
                                    clicked = True
                                    #self.bottom_panel.clearPanel()
                                else:
                                    tower.hideRadius()
                                    self.bottom_panel.clearPanel()

                            else:
                                tower.hideRadius()

                        if clicked == False:
                            self.bottom_panel.clearPanel()

            self.draw()

            for monster in self.waves.monsters:
                if monster.reached_end:
                    self.take_damage(monster.damage)
                    if monster.name == "Thief":
                        self.get_robbed()
                    monster.kill()
                if monster.health <= 0:
                    self.money+= monster.reward
                    monster.kill()
                monster.draw_health_bar(self.screen, monster.image_size)

            for i in self.towers:
                #self.money=i.pay()
                if i.generated_income:
                    # print(i.income)
                    self.money += i.income
                    self.side_panel.money += i.income

            # print(self.waves.won, self.waves.lost)
            pygame.display.flip()


    def draw(self):
        #print(self.money)
        self.side_panel.money=self.money
        self.screen.blit(self.background, (0, 0))
        self.tower_group.draw(self.screen)
        # Rysowanie linii łączących waypoints
        # self.screen.blit(self.windmill, (-10 * self.sf, -150 * self.sf))
        self.monsters.update()  # Aktualizuje wszystkie potwory w grupie

        self.waves.update()

        self.side_panel.draw(
            self.waves.wave_num,
            self.max_waves,
            self.waves.wave_running,
            self.waves.won,
            self.waves.lost,
        )
        # self.waves.draw_loss()
        if self.bottom_panel.working == 0:
            self.bottom_panel.clearPanel()

        if self.bottom_panel.working == 1:
            self.bottom_panel.draw()
        if self.Is == 1:
            for tower in self.towers:
                tower.update(self.monsters, self.money,self.vol)

                bullets = tower.getBullets()
                for i in range(0, len(bullets)):
                    self.screen.blit(bullets[i].getSprite(), bullets[i].getPosition())
                    bullets[i].update()
                    if bullets[i].checkCollision():
                        bullets.pop(i)
