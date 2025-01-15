import pygame
from creatures import *
import math
import random


class Waves:
    def __init__(self, sf, screen, difficulty = 'easy'):
        self.screen = screen
        self.sf = sf
        self.wave_num = 1
        self.max_waves = 50
        self.wave_running = False
        self.won = False
        self.lost = False

        self.map_base_spawn_point = (670/8, 170/6) #dla mapy 3
        self.map_start_coefficient_x = -math.sqrt(2)
        self.map_start_coefficient_y = -math.sqrt(2) #tymczasowo (), bedzie zalezne od mapy zeby potwory sie spawnowaly bardziej w dol/gore/lewo/raczej nie prawo
        #DO MAPY 1

        #DO MAPY 1
        self.waypoints = [(580/8*self.sf, 3100/6*self.sf), (580/8*self.sf, 2070/6*self.sf),
                          (1580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 1270/6*self.sf),
                          (700/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 600/6*self.sf),
                          (2310/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 2440/6*self.sf),
                          (3720/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 1750/6*self.sf),
                          (3050/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 400/6*self.sf),
                          (3600/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 1275/6*self.sf),
                          (4500/8*self.sf, 1275/6*self.sf)]
        #DO MAPY 2
        self.waypoints = [(1980 / 8 * self.sf, 2680 / 6 * self.sf), (2180 / 8 * self.sf, 2580 / 6 * self.sf),
                          (2480 / 8 * self.sf, 2680 / 6 * self.sf), (3080 / 8 * self.sf, 3180 / 6 * self.sf),
                          (3380 / 8 * self.sf, 3220 / 6 * self.sf), (3730 / 8 * self.sf, 3220 / 6 * self.sf),
                          (4030 / 8 * self.sf, 3120 / 6 * self.sf), (4310 / 8 * self.sf, 2890 / 6 * self.sf),
                          (4510 / 8 * self.sf, 2690 / 6 * self.sf), (4685 / 8 * self.sf, 2390 / 6 * self.sf),
                          (4735 / 8 * self.sf, 2090 / 6 * self.sf), (4725 / 8 * self.sf, 1790 / 6 * self.sf),
                          (4700 / 8 * self.sf, 1490 / 6 * self.sf), (4620 / 8 * self.sf, 1190 / 6 * self.sf),
                          (4510 / 8 * self.sf, 990 / 6 * self.sf), (4110 / 8 * self.sf, 790 / 6 * self.sf),
                          (3950 / 8 * self.sf, 680 / 6 * self.sf), (3710 / 8 * self.sf, 680 / 6 * self.sf),
                          (3390 / 8 * self.sf, 780 / 6 * self.sf), (3210 / 8 * self.sf, 910 / 6 * self.sf),
                          (3110 / 8 * self.sf, 1110 / 6 * self.sf), (3150 / 8 * self.sf, 1410 / 6 * self.sf),
                          (3400 / 8 * self.sf, 1810 / 6 * self.sf), (3400 / 8 * self.sf, 1910 / 6 * self.sf),
                          (3200 / 8 * self.sf, 2110 / 6 * self.sf), (2800 / 8 * self.sf, 2260 / 6 * self.sf),
                          (2400 / 8 * self.sf, 2340 / 6 * self.sf), (2000 / 8 * self.sf, 2320 / 6 * self.sf),
                          (1700 / 8 * self.sf, 2220 / 6 * self.sf), (1500 / 8 * self.sf, 2000 / 6 * self.sf),
                          (1350 / 8 * self.sf, 1700 / 6 * self.sf), (1330 / 8 * self.sf, 1450 / 6 * self.sf),
                          (1530 / 8 * self.sf, 1250 / 6 * self.sf), (1860 / 8 * self.sf, 1080 / 6 * self.sf),
                          (1990 / 8 * self.sf, 1000 / 6 * self.sf), (2220 / 8 * self.sf, 880 / 6 * self.sf),
                          (2120 / 8 * self.sf, 765 / 6 * self.sf), (1960 / 8 * self.sf, 655 / 6 * self.sf),
                          (1660 / 8 * self.sf, 535 / 6 * self.sf), (1260 / 8 * self.sf, 445 / 6 * self.sf),
                          (1160 / 8 * self.sf, 445 / 6 * self.sf), (960 / 8 * self.sf, 495 / 6 * self.sf),
                          (790 / 8 * self.sf, 595 / 6 * self.sf), (600 / 8 * self.sf, 895 / 6 * self.sf),
                          (580 / 8 * self.sf, 1095 / 6 * self.sf), (730 / 8 * self.sf, 1485 / 6 * self.sf),
                          (730 / 8 * self.sf, 1535 / 6 * self.sf), (610 / 8 * self.sf, 1595 / 6 * self.sf),
                          (500 / 8 * self.sf, 1675 / 6 * self.sf), (400 / 8 * self.sf, 1695 / 6 * self.sf),
                          (350 / 8 * self.sf, 1695 / 6 * self.sf)
                          ]
        # DO MAPY 3
        self.waypoints = [(920 / 8 * self.sf, 420 / 6 * self.sf), (1235 / 8 * self.sf, 660 / 6 * self.sf),
                          (605 / 8 * self.sf, 1080 / 6 * self.sf), (605 / 8 * self.sf, 1280 / 6 * self.sf),
                          (1050 / 8 * self.sf, 1630 / 6 * self.sf), (700 / 8 * self.sf, 2190 / 6 * self.sf),
                          (900 / 8 * self.sf, 2490 / 6 * self.sf), (1100 / 8 * self.sf, 2590 / 6 * self.sf),
                          (1250 / 8 * self.sf, 2590 / 6 * self.sf), (1500 / 8 * self.sf, 2590 / 6 * self.sf),
                          (1660 / 8 * self.sf, 2590 / 6 * self.sf),
                          (1720 / 8 * self.sf, 2700 / 6 * self.sf), (1800 / 8 * self.sf, 2800 / 6 * self.sf),
                          (2380 / 8 * self.sf, 3180 / 6 * self.sf), (3080 / 8 * self.sf, 3140 / 6 * self.sf),
                          (3480 / 8 * self.sf, 3080 / 6 * self.sf), (3580 / 8 * self.sf, 2780 / 6 * self.sf),
                          (3520 / 8 * self.sf, 2720 / 6 * self.sf), (3500 / 8 * self.sf, 2580 / 6 * self.sf),
                          (3430 / 8 * self.sf, 2540 / 6 * self.sf), (3680 / 8 * self.sf, 2610 / 6 * self.sf),
                          (3850 / 8 * self.sf, 2610 / 6 * self.sf), (4050 / 8 * self.sf, 2510 / 6 * self.sf),
                          (4200 / 8 * self.sf, 2410 / 6 * self.sf), (4230 / 8 * self.sf, 2110 / 6 * self.sf),
                          (4200 / 8 * self.sf, 1910 / 6 * self.sf), (4000 / 8 * self.sf, 1730 / 6 * self.sf),
                          (3920 / 8 * self.sf, 1700 / 6 * self.sf), (3920 / 8 * self.sf, 1670 / 6 * self.sf),
                          (4320 / 8 * self.sf, 1270 / 6 * self.sf), (4220 / 8 * self.sf, 1070 / 6 * self.sf),
                          (3620 / 8 * self.sf, 730 / 6 * self.sf),
                          (3300 / 8 * self.sf, 370 / 6 * self.sf), (3300 / 8 * self.sf, 170 / 6 * self.sf), (3520 / 8 * self.sf, 0 / 6 * self.sf)]


        scale_x = 650 / 650  # Współczynnik skali w osi X
        scale_y = 470 / 600  # Współczynnik skali w osi Y
        self.waypoints = [(x * scale_x, y * scale_y) for x, y in self.waypoints]

        self.Troll = Troll((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,
              (64 * self.sf, 50 * self.sf), self.sf)
        self.Dragon = Dragon((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,
                        (64 * self.sf, 50 * self.sf), self.sf)
        self.Ghost = Ghost((-250 / 8 * self.sf, 3100 / 6 * self.sf),self.waypoints,
                      (64 * self.sf, 50 * self.sf), self.sf)
        self.Goblin = Goblin((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,
                        (44 * self.sf, 40 * self.sf), self.sf)
        self.Hydra = Hydra((-250 / 8 * self.sf, 3100 / 6 * self.sf),self.waypoints,
                      (64 * self.sf, 50 * self.sf), self.sf)
        self.Skeleton = Skeleton((-250 / 8 * self.sf, 3100 / 6 * self.sf),self.waypoints,
                            (64 * self.sf, 50 * self.sf), self.sf)
        self.Thief = Thief((-250 / 8 * self.sf, 3100 / 6 * self.sf),self.waypoints,
                      (64 * self.sf, 50 * self.sf), self.sf)

        self.monsters = pygame.sprite.Group()

    def create_wave(self):
        if self.won:
            return
        if self.wave_num <= self.max_waves:
            self.wave_running = True
            if self.wave_num == 1:
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0]+self.map_start_coefficient_x, self.map_base_spawn_point[1]+self.map_start_coefficient_y)), self.waypoints, (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))


            elif self.wave_num == 2:
                pass
                self.monsters.add(Goblin((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,(44 * self.sf, 40 * self.sf), self.sf,speed=9))
                self.monsters.add(Goblin((-1050 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,(44 * self.sf, 40 * self.sf), self.sf,speed=9))
                self.monsters.add(Goblin((-1850 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (44 * self.sf, 40 * self.sf), self.sf,speed=9))
            elif self.wave_num == 3:
                self.monsters.add(Thief((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (44 * self.sf, 40 * self.sf), self.sf,speed=9))
            elif self.wave_num == 4:
                self.monsters.add(
                    Dragon((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (44 * self.sf, 40 * self.sf),self.sf, speed=4))
            elif self.wave_num == 5:
                pass
            elif self.wave_num == 6:
                pass
            elif self.wave_num == 7:
                pass
            elif self.wave_num == 8:
                pass
            elif self.wave_num == 9:
                pass
            elif self.wave_num == 10:
                pass
            elif self.wave_num == 11:
                pass
            elif self.wave_num == 12:
                pass
            elif self.wave_num == 13:
                pass
            elif self.wave_num == 14:
                pass
            elif self.wave_num == 15:
                pass
            elif self.wave_num == 16:
                pass
            elif self.wave_num == 17:
                pass
            elif self.wave_num == 18:
                pass
            elif self.wave_num == 19:
                pass
            elif self.wave_num == 20:
                pass
            elif self.wave_num == 21:
                pass
            elif self.wave_num == 22:
                pass
            elif self.wave_num == 23:
                pass
            elif self.wave_num == 24:
                pass
            elif self.wave_num == 25:
                pass
            elif self.wave_num == 26:
                pass
            elif self.wave_num == 27:
                pass
            elif self.wave_num == 28:
                pass
            elif self.wave_num == 29:
                pass
            elif self.wave_num == 30:
                pass
            elif self.wave_num == 31:
                pass
            elif self.wave_num == 32:
                pass
            elif self.wave_num == 33:
                pass
            elif self.wave_num == 34:
                pass
            elif self.wave_num == 35:
                pass
            elif self.wave_num == 36:
                pass
            elif self.wave_num == 37:
                pass
            elif self.wave_num == 38:
                pass
            elif self.wave_num == 39:
                pass
            elif self.wave_num == 40:
                pass
            elif self.wave_num == 41:
                pass
            elif self.wave_num == 42:
                pass
            elif self.wave_num == 43:
                pass
            elif self.wave_num == 44:
                pass
            elif self.wave_num == 45:
                pass
            elif self.wave_num == 46:
                pass
            elif self.wave_num == 47:
                pass
            elif self.wave_num == 48:
                pass
            elif self.wave_num == 49:
                pass
            elif self.wave_num == 50:
                pass
            elif self.wave_num == 51:
                pass
            elif self.wave_num == 52:
                pass
            elif self.wave_num == 53:
                pass
            elif self.wave_num == 54:
                pass
            elif self.wave_num == 55:
                pass
            elif self.wave_num == 56:
                pass
            elif self.wave_num == 57:
                pass
            elif self.wave_num == 58:
                pass
            elif self.wave_num == 59:
                pass
            elif self.wave_num == 60:
                pass
            elif self.wave_num == 61:
                pass
            elif self.wave_num == 62:
                pass
            elif self.wave_num == 63:
                pass
            elif self.wave_num == 64:
                pass
            elif self.wave_num == 65:
                pass
            elif self.wave_num == 66:
                pass
            elif self.wave_num == 67:
                pass
            elif self.wave_num == 68:
                pass
            elif self.wave_num == 69:
                pass
            elif self.wave_num == 70:
                pass
            elif self.wave_num == 71:
                pass
            elif self.wave_num == 72:
                pass
            elif self.wave_num == 73:
                pass
            elif self.wave_num == 74:
                pass
            elif self.wave_num == 75:
                pass

    def check_if_wave_finished(self):
        if self.wave_running:
            if not self.monsters:
                self.wave_running = False
                self.wave_num += 1
                if self.wave_num > self.max_waves:
                    self.wave_num -= 1
                    self.win()

    def win(self):
        self.won = True

    def lose(self):
        self.lost = True

    def draw_victory(self):
        for i in range(self.screen.get_height()):
            color = (
                int(255 - (i / self.screen.get_height()) * 255),  # Od czerwonego
                int((i / self.screen.get_height()) * 255),        # do zielonego
                0                                                # Stały niebieski
            )
            pygame.draw.line(self.screen, color, (0, i), (self.screen.get_width(), i))
        font = pygame.font.Font(None, 100)
        victory_text = "Victory!"
        text_color = (128, 0, 128)
        text_surface = font.render(victory_text, True, text_color)
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)

        # Animowane iskry (opcjonalnie)
        for _ in range(10):  # Losowe iskry
            spark_x = text_rect.centerx + random.randint(-200, 200)
            spark_y = text_rect.centery + random.randint(-100, 100)
            spark_color = (255, random.randint(200, 255), 0)  # Iskry w odcieniach żółci i pomarańczu
            pygame.draw.circle(self.screen, spark_color, (spark_x, spark_y), random.randint(2, 5))

    def draw_loss(self):
        defeat_screen = pygame.image.load("assets/miscelanneous/defeat.png")
        #defeat_screen = pygame.transform.scale(defeat_screen, (d, defeat_height))
        # Załaduj czcionkę
        font_path = "Fonts/Pixeltype.ttf"  # Ścieżka do pliku czcionki
        font_size = 80  # Rozmiar czcionki
        font = pygame.font.Font(font_path, font_size)  # Ładowanie czcionki
        font.set_bold(True)

        text_surface = font.render("YOU LOST", True, (255, 0, 0))  # Czerwony kolor napisu


        # 1. Stwórz pełne tło
        background_color = (0, 0, 0)  # Czarny kolor tła
        self.screen.fill(background_color)  # Wypełni ekran tłem

        self.screen.blit(text_surface, (280 + 5, 150 + defeat_screen.get_height() + 10))
        self.screen.blit(defeat_screen, (280, 150))


    def draw(self, won):
        '''wave_text = f"{self.wave_num}/{self.max_waves}"
        font = pygame.font.Font(None, 30)
        wave_surface = font.render(wave_text, True, (255, 255, 255))  # Kolor tekstu biały
        wave_rect = wave_surface.get_rect(center=(self.screen.get_width() - 100, 30))
        self.screen.blit(wave_surface, wave_rect)'''
        if self.won:
            self.draw_victory()
        elif self.lost:
            self.draw_loss()

    def update(self):
        self.monsters.update()  # Aktualizacja ruchu potworów w grupie
        self.monsters.draw(self.screen)  # Rysowanie potworów na ekranie
        self.draw(self.won)
        self.check_if_wave_finished()


    def getMonsters(self):
        return self.monsters
