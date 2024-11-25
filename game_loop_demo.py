from creature_classes import *
from klasy_obrońców import *





pygame.init()
width = 1500
height = 1100
screen = pygame.display.set_mode((width, height))
background = pygame.image.load(r"C:\Users\ignac\OneDrive\Pulpit\folder gry\graphicstd\map\background.png")


background = pygame.transform.scale(background, (width, height))
# Inicjalizacja grupy potworów
monsters = pygame.sprite.Group()

scwidth = screen.get_width()
scheight = screen.get_height()

waypoints = [(120/1000*scwidth, 695/800*scheight), (120/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 272/800*scheight), (900/1000*scwidth, 272/800*scheight)]
waypoints2 = [(x + 50, y) for x, y in waypoints]


def get_color_at_mouse_click(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Uzyskanie współrzędnych kliknięcia
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Sprawdzanie koloru piksela w tym miejscu
        color = screen.get_at((mouse_x, mouse_y))
        #print(f"Kolor w miejscu kliknięcia: {color}")
        R, G, B, A = color  # Przypisanie wartości składowych koloru
        brightness = 0.2126 * R + 0.7152 * G + 0.0722 * B  # Obliczanie jasności

        # Jeśli jasność jest powyżej pewnego progu (np. 128), uznajemy kolor za jasny
        return brightness > 128




# Dodanie potworow do grupy
dragon = Dragon(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=10/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight))
monsters.add(dragon)
monsters.add(Troll(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=2/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Ghost(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=7/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Goblin(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(50/1000*scwidth, 50/800*scheight), animation_speed=5, speed=4/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Hydra(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(75/1000*scwidth, 75/800*scheight), animation_speed=7, speed=3.5/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Skeleton(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=3/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Thief(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=5/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))

#dodawanie wierż
tower_group = pygame.sprite.Group()
tower_image_path = r"C:\Users\ignac\OneDrive\Pulpit\folder gry\PLiki do gry tower defense\wierze\moździeź\moździeź1.png"
Is=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lewy przycisk myszy
            mouse_position = pygame.mouse.get_pos()  # Pobierz współrzędne myszy
            tower = Cannon(position=mouse_position, image_path=tower_image_path,range=100,damage=40)
            if get_color_at_mouse_click(event):
                tower_group.add(tower)
                Is=1# Dodaj nową wieżę do grupy
            
    screen.blit(background, (0, 0))
    tower_group.draw(screen)
    # Rysowanie linii łączących waypoints
    if len(waypoints) > 1:
        pygame.draw.lines(screen, (0, 255, 0), False, waypoints2, 3)  # Zielona linia o grubości 3 pikseli

    monsters.update()  # Aktualizuje wszystkie potwory w grupie
    if Is ==1:
        tower.update(monsters)
    monsters.draw(screen)  # Renderuje wszystkie potwory w grupie
    pygame.display.flip()
