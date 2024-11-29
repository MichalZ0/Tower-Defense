from creatures import *
from defenders import *
import os

class Game:
    def __init__(self, screen, sf): 
        pygame.init()
        self.screen = screen
        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        self.bgPath = os.path.join(os.getcwd(), 'assets', 'background.png')
        self.background = pygame.image.load(self.bgPath)
        self.sf = sf # Wspolczynnik wielkosci ekranu wzgledem bazowej rozdzielczosci (800x600)


        self.background = pygame.transform.scale(self.background, (self.width*self.sf, self.height*self.sf))
        # Inicjalizacja grupy potworów
        self.monsters = pygame.sprite.Group()

        scwidth = screen.get_width()
        scheight = screen.get_height()

        self.waypoints = [(120/1000*scwidth, 695/800*scheight), (120/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 272/800*scheight), (900/1000*scwidth, 272/800*scheight)]

        self.waypoints2 = []
        for i in range(len(self.waypoints) - 1):
            x1, y1 = self.waypoints[i]
            x2, y2 = self.waypoints[i+1]
            middle_x = (x1 + x2) / 2
            middle_y = (y1 + y2) / 2
            self.waypoints2.append((middle_x, middle_y))

        dragon = Dragon(position=(-50/1000*scwidth, 685/800*scheight), waypoints=self.waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=10/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight))
        self.monsters.add(dragon)

        self.monsters.add(Troll(position=(-50/1000*scwidth, 685/800*scheight), waypoints=self.waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=2/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))

        self.tower = None
        self.tower_group = pygame.sprite.Group()
        self.tower_image_path = os.path.join(os.getcwd(), 'assets', 'towers')

        self.towers = []

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

    def run(self):
        self.Is=0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return [False, None]

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return [True, 0]

                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:  # Lewy przycisk myszy
                    mouse_position = pygame.mouse.get_pos()  # Pobierz współrzędne myszy
                    print(mouse_position)
                    self.tower = Cannon(position=mouse_position, image_path=self.tower_image_path,range=100,damage=40)
                    if (len(self.towers) == 1): 
                        self.towers[0].hideRadius()

                    self.towers.append(self.tower)

                    if self.get_color_at_mouse_click(mouse_position):
                        self.tower_group.add(self.tower)
                        self.Is=1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for tower in self.towers:
                        if tower.getRect().collidepoint(event.pos):
                            tower.showRadius()
                        else: 
                            tower.hideRadius()


            self.draw()
            pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.tower_group.draw(self.screen)
        # Rysowanie linii łączących waypoints
        # if len(self.waypoints) > 1:
        #     pygame.draw.lines(self.screen, (0, 255, 0), False, self.waypoints2, 3)  # Zielona linia o grubości 3 pikseli

        self.monsters.update()  # Aktualizuje wszystkie potwory w grupie
        if self.Is ==1:
            self.tower.update(self.monsters)

        self.monsters.draw(self.screen)  # Renderuje wszystkie potwory w grupie
        
