import pygame
from creatures import *
import math
import random
import math

from Components.ButtonModule import *


class Waves:
    def __init__(self, sf, screen, difficulty = 'easy', mapName='Greenfield',max_waves=50):
        self.screen = screen
        self.sf = sf
        self.wave_num = 1
        self.max_waves = max_waves
        self.wave_running = False
        self.won = False
        self.lost = False
        self.map_base_spawn_point = (-250 / 8, 3100 / 6)  # dla mapy 1
        self.map_base_spawn_point = (2150 / 8, 4100 / 6)  # dla mapy 2
        #self.map_base_spawn_point = (670/8, 170/6) #dla mapy 3
        #WSPOLCZYNNIKI DLA MAPY CAVE ABY POTWORY SIE SPAWNOWALY W DOBRYM MIEJSCU
        self.map_start_coefficient_x = -math.sqrt(2)
        self.map_start_coefficient_y = -math.sqrt(2)
        #WSPLCZYNNIKI ALE DLA MAPY DESERT
        self.map_start_coefficient_x = 0
        self.map_start_coefficient_y = 2
        #WPOSLCZYNNIKI DLA MAPY ZIELONEJ
        #self.map_start_coefficient_x = -2
        #self.map_start_coefficient_y = 0
        #DO MAPY 1
        self.waypointsDict = {
                          'Greenfield': [(580/8*self.sf, 3100/6*self.sf), (580/8*self.sf, 2070/6*self.sf),
                          (1580/8*self.sf, 2070/6*self.sf), (1580/8*self.sf, 1270/6*self.sf),
                          (700/8*self.sf, 1270/6*self.sf), (700/8*self.sf, 600/6*self.sf),
                          (2310/8*self.sf, 600/6*self.sf), (2310/8*self.sf, 2440/6*self.sf),
                          (3720/8*self.sf, 2440/6*self.sf), (3720/8*self.sf, 1750/6*self.sf),
                          (3050/8*self.sf, 1750/6*self.sf), (3050/8*self.sf, 400/6*self.sf),
                          (3600/8*self.sf, 400/6*self.sf), (3600/8*self.sf, 1275/6*self.sf),
                          (4500/8*self.sf, 1275/6*self.sf)], 
        #DO MAPY 2
                'Desert': [(1980 / 8 * self.sf, 2680 / 6 * self.sf), (2180 / 8 * self.sf, 2580 / 6 * self.sf),
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
                          ], 
        # DO MAPY 3
            'Cave': [(920 / 8 * self.sf, 420 / 6 * self.sf), (1235 / 8 * self.sf, 660 / 6 * self.sf),
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
        } 


        self.waypoints = self.waypointsDict[mapName]
        self.monsters = pygame.sprite.Group()

    def create_wave(self):
        if self.won:
            return
        if self.wave_num <= self.max_waves:
            self.wave_running = True
            #DLA MAPY 
            # if self.wave_num == 1:
            #     self.monsters.add(Goblin((-250 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,(44 * self.sf, 44 * self.sf),self.sf,speed=1))
            #     self.monsters.add(Thief((-550 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (50 * self.sf, 50 * self.sf),self.sf, speed=1))
            #     self.monsters.add(Troll((-850 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (58 * self.sf, 58 * self.sf),self.sf, speed=1))
            #     self.monsters.add(Ghost((-1150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (44 * self.sf, 44 * self.sf),self.sf, speed=1))
            #     self.monsters.add(Hydra((-1450 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (73 * self.sf, 60 * self.sf),self.sf, speed=1))
            #     self.monsters.add(Skeleton((-1750 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (52 * self.sf, 54 * self.sf),self.sf, speed=1))
            #     self.monsters.add(Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),self.sf, speed=1))
            #     self.monsters.add(
            #         Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
            #                self.sf, speed=9))
            #     self.monsters.add(
            #         Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
            #                self.sf, speed=9))
            #DLA MAPY 2
            # if self.wave_num == 1:
            #     self.monsters.add(
            #         Goblin((2150 / 8 * self.sf, 4100 / 6 * self.sf), self.waypoints, (44 * self.sf, 44 * self.sf),
            #                self.sf, speed=2))
            #     self.monsters.add(
            #         Thief((-550 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (50 * self.sf, 50 * self.sf),
            #               self.sf, speed=1))
            #     self.monsters.add(
            #         Troll((-850 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (58 * self.sf, 58 * self.sf),
            #               self.sf, speed=1))
            #     self.monsters.add(
            #         Ghost((-1150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (44 * self.sf, 44 * self.sf),
            #               self.sf, speed=1))
            #     self.monsters.add(
            #         Hydra((-1450 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (73 * self.sf, 60 * self.sf),
            #               self.sf, speed=1))
            #     self.monsters.add(
            #         Skeleton((-1750 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (52 * self.sf, 54 * self.sf),
            #                  self.sf, speed=1))
            #     self.monsters.add(
            #         Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
            #                self.sf, speed=1))
            #     self.monsters.add(
            #         Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
            #                self.sf, speed=9))
            #     self.monsters.add(
            #         Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
            #                self.sf, speed=9))

            if self.wave_num == 1:
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0]+self.map_start_coefficient_x, self.map_base_spawn_point[1]+self.map_start_coefficient_y)), self.waypoints, (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
                    
                    # self.monsters.add(
                    # Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                    #          self.map_base_spawn_point[1] + self.map_start_coefficient_y)), self.waypoints,
                    #        (50 * self.sf, 50 * self.sf),
                    #        self.sf, speed=1))
                    # self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 120,
                    #                        self.map_base_spawn_point[1] + self.map_start_coefficient_y * 120)),
                    #                      self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                    # self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                    #                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                    #                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                    # self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                    #                       self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                    #                     self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                    # self.monsters.add(
                    #     Skeleton((-1750 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints,
                    #              (52 * self.sf, 54 * self.sf),
                    #              self.sf, speed=1))
                    # self.monsters.add(
                    #     Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
                    #            self.sf, speed=1))
                    # self.monsters.add(
                    #     Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
                    #            self.sf, speed=9))
                    # self.monsters.add(
                    #     Dragon((-2150 / 8 * self.sf, 3100 / 6 * self.sf), self.waypoints, (70 * self.sf, 70 * self.sf),
                    #            self.sf, speed=9))


            elif self.wave_num == 2:
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x, self.map_base_spawn_point[1] + self.map_start_coefficient_y)), self.waypoints,(44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*100,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*100)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 200,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 200)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))

            elif self.wave_num == 3:
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*100,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*100)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*200,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*200)),
                                         self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*300,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*300)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*400,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*400)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
            elif self.wave_num == 4:
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 30,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 30)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 60,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 60)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*260,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*260)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*290,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*290)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*320,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*320)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*350,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*350)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
            elif self.wave_num == 5:
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 140,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 140)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 280,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 280)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 420,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 420)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 560,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 560)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 700,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 700)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 840,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 840)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 980,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 980)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1120,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1120)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1260,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1260)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
            elif self.wave_num == 6:
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*20,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y*20)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 100,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 100)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 120,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 120)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 200,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 200)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 220,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 220)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 300,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 300)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 320,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 320)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 400,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 400)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 420,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 420)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 500,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 500)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 520,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 520)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
            elif self.wave_num == 7:
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 30,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 30)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 60,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 60)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 90,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 90)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 120,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 120)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 220,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 220)),
                                         self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 8:
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 100)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 9:
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 30,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 30)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 60,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 60)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 90,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 90)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 120,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 120)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 150,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 150)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 250,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 250)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 450,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 450)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 480,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 480)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 510,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 510)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 540,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 540)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 570,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 570)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 600,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 600)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
            elif self.wave_num == 10:
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                           self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*50,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*50)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*100)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*150,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*150)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*200,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*200)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))

            elif self.wave_num == 11:
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*50,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*50)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 170,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 170)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 200,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 200)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 230,
                                           self.map_base_spawn_point[1] + self.map_start_coefficient_y * 230)),
                                         self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 280,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 280)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 310,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 310)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 340,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 340)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 530,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 530)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 570,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 570)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))

            elif self.wave_num == 12:
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*30,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*30)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*60,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*60)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*110,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*110)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*160,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*160)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*190,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*190)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*220,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*220)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
            elif self.wave_num == 13:
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 100,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 100)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 130,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 130)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 160,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 160)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 300,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 300)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 300,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 300)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 330,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 330)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 360,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 360)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 600,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 600)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 500,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 500)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 530,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 530)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 560,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 560)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 800,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 800)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 650,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 650)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 680,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 680)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 710,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 710)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1100)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 900,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 900)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 930,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 930)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 960,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 960)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 990,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 990)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1020,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1020)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1050,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1050)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1080,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1080)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1110,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1110)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
            elif self.wave_num == 14:
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*100)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*200,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*200)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*300,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*300)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*400,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*400)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*500,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*500)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*600,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*600)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*700,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*700)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 15:
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 50,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 50)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 50,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 50)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 100)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 150,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 150)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 200,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 200)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 250,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 250)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 300,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 300)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 16:
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 100,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 100)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 130,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 130)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 130,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 130)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 260,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 260)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 290,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 290)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 310,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 310)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 440,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 440)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 470,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 470)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 470,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 470)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 660,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 660)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 690,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 690)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 650,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 650)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 880,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 880)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 910,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 910)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 850,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * 850)),
                                        self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1110,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1110)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * 1140,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * 1140)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
            elif self.wave_num == 17:
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*30,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*30)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*60,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*60)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*110,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*110)), self.waypoints,
                           (50 * self.sf, 50 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*160,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*160)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*190,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*190)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*220,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*220)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*270,
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y*270)), self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*300,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*300)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*330,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*330)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*360,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*360)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*410,
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y*410)), self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*460,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*460)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*490,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*490)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*520,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*520)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*570,
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y*570)), self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*620,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*620)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*650,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*650)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
                self.monsters.add(
                    Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*680,
                             self.map_base_spawn_point[1] + self.map_start_coefficient_y*680)), self.waypoints,
                           (44 * self.sf, 44 * self.sf),
                           self.sf, speed=1))
            elif self.wave_num == 18:
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*100,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*100)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*200,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*200)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*300,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*300)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*400,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y*400)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
            elif self.wave_num == 19:
                for x in range(22):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x*20,
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * x*20)), self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
            elif self.wave_num == 20:
                for x in range(3):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x*30,
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * x*30)),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(10):
                    self.monsters.add(
                        Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*30+230),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*30+230))), self.waypoints,
                              (50 * self.sf, 50 * self.sf),
                              self.sf, speed=1))
            elif self.wave_num == 21:
                for x in range(15):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x*30,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * x*30)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))

            elif self.wave_num == 22:
                for x in range(5):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x * 30,
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * x * 30)),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(15):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30+250),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30+250))), self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))

            elif self.wave_num == 23:
                for x in range(3):
                    self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x * 30,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * x * 30)),
                                        self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                for x in range(5):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30+100),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30+100))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(12):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30+380),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30+380))), self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
            elif self.wave_num == 24:
                for x in range(7):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x*30,
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * x*30)),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                for x in range(5):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30+160),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30+160))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(10):
                    self.monsters.add(
                        Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*30+400),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*30+400))), self.waypoints,
                              (50 * self.sf, 50 * self.sf),
                              self.sf, speed=1))
            elif self.wave_num == 25:
                for x in range(40):
                    self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x*20,
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * x*20)),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
            elif self.wave_num == 26:
                for x in range(17):
                    self.monsters.add(
                        Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*30),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*30))), self.waypoints,
                              (50 * self.sf, 50 * self.sf),
                              self.sf, speed=1))
                for x in range(14):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*30+900),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*30+900))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
            elif self.wave_num == 27:
                for x in range(14):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*150),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*60))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))

                for x in range(12):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30+1000),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30+1000))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 28:
                for x in range(24):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 23),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 23))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 29:
                for x in range(14):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 35),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 35))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))

                    self.monsters.add(Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 35+35+20*x),
                                                  self.map_base_spawn_point[
                                                      1] + self.map_start_coefficient_y * (x * 35+35+20*x))),
                                                self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
            elif self.wave_num == 30:
                for x in range(1):
                    self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x,
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y)),
                                            self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 31:
                for x in range(10):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30))), self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
                for x in range(2):
                    self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*(x*500+800)),
                                               self.map_base_spawn_point[1] + self.map_start_coefficient_y*(x*500+800)),
                                             self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 32:
                for x in range(2):
                    self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*(x*100)),
                                               self.map_base_spawn_point[1] + self.map_start_coefficient_y*(x*100)),
                                             self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 33:
                self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x),
                                               self.map_base_spawn_point[1] + self.map_start_coefficient_y),
                                             self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
                for x in range(25):
                    self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*40+80),
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*40+80))),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                for x in range(14):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*60+500),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*60+500))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
            elif self.wave_num == 34:
                for x in range(80):
                    self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*15),
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*15))),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
            elif self.wave_num == 35:
                for x in range(10):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30))),
                               self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
                for x in range(10):
                    self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30 + 300),
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30 + 300))),
                          self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                for x in range(10):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*60+800),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*60+800))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                self.monsters.add(
                    Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x + 2300)),
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x + 2300)),
                           self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 36:
                for x in range(50):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 25),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 25))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
            elif self.wave_num == 37:
                for x in range(7):
                    self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*(x*400)),
                                               self.map_base_spawn_point[1] + self.map_start_coefficient_y*(x*100)),
                                             self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 38:
                for x in range(10):
                    self.monsters.add(
                    Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * x * 35,
                            self.map_base_spawn_point[
                                1] + self.map_start_coefficient_y * x * 35)),
                          self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                for x in range(10):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 40+320),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 40+320))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(3):
                    self.monsters.add(Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x*(x*400+500)),
                                               self.map_base_spawn_point[1] + self.map_start_coefficient_y*(x*400+500)),
                                             self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 39:
                for x in range(10):
                    self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 30),
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 30))),
                          self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                    for x in range(5):
                        self.monsters.add(
                            Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 300+600)),
                                    self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 300+600)),
                                   self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 40:
                for x in range(3):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 80)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 80)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
                for x in range(3):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 80 + 500)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 80 + 500)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
                for x in range(3):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 80 + 1000)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 80 + 1000)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
                for x in range(3):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 80 + 1500)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 80 + 1500)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 41:
                for x in range(25):
                    self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*25),
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*25))),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                for x in range(25):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 25+700),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 25+700))),
                               self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
                for x in range(10):
                    self.monsters.add(
                    Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 35+1400),
                            self.map_base_spawn_point[
                                1] + self.map_start_coefficient_y * (x * 35+1400))),
                          self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                for x in range(25):
                    self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 25+1800),
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 25+1800))),
                          self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
            elif self.wave_num == 42:
                for x in range(5):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 100)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 100)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
                for x in range(30):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 25+350),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 25+350))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(15):
                    self.monsters.add(
                    Thief(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 25 + 1400),
                            self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 25 + 1400))),
                          self.waypoints,
                          (50 * self.sf, 50 * self.sf),
                          self.sf, speed=1))
                for x in range(5):
                    self.monsters.add(
                    Hydra(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 35+1800),
                            self.map_base_spawn_point[
                                1] + self.map_start_coefficient_y * (x * 35+1800))),
                          self.waypoints, (73 * self.sf, 60 * self.sf), self.sf, speed=1))
                for x in range(2):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 500 + 4000)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 500 + 4000)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 43:
                for x in range(100):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 10),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 10))),
                               self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
                for x in range(20):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*60+1500),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*60+1500))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                for x in range(5):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 200+3000)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 200+3000)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))
            elif self.wave_num == 44:
                for x in range(100):
                    self.monsters.add(Skeleton(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*25),
                                             self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*25))),
                                           self.waypoints, (52 * self.sf, 54 * self.sf), self.sf, speed=1))
                for x in range(20):
                    self.monsters.add(Troll(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 80+350),
                                              self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 80+350))),
                                            self.waypoints, (58 * self.sf, 58 * self.sf), self.sf, speed=0.8))
                for x in range(20):
                    self.monsters.add(Ghost(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x*90+1500),
                                          self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x*90+1500))),
                                        self.waypoints, (44 * self.sf, 44 * self.sf), self.sf, speed=1.5))
                for x in range(50):
                    self.monsters.add(
                        Goblin(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 50+10),
                                 self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 50+10))),
                               self.waypoints,
                               (44 * self.sf, 44 * self.sf),
                               self.sf, speed=1))
            elif self.wave_num == 45:
                for x in range(25):
                    self.monsters.add(
                        Dragon(((self.map_base_spawn_point[0] + self.map_start_coefficient_x * (x * 100)),
                                self.map_base_spawn_point[1] + self.map_start_coefficient_y * (x * 100)),
                               self.waypoints, (70 * self.sf, 70 * self.sf), self.sf, speed=2))


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
        self.monsters = pygame.sprite.Group()

    def draw_victory(self):
        defeat_screen = pygame.image.load("assets/miscelanneous/defeat.png")
        for i in range(self.screen.get_height()):
            color = (
                int(255 - (i / self.screen.get_height()) * 255),  # Od czerwonego
                int((i / self.screen.get_height()) * 255),        # do zielonego
                0                                                # Stały niebieski
            )
            pygame.draw.line(self.screen, color, (0, i), (self.screen.get_width(), i))
        font = pygame.font.Font(None, 100)
        victory_text = "YOU WON!"
        text_color = (128, 0, 128)
        text_surface = font.render(victory_text, True, text_color)
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)
        mage = pygame.image.load('assets/towers/MageTower/mag gotowy do strzału.png')
        mage = pygame.transform.scale(mage, (850, 800))
        mage_flipped = pygame.transform.flip(mage, True, False)
        self.screen.blit(mage_flipped, (-280, 0))
        self.screen.blit(mage, (233, 0))

        self.restartButton = Button(self.screen,
                                    (240, 70),
                                    (self.screen.get_width() / 2 - 240 / 2,
                                     100 + defeat_screen.get_height() + 10 + text_surface.get_height() + 20),
                                    "blue",
                                    "ZAGRAJ PONOWNIE",
                                    textSize=32)
        self.menuButton = Button(self.screen,
                                 (240, 70),
                                 (self.screen.get_width() / 2 - 240 / 2,
                                  self.restartButton.getPosition()[1] + self.restartButton.getSize()[1] + 20),
                                 "blue",
                                 "POWROT DO MENU",
                                 textSize=32)
        self.menuButton.draw()
        self.menuButton.onClick(self.goBackToMenu)


        # Animowane iskry
        for _ in range(10):  # Losowe iskry
            spark_x = text_rect.centerx + random.randint(-200, 200)
            spark_y = text_rect.centery + random.randint(-100, 100)
            spark_color = (255, random.randint(200, 255), 0)  # Iskry w odcieniach żółci i pomarańczu
            pygame.draw.circle(self.screen, spark_color, (spark_x, spark_y), random.randint(2, 5))

    def draw_loss(self):
        defeat_screen = pygame.image.load("assets/miscelanneous/defeat.png")
        font_path = "Fonts/Pixeltype.ttf"
        font_size = 80  # Rozmiar czcionki
        font = pygame.font.Font(font_path, font_size)  # Ładowanie czcionki
        font.set_bold(True)

        text_surface = font.render("YOU LOST", True, (0, 0, 0))  # Czarny kolor napisu


        # pełne tło
        background_color = (100,0,0)
        self.screen.fill(background_color)  # Wypełni ekran tłem

        self.screen.blit(text_surface, (255 , 100 + defeat_screen.get_height() + 10))
        self.screen.blit(defeat_screen, (280, 100))
        dragon = pygame.image.load('assets/creatures/Dragon/dragon_fire.png')
        dragon = pygame.transform.scale(dragon, (850, 800))
        dragon_flipped = pygame.transform.flip(dragon, True, False)
        self.screen.blit(dragon, (0, 50))
        self.screen.blit(dragon_flipped, (-60, 50))


        self.restartButton = Button(self.screen, 
                                    (240, 70),
                                    (self.screen.get_width()/2 - 240/2, 
                                     100 + defeat_screen.get_height() + 10 + text_surface.get_height() + 20),
                                    "blue",
                                    "ZAGRAJ PONOWNIE",
                                    textSize=32)


        self.menuButton = Button(self.screen, 
                                    (240, 70),
                                    (self.screen.get_width()/2 - 240/2, 
                                     self.restartButton.getPosition()[1] + self.restartButton.getSize()[1] + 20),
                                    "blue",
                                    "POWROT DO MENU",
                                    textSize=32)
        self.restartButton.draw()
        self.menuButton.draw()

        self.restartButton.onClick(self.restartGame)
        self.menuButton.onClick(self.goBackToMenu)


    def restartGame(self):
        return True

    def goBackToMenu(self): 
        return True



    def draw(self, won):
        wave_text = f"{self.wave_num}/{self.max_waves}"
        font = pygame.font.Font(None, 30)
        wave_surface = font.render(wave_text, True, (255, 255, 255))  # Kolor tekstu biały
        wave_rect = wave_surface.get_rect(center=(self.screen.get_width() - 100, 30))
        self.screen.blit(wave_surface, wave_rect)
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
