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
        self.waypoints = [(580/8*self.sf, 3100/6*self.sf), (580/8*self.sf, 2070/6*self.sf),
                          (1580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 1270/6*self.sf),
                          (700/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 600/6*self.sf),
                          (2310/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 2440/6*self.sf),
                          (3720/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 1750/6*self.sf),
                          (3050/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 400/6*self.sf),
                          (3600/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 1275/6*self.sf),
                          (4500/8*self.sf, 1275/6*self.sf)]
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
                self.monsters.add(Goblin((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,(44 * self.sf, 40 * self.sf),self.sf,speed=9))
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

    def draw(self, won):
        wave_text = f"{self.wave_num}/{self.max_waves}"
        font = pygame.font.Font(None, 30)
        wave_surface = font.render(wave_text, True, (255, 255, 255))  # Kolor tekstu biały
        wave_rect = wave_surface.get_rect(center=(self.screen.get_width() - 100, 30))
        self.screen.blit(wave_surface, wave_rect)
        if self.won:
            self.draw_victory()

    def update(self):
        self.monsters.update()  # Aktualizacja ruchu potworów w grupie
        self.monsters.draw(self.screen)  # Rysowanie potworów na ekranie
        self.draw(self.won)
        self.check_if_wave_finished()
