from creature_classes import *


pygame.init()
width = 1500
height = 1100
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))
# Inicjalizacja grupy potworów
monsters = pygame.sprite.Group()

scwidth = screen.get_width()
scheight = screen.get_height()

waypoints = [(120/1000*scwidth, 695/800*scheight), (120/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 445/800*scheight), (315/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 275/800*scheight), (150/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 120/800*scheight), (452/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 529/800*scheight), (722/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 385/800*scheight), (595/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 85/800*scheight), (700/1000*scwidth, 272/800*scheight), (900/1000*scwidth, 272/800*scheight)]
# Dodanie potworow do grupy
dragon = Dragon(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=10/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight))
monsters.add(dragon)
monsters.add(Troll(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=2/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Ghost(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=7/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Goblin(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(50/1000*scwidth, 50/800*scheight), animation_speed=5, speed=4/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Hydra(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(75/1000*scwidth, 75/800*scheight), animation_speed=7, speed=3.5/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Skeleton(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=3/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))
monsters.add(Thief(position=(-50/1000*scwidth, 685/800*scheight), waypoints=waypoints, image_size=(64/1000*scwidth, 64/800*scheight), animation_speed=5, speed=5/1000 * (scwidth + scheight)/2, screen_size=(scwidth, scheight)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    monsters.update()  # Aktualizuje wszystkie potwory w grupie
    monsters.draw(screen)    # Renderuje wszystkie potwory w grupie
    pygame.display.flip()
