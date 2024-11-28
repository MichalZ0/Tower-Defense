import pygame
import os

from Components import ButtonModule
from Components import TextModule
from Components import SelectModule 
from Components import SliderModule 

import Settings
import game

class mainMenu:
    def __init__(self, screen, backgroundColor='white', scaleFactor=1):

        self.running = True

        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.screenMode = 0

        self.sf = scaleFactor
        print(self.sf)
                

        self.menuScreen = pygame.Surface((self.screenRect.width, self.screenRect.height))
        self.settingsScreen = pygame.Surface((self.screenRect.width, self.screenRect.height)) 

        self.screens = [self.menuScreen, self.settingsScreen]
        self.currentScreen = 0; 

        self.screenWidth = self.menuScreen.get_size()[0]
        self.backgroundColor = backgroundColor

        # self.music = pygame.mixer.music.load('assets/New Folder/soundstd/shooting/fire.mp3')
        # pygame.mixer.music.play(-1)
        # pygame.mixer_music.set_volume(float(Settings.Settings.readRaw()['volume'])/100)
        
      
    
        self.buttonWidth = 420 * self.sf
        self.buttonHeight = 80 * self.sf
        self.buttonSize = (self.buttonWidth, self.buttonHeight)

        self.screenCenter = [self.menuScreen.get_width() / 2, self.menuScreen.get_height() / 2]

        # self.backgroundImage = pygame.image.load(os.path.join(os.getcwd(), 'assets', 'background.jpg'))
        self.backgroundImage = pygame.image.load(os.path.join(os.getcwd(), 'assets', 'test.jpg'))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.menuScreen.get_width(), self.menuScreen.get_height()))

        self.title = TextModule.Text(self.menuScreen, (10*self.sf,10*self.sf), "TOWER DEFENSE", 36)
        self.title.setPosition((self.screenWidth/2 - self.title.getSize()[0]/2, 10*self.sf))

        self.startButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, 100*self.sf), 'blue', "Start game", borderRadius=30, hoverBg='gray')

        self.buttonGap = 30*self.sf

        self.settingsButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, self.startButton.getPosition()[1] + self.buttonHeight + self.buttonGap), 'green', "Settings", borderRadius=30, hoverBg='gray')

        self.exitButton = ButtonModule.Button(self.menuScreen, self.buttonSize, (self.screenCenter[0] - self.buttonWidth / 2, self.settingsButton.getPosition()[1] + self.buttonHeight + self.buttonGap), 'red', "Exit game", borderRadius=30, hoverBg='gray')


        self.buttons = [self.startButton, self.settingsButton, self.exitButton]

        self.startButton.onClick(self.startGame)
        self.exitButton.onClick(self.Exit)
        self.settingsButton.onClick(self.goToSettings)

        self.settings()





    def startGame(self):
        self.newGame = game.Game(self.screen, self.sf)
        self.currentScreen = 3

    def goToSettings(self): 
        self.currentScreen = 1 


    def draw(self):
        self.menuScreen.blit(self.backgroundImage, (0,0))
        self.title.draw()
        self.startButton.draw()
        self.settingsButton.draw()
        self.exitButton.draw()
        self.screen.blit(self.menuScreen, (0,0))


 
    def menuRun(self):
        while self.currentScreen==0: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentScreen = None
                    self.running = False
                
                if event.type == pygame.MOUSEMOTION:
                    ButtonModule.isHovered(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.startButton.clicked(event)):
                        pass
                    self.settingsButton.clicked(event)
                    self.exitButton.clicked(event)

            
                self.draw()
                pygame.display.flip()

    def run(self):
        while self.running: 
            if (self.currentScreen == 0):
                self.menuRun()
            if (self.currentScreen == 1):
                self.settingsRun() 
            if (self.currentScreen == 3): 
                self.running, self.currentScreen = self.newGame.run()
                


    def Exit(self):
        self.currentScreen=None
        self.running = False;
    
    def setWindowed(self):
        Settings.Settings.set('display', 'windowed')
        self.screen = pygame.display.set_mode(Settings.Settings.getSettings()['resolution'])
        
        self.screenMode = 0

        return True

    def setFullscreen(self): 
        Settings.Settings.set('display', 'fullscreen')
        self.screen = pygame.display.set_mode(Settings.Settings.getSettings()['resolution'], 
                                              Settings.Settings.getSettings()['display'])
        self.screenMode = pygame.FULLSCREEN
        return True
        
    def setResolution(self, *args):
        newSize = str(args[0])
        Settings.Settings.set('resolution', newSize) 
        scaleFactor = ((Settings.Settings.getSettings()['resolution'][0] * 100) / 800)/100 
        self.screen = pygame.display.set_mode(Settings.Settings.getSettings()['resolution'], self.screenMode)
        self.__init__(self.screen, scaleFactor=scaleFactor)

    def goBack(self):
        self.currentScreen = 0
        
    def settings(self):

        self.settingsFont = TextModule.Text(self.settingsScreen, (0,0), "SETTINGS", size=48)
        self.displayFont = TextModule.Text(self.settingsScreen, (0, (self.settingsFont.getPosition()[1] + 80)*self.sf)
                                           , "Display", size=24)

        self.displayTextFormatted = Settings.Settings.readRaw()['display'].capitalize()

        self.displaySettings = SelectModule.Select(self.settingsScreen, (300*self.sf, 60*self.sf), ['Windowed', 'Fullscreen'], (100*self.sf,100*self.sf), [self.setWindowed, self.setFullscreen], self.displayTextFormatted)

        self.resolutionTextFormatted = Settings.Settings.readRaw()['resolution'].split(',')
        self.resolutionTextFormatted = self.resolutionTextFormatted[0] + 'x' + self.resolutionTextFormatted[1]
        self.resolution = SelectModule.Select(self.settingsScreen, (300*self.sf, 60*self.sf), ['1024x768','800x600'], (100*self.sf,200*self.sf), [lambda: self.setResolution('1024,768'), lambda: self.setResolution('800,600')], self.resolutionTextFormatted)


        self.gameVolume = SliderModule.Slider(self.settingsScreen, (383*self.sf, 30*self.sf), (100*self.sf, 300*self.sf))

        self.applyButton = ButtonModule.Button(self.settingsScreen, (self.buttonWidth, self.buttonHeight), (self.menuScreen.get_width()/2 - self.buttonWidth/2, 450*self.sf), 'red', "Apply changes", borderRadius=30)
        self.applyButton.onClick(self.goBack)

        self.updateRect = (0,0, self.screenRect.width, self.screenRect.height)

        self.displaySettings.setClearScreen(self.screen.copy())
        self.resolution.setClearScreen(self.screen.copy())


    def settingsRun(self):
        
        self.settingsDraw()
        pygame.display.flip()
        self.updateRect = pygame.Rect(100*self.sf, 100*self.sf, (self.screenRect.width - 100)*self.sf, 
                                      (self.screenRect.height - 100)*self.sf)


        while self.currentScreen == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                    return 

                if (event.type == pygame.MOUSEBUTTONDOWN): 

                    if (self.displaySettings.isActive()==0):
                        self.resolution.clicked(event)
                    self.displaySettings.clicked(event)


                    self.applyButton.clicked(event)

                vol = self.gameVolume.clicked(event)
                Settings.Settings.set('volume', str(vol))

                if (vol != None):
                    pygame.mixer_music.set_volume(vol/100)

            self.settingsDraw()
            pygame.display.update()


    def settingsDraw(self): 
        self.settingsScreen.fill('black')
        self.settingsFont.draw()

        self.gameVolume.draw()
        self.gameVolume.percentageDisplay((self.gameVolume.getRect().width + self.gameVolume.getRect().x, self.gameVolume.getRect().y))
        self.resolution.draw()
        self.displaySettings.draw()
        self.displayFont.draw()
        self.applyButton.draw()

        self.screen.blit(self.settingsScreen, (0,0))
