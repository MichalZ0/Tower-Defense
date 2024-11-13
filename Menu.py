import pygame
import os

from Components import ButtonModule
from Components import TextModule
from Components import SelectModule 
from Components import SliderModule 

class mainMenu:
    def __init__(self, screen, backgroundColor='white'):
        self.running = True

        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.screenMode = 0

        self.menuScreen = pygame.Surface((self.screenRect.width, self.screenRect.height))
        self.settingsScreen =pygame.Surface((self.screenRect.width, self.screenRect.height)) 

        self.screens = [self.menuScreen, self.settingsScreen]
        self.currentScreen = 0; 

        self.screenWidth = self.menuScreen.get_size()[0]
        self.backgroundColor = backgroundColor

        self.musicPath = os.path.join(os.getcwd(), 'sounds', 'nyan.mp3')
        self.music = pygame.mixer.music.load('assets/sounds/nyan.mp3')
        pygame.mixer.music.play()
        
      
    
        self.buttonWidth = 420
        self.buttonHeight = 80 
        self.buttonSize = (self.buttonWidth, self.buttonHeight)

        self.screenCenter = [self.menuScreen.get_width() / 2, self.menuScreen.get_height() / 2]

        # self.backgroundImage = pygame.image.load(os.path.join(os.getcwd(), 'assets', 'background.jpg'))
        self.backgroundImage = pygame.image.load(os.path.join(os.getcwd(), 'assets', 'test.jpg'))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.menuScreen.get_width(), self.menuScreen.get_height()))

        self.title = TextModule.Text(self.menuScreen, (10,10), "TOWER DEFENSE", 36)
        self.title.setPosition((self.screenWidth/2 - self.title.getSize()[0]/2, 10))

        self.startButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, 100), 'blue', "Start game", borderRadius=30)

        self.buttonGap = 30

        self.settingsButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, self.startButton.getPosition()[1] + self.buttonHeight + self.buttonGap), 'green', "Settings", borderRadius=30)

        self.exitButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, self.settingsButton.getPosition()[1] + self.buttonHeight + self.buttonGap), 'red', "Exit game", borderRadius=30)


        self.buttons = [self.startButton, self.settingsButton, self.exitButton]


        # self.startButton.onClick(self.test, 2)
        self.exitButton.onClick(self.Exit)
        self.settingsButton.onClick(self.goToSettings)

        self.settings()




    

    def goToSettings(self): 
        self.currentScreen = 1 


    def draw(self):
        self.menuScreen.blit(self.backgroundImage, (0,0))
        self.title.draw()
        self.startButton.draw()
        self.settingsButton.draw()
        self.exitButton.draw()


 
    def menuRun(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.startButton.clicked(event)):
                    pass
                self.settingsButton.clicked(event)
                self.exitButton.clicked(event)


        
            self.draw()
            self.screen.blit(self.menuScreen, (0,0))

    def run(self):
        while self.running: 
            if (self.currentScreen == 0):
                self.menuRun()
            if (self.currentScreen == 1):
                self.settingsRun() 



            pygame.display.flip()


    def Exit(self):
        self.running = False;
    
    def setWindowed(self):
        self.screen = pygame.display.set_mode((self.screenRect.width,self.screenRect.height))
        self.screenMode = 0

    def setFullscreen(self): 
        self.screen = pygame.display.set_mode((self.screenRect.width,self.screenRect.height), pygame.FULLSCREEN)
        self.screenMode = pygame.FULLSCREEN
        
    def setResolution(self, *args):
        newSize = args[0]
        self.screen = pygame.display.set_mode(newSize, self.screenMode)
        self.__init__(self.screen)

    def goBack(self):
        self.currentScreen = 0
        
    def settings(self):

        self.settingsFont = TextModule.Text(self.settingsScreen, (0,0), "SETTINGS", size=48)
        self.displayFont = TextModule.Text(self.settingsScreen, (0, self.settingsFont.getPosition()[1] + 80), "Display", size=24)

        self.displaySettings = SelectModule.Select(self.settingsScreen, (300, 60), ['Windowed', 'Fullscreen'], (100,100), [self.setWindowed, self.setFullscreen])

        self.resolution = SelectModule.Select(self.settingsScreen, (300, 60), ['1024x768','800x600'], (100,300), [lambda: self.setResolution((1024, 768)), lambda: self.setResolution((800, 600))])


        self.gameVolume = SliderModule.Slider(self.settingsScreen, (383, 25), (100, 450))

        self.applyButton = ButtonModule.Button(self.settingsScreen, (self.buttonWidth, self.buttonHeight), (self.menuScreen.get_width()/2 - self.buttonWidth/2, 600), 'red', "Apply changes", borderRadius=30)
        self.applyButton.onClick(self.goBack)

        self.initialScreen = pygame.Surface((self.screenRect.width, self.screenRect.height))
        self.settingsDraw(self.initialScreen)

        self.displaySettings.setClearScreen(self.initialScreen)
        self.resolution.setClearScreen(self.initialScreen)


    def settingsRun(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 

            if (event.type == pygame.MOUSEBUTTONDOWN): 
                self.displaySettings.clicked(event)
                self.resolution.clicked(event)
                self.applyButton.clicked(event)

            vol = self.gameVolume.clicked(event)
            if (vol != None):
                pygame.mixer_music.set_volume(vol)
    
            self.settingsDraw(self.screen)

        pygame.display.flip()


    def settingsDraw(self, screen): 
        self.displaySettings.draw()
        self.resolution.draw()
        self.gameVolume.draw()
        self.gameVolume.percentageDisplay((self.gameVolume.getRect().width + self.gameVolume.getRect().x, self.gameVolume.getRect().y))
        self.settingsFont.draw()
        self.displayFont.draw()
        self.applyButton.draw()

        self.screen.blit(self.settingsScreen, (0,0))






