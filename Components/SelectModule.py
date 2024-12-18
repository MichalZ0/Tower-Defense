import pygame
from Components import TextModule
from Components import ButtonModule

class Select:
    state = 0
    def __init__(self, screen, size, options, position, functions, selected=''):
        self.screen = screen
        self.initialScreen = None
        self.size = size
        self.position = position
        self.selectElementsLen = len(options)
        self.optionsTexts = options
        self.functions= functions

        self.arrowSize = (self.size[1], self.size[1])
        self.selectRect = pygame.Rect(self.position[0],self.position[1], self.size[0] + self.arrowSize[1], self.size[1])

        self.selectedElement = pygame.Surface((self.selectRect.width, self.selectRect.height))

        self.arrow = pygame.Surface((self.size[1], self.size[1]))
        arrow_points = [(30, 54), (6, 6), (54, 6)]
        self.arrow.fill('gray')
        pygame.draw.polygon(self.arrow, (255, 255, 255), arrow_points)


        self.selectedOptionButton = ButtonModule.Button(self.selectedElement, (self.selectRect.width - self.arrowSize[0], self.selectRect.height), (0,0), 'blue', selected)
        self.selectedOptionButton.draw()

        self.selectedElement.blit(self.arrow, (self.selectedElement.get_width()-self.arrow.get_width(), 0))

        self.expandedSelect = pygame.Surface((self.selectRect.width, self.selectRect.height * self.selectElementsLen + self.selectRect.height))
        self.expandedSelect.fill('black')

        self.expandedSelect.blit(self.selectedElement, (0, 0))

        self.currentMenuState = 0
        self.menuStates = [self.selectedElement, self.expandedSelect]

        self.options = [] 
        self.prevState = 1
        self.testState = 0

        for i in range(0, len(options)): 
            self.options.append(ButtonModule.Button(self.expandedSelect, (self.selectRect.width, self.selectRect.height), (0, (i+1) * self.selectRect.height), "red", options[i]))
            self.options[i].onClick(self.functions[i])
            self.options[i].draw()




    def draw(self):
        self.screen.blit(self.menuStates[self.currentMenuState], (self.selectRect.x, self.selectRect.y))
        pygame.display.update(pygame.Rect(100, 100, 100, 100))


    def clicked(self, event):

        if (self.currentMenuState == 1): 
            for option in self.options:
                self.buttonClickRect = option.getRect().copy()
                
                self.buttonClickRect.x = self.selectRect.x
                self.buttonClickRect.y += self.selectRect.y

                res = option.clicked(event, self.buttonClickRect)
                if (res == True):
                    self.selectNewElement(option.getText(), option.getClickFunction())


        
        if (self.selectRect.collidepoint(event.pos)):
            self.currentMenuState = int(not self.currentMenuState)
        else:
            self.screen.blit(self.initialScreen, (0,0))
            self.currentMenuState = 0 







    def setClearScreen(self, newScreen):
        self.initialScreen = newScreen


    def isActive(self):
        return self.currentMenuState


    def selectNewElement(self, text, function): 
        self.selectedOptionButton = ButtonModule.Button(self.selectedElement, (self.selectRect.width - self.arrowSize[0], self.selectRect.height), (0,0), "blue", text)
        self.selectedOptionButton.onClick(function) 
        self.selectedOptionButton.draw()
        self.expandedSelect.blit(self.selectedElement, (0, 0))
