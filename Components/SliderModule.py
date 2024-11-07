import pygame

class Slider:
    def __init__(self, screen, size, pos):
        self.screen = screen
        self.pressed = 0
        self.pos = (0,0)
        self.volume = 0

        self.sliderRect = pygame.Rect(pos[0], pos[1], size[0], size[1] )

        self.sliderSurface = pygame.Surface(self.sliderRect.size)
        pygame.draw.rect(self.sliderSurface, "red", (0,0, self.sliderRect.width, self.sliderRect.height), border_radius=10)

        self.sliderHead = pygame.draw.circle(self.sliderSurface, "white", (self.sliderRect.width/2, self.sliderRect.height/2), self.sliderRect.height/2)


        
        

    def draw(self):
        self.screen.blit(self.sliderSurface, (self.sliderRect.x, self.sliderRect.y))


    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pressed = 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = 0
        
        self.sliderLowestPos = self.sliderRect.x + self.sliderHead.width/2
        self.sliderHighestPos = (self.sliderRect.x + self.sliderRect.width) - self.sliderHead.width/2

        if event.type == pygame.MOUSEMOTION and self.pressed == 1:
            if (self.sliderRect.collidepoint(event.pos)):
                self.sliderSurface = pygame.Surface(self.sliderRect.size)
                pygame.draw.rect(self.sliderSurface, "red", (0,0, self.sliderRect.width, self.sliderRect.height), border_radius=10)
                
                if (event.pos[0] > self.sliderLowestPos and event.pos[0] < self.sliderHighestPos):
                    self.sliderHeadDrawPos = event.pos

                self.sliderHead = pygame.draw.circle(self.sliderSurface, "white", (self.sliderHeadDrawPos[0]-self.sliderRect.x, self.sliderRect.height/2), self.sliderRect.height/2)
                self.volume = (self.sliderHeadDrawPos[0] * 100) / (self.sliderRect.width + self.sliderRect.x- (self.sliderHead.width/2))
                print(self.volume)

             
            






