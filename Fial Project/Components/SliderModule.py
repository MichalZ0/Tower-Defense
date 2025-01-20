import pygame
from Components import TextModule
import Settings

class Slider:
    def __init__(self, screen, size, pos):
        self.screen = screen
        self.pressed = 0
        self.pos = (0,0)
        self.volume = float(Settings.Settings.readRaw()['volume'])

        self.sliderRect = pygame.Rect(pos[0], pos[1], size[0], size[1] )

        self.sliderSurface = pygame.Surface(self.sliderRect.size)
        pygame.draw.rect(self.sliderSurface, "red", (0,0, self.sliderRect.width, self.sliderRect.height), border_radius=self.sliderRect.height//2)

        self.headRadius = self.sliderRect.height/2

        self.headDrawRange = (self.headRadius, self.sliderRect.width - self.headRadius)
        

        self.headPosition = [self.calculatePercentageInRange(self.headDrawRange, self.volume), self.headRadius]
        self.sliderHead = pygame.draw.circle(self.sliderSurface, "white", self.headPosition, self.headRadius)



    def drawHead(self):
        pygame.draw.rect(self.sliderSurface, "red", (0,0, self.sliderRect.width, self.sliderRect.height), border_radius=self.sliderRect.height//2)
        self.sliderHead = pygame.draw.circle(self.sliderSurface, "white", self.headPosition, self.headRadius)

    def draw(self):
        self.screen.blit(self.sliderSurface, (self.sliderRect.x, self.sliderRect.y))


    def calculatePercentageInRange(self, range, input):
        return (input * (range[1] - range[0]) / 100) + range[0] 

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.sliderRect.collidepoint(event.pos): 
            self.pressed = 1

        if (self.pressed == 1): 
            self.headPosition[0] = event.pos[0] - self.sliderRect.x
            if (event.pos[0] < self.sliderRect.x + self.headRadius):
                self.headPosition[0] = self.headRadius
            if (event.pos[0] > self.sliderRect.x + self.sliderRect.width - self.headRadius):
                self.headPosition[0] = self.sliderRect.width - self.headRadius

            self.drawHead()
            
            self.volume = ((self.headPosition[0] - self.headDrawRange[0]) * 100) / (self.headDrawRange[1] - self.headDrawRange[0])
            self.volume = round(self.volume, 1)
            
         

        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = 0

        return self.volume

    def percentageDisplay(self, pos):
        self.percentageSurface = pygame.Surface((100, 100))
        self.strValue = str(self.volume) + '%'

        self.value = TextModule.Text(self.percentageSurface, (0, 0),  self.strValue)
        self.value.draw()
        self.screen.blit(self.percentageSurface, (pos[0], pos[1]))

    def getRect(self):
        return self.sliderRect

