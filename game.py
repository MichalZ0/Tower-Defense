import pygame
class Game:
    def __init__(self, screen): 
        self.screen = screen 

    def run(self):
        running = True
        while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
            

          self.screen.fill('black')
          pygame.display.flip()
