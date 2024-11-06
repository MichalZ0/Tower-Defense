import pygame

class Slider:
    def __init__(self, screen, size, pos):
        self.screen = screen

        self.sliderRect = pygame.Rect(pos[0], pos[1], size[0], size[1] )

        self.sliderSurface = pygame.Surface(self.sliderRect.size)
        pygame.draw.rect(self.sliderSurface, "red", (0,0, self.sliderRect.width, self.sliderRect.height), border_radius=10)

        self.sliderHead = pygame.draw.circle(self.sliderSurface, "white", (self.sliderRect.width/2, self.sliderRect.height/2), self.sliderRect.height/2)


        
        

    def draw(self):
        self.screen.blit(self.sliderSurface, (self.sliderRect.x, self.sliderRect.y))






