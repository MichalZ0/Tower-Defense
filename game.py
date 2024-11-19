import pygame
import creature_classes

class Game:
    def __init__(self, screen): 
        self.screen = screen 
        self.screenSize = (self.screen.get_width(), self.screen.get_height())
        self.background = pygame.image.load("assets//background.png")
        self.background = pygame.transform.scale(self.background, self.screenSize)

        self.monsters = pygame.sprite.Group()

        scwidth, scheight = self.screenSize



        monsters = pygame.sprite.Group()
        waypoints = [(120/1000*scwidth, 695/800*scheight), 
                     (120/1000*scwidth, 445/800*scheight), 
                     (315/1000*scwidth, 445/800*scheight), 
                     (315/1000*scwidth, 275/800*scheight),
                     (150/1000*scwidth, 275/800*scheight),
                     (150/1000*scwidth, 120/800*scheight),
                     (452/1000*scwidth, 120/800*scheight),
                     (452/1000*scwidth, 529/800*scheight),
                     (722/1000*scwidth, 529/800*scheight),
                     (722/1000*scwidth, 385/800*scheight),
                     (595/1000*scwidth, 385/800*scheight),
                     (595/1000*scwidth, 85/800*scheight),
                     (700/1000*scwidth, 85/800*scheight),
                     (700/1000*scwidth, 272/800*scheight),
                     (900/1000*scwidth, 272/800*scheight)]

        # Dodanie potworow do grupy
        dragon = creature_classes.Dragon(
                                         # position=(-50/1000*scwidth, 685/800*scheight), 
                                         position=(0,0),
                                         waypoints=waypoints,
                                         image_size=(64/1000*scwidth, 64/800*scheight),
                                         animation_speed=5,
                                         speed=10/1000 * (scwidth + scheight)/2,
                                         screen_size=(scwidth, scheight))
        monsters.add(dragon)





    def run(self):
        running = True
        while running:
          for event in pygame.event.get():

            if event.type == pygame.QUIT:
              return False, 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, 0
            

          self.draw()
          pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.monsters.update()
        self.monsters.draw(self.screen)