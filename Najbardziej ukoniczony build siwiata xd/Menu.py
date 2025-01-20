import pygame
import os

from Components import ButtonModule
from Components import TextModule
from Components import SelectModule
from Components import SliderModule

import Settings
import game


class mainMenu:
    def __init__(self, screen, backgroundColor="white", scaleFactor=1):

        self.running = True

        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.screenMode = 0

        self.sf = scaleFactor
        print(self.sf)

        self.menuScreen = pygame.Surface(
            (self.screenRect.width, self.screenRect.height)
        )
        self.settingsScreen = pygame.Surface(
            (self.screenRect.width, self.screenRect.height)
        )
        self.selectLevelScreen = pygame.Surface(
            (self.screenRect.width, self.screenRect.height)
        )
        self.selectDifficultyScreen = pygame.Surface(
            (self.screenRect.width, self.screenRect.height)
        )

        self.screens = [
            self.menuScreen,
            self.settingsScreen,
            self.selectLevelScreen,
            self.selectDifficultyScreen,
        ]
        self.currentScreen = 0

        self.screenWidth = self.menuScreen.get_size()[0]
        self.backgroundColor = backgroundColor

        # self.music = pygame.mixer.music.load('assets/New Folder/soundstd/shooting/fire.mp3')
        # pygame.mixer.music.play(-1)
        # pygame.mixer_music.set_volume(float(Settings.Settings.readRaw()['volume'])/100)

        self.buttonWidth = 420 * self.sf
        self.buttonHeight = 80 * self.sf
        self.buttonSize = (self.buttonWidth, self.buttonHeight)

        self.screenCenter = [
            self.menuScreen.get_width() / 2,
            self.menuScreen.get_height() / 2,
        ]

        # self.backgroundImage = pygame.image.load(os.path.join(os.getcwd(), 'assets', 'background.jpg'))
        self.backgroundImage = pygame.image.load(
            os.path.join(os.getcwd(), "assets", "test.jpg")
        )
        self.backgroundImage = pygame.transform.scale(
            self.backgroundImage,
            (self.menuScreen.get_width(), self.menuScreen.get_height()),
        )

        self.title = TextModule.Text(
            self.menuScreen, (10 * self.sf, 10 * self.sf), "TOWER DEFENSE", 36
        )
        self.title.setPosition(
            (self.screenWidth / 2 - self.title.getSize()[0] / 2, 10 * self.sf)
        )

        self.startButton = ButtonModule.Button(
            self.menuScreen,
            self.buttonSize,
            (self.screenCenter[0] - self.buttonWidth / 2, 100 * self.sf),
            "blue",
            "Start game",
            borderRadius=30,
            hoverBg="gray",
        )

        self.buttonGap = 30 * self.sf

        self.settingsButton = ButtonModule.Button(
            self.menuScreen,
            self.buttonSize,
            (
                self.screenCenter[0] - self.buttonWidth / 2,
                self.startButton.getPosition()[1] + self.buttonHeight + self.buttonGap,
            ),
            "green",
            "Settings",
            borderRadius=30,
            hoverBg="gray",
        )

        self.exitButton = ButtonModule.Button(
            self.menuScreen,
            self.buttonSize,
            (
                self.screenCenter[0] - self.buttonWidth / 2,
                self.settingsButton.getPosition()[1]
                + self.buttonHeight
                + self.buttonGap,
            ),
            "red",
            "Exit game",
            borderRadius=30,
            hoverBg="gray",
        )

        self.buttons = [self.startButton, self.settingsButton, self.exitButton]

        self.startButton.onClick(self.goToLevelSelection)
        self.exitButton.onClick(self.Exit)
        self.settingsButton.onClick(self.goToSettings)

        self.settings()
        self.selectLevel()
        self.selectDifficulty()

    def goToLevelSelection(self):
        self.currentScreen = 2

    def startGame(self, diff):
        self.newGame = game.Game(self.screen, self.sf, difficulty=diff, level=self.maps[self.currentMapIdx][0])
        self.currentScreen = 4

    def goToSettings(self):
        self.currentScreen = 1

    def draw(self):
        self.menuScreen.blit(self.backgroundImage, (0, 0))
        self.title.draw()
        self.startButton.draw()
        self.settingsButton.draw()
        self.exitButton.draw()
        self.screen.blit(self.menuScreen, (0, 0))

    def menuRun(self):
        while self.currentScreen == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentScreen = None
                    self.running = False

                if event.type == pygame.MOUSEMOTION:
                    ButtonModule.isHovered(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.startButton.clicked(event):
                        pass
                    self.settingsButton.clicked(event)
                    self.exitButton.clicked(event)

                self.draw()
                pygame.display.flip()

    def run(self):
        while self.running:
            if self.currentScreen == 0:
                self.menuRun()
            if self.currentScreen == 1:
                self.settingsRun()
            if self.currentScreen == 2:
                self.selectLevelRun()
            if self.currentScreen == 3:
                self.selectDifficultyRun()
            if self.currentScreen == 4:
                self.running, self.currentScreen = self.newGame.run()

    def Exit(self):
        self.currentScreen = None
        self.running = False

    def setWindowed(self):
        Settings.Settings.set("display", "windowed")
        self.screen = pygame.display.set_mode(
            Settings.Settings.getSettings()["resolution"]
        )

        self.screenMode = 0

        return True

    def setFullscreen(self):
        Settings.Settings.set("display", "fullscreen")
        self.screen = pygame.display.set_mode(
            Settings.Settings.getSettings()["resolution"],
            Settings.Settings.getSettings()["display"],
        )
        self.screenMode = pygame.FULLSCREEN
        return True

    def setResolution(self, *args):
        newSize = str(args[0])
        Settings.Settings.set("resolution", newSize)
        scaleFactor = (
            (Settings.Settings.getSettings()["resolution"][0] * 100) / 800
        ) / 100
        self.screen = pygame.display.set_mode(
            Settings.Settings.getSettings()["resolution"], self.screenMode
        )
        self.__init__(self.screen, scaleFactor=scaleFactor)

    def goBack(self):
        self.currentScreen = 0

    def settings(self):

        self.settingsFont = TextModule.Text(
            self.settingsScreen, (0, 0), "SETTINGS", size=48
        )
        self.displayFont = TextModule.Text(
            self.settingsScreen,
            (0, (self.settingsFont.getPosition()[1] + 80) * self.sf),
            "Display",
            size=24,
        )

        self.displayTextFormatted = Settings.Settings.readRaw()["display"].capitalize()

        self.displaySettings = SelectModule.Select(
            self.settingsScreen,
            (300 * self.sf, 60 * self.sf),
            ["Windowed", "Fullscreen"],
            (100 * self.sf, 100 * self.sf),
            [self.setWindowed, self.setFullscreen],
            self.displayTextFormatted,
        )

        self.resolutionTextFormatted = Settings.Settings.readRaw()["resolution"].split(
            ","
        )
        self.resolutionTextFormatted = (
            self.resolutionTextFormatted[0] + "x" + self.resolutionTextFormatted[1]
        )
        self.resolution = SelectModule.Select(
            self.settingsScreen,
            (300 * self.sf, 60 * self.sf),
            ["1024x768", "800x600"],
            (100 * self.sf, 200 * self.sf),
            [
                lambda: self.setResolution("1024,768"),
                lambda: self.setResolution("800,600"),
            ],
            self.resolutionTextFormatted,
        )

        self.gameVolume = SliderModule.Slider(
            self.settingsScreen,
            (383 * self.sf, 30 * self.sf),
            (100 * self.sf, 300 * self.sf),
        )

        self.applyButton = ButtonModule.Button(
            self.settingsScreen,
            (self.buttonWidth, self.buttonHeight),
            (self.menuScreen.get_width() / 2 - self.buttonWidth / 2, 450 * self.sf),
            "red",
            "Apply changes",
            borderRadius=30,
        )
        self.applyButton.onClick(self.goBack)

        self.updateRect = (0, 0, self.screenRect.width, self.screenRect.height)

        self.displaySettings.setClearScreen(self.screen.copy())
        self.resolution.setClearScreen(self.screen.copy())

    def settingsRun(self):

        self.settingsDraw()
        pygame.display.flip()
        self.updateRect = pygame.Rect(
            100 * self.sf,
            100 * self.sf,
            (self.screenRect.width - 100) * self.sf,
            (self.screenRect.height - 100) * self.sf,
        )

        while self.currentScreen == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.displaySettings.isActive() == 0:
                        self.resolution.clicked(event)
                    self.displaySettings.clicked(event)

                    self.applyButton.clicked(event)

                vol = self.gameVolume.clicked(event)
                Settings.Settings.set("volume", str(vol))

                if vol != None:
                    pygame.mixer_music.set_volume(vol / 100)

            self.settingsDraw()
            pygame.display.update()

    def settingsDraw(self):
        self.settingsScreen.fill("black")
        self.settingsFont.draw()

        self.gameVolume.draw()
        self.gameVolume.percentageDisplay(
            (
                self.gameVolume.getRect().width + self.gameVolume.getRect().x,
                self.gameVolume.getRect().y,
            )
        )
        self.resolution.draw()
        self.displaySettings.draw()
        self.displayFont.draw()
        self.applyButton.draw()

        self.screen.blit(self.settingsScreen, (0, 0))

    def goToLeftElement(self):
        if self.currentMapIdx == 0: 
            self.currentMapIdx = len(self.maps)-1
        else:
            self.currentMapIdx -= 1


        self.levelTitle.setText(self.maps[self.currentMapIdx][0])
        self.levelTitle.setPosition(
            (
                self.screenRect.width / 2 - self.levelTitle.getSize()[0] / 2,
                self.currentLevelImageRect.y + self.currentLevelImageRect.height,
            )
        )
        self.selectLevelDraw()

    def goToRightElement(self):
        if self.currentMapIdx == len(self.maps) - 1:
            self.currentMapIdx = 0
        else:
            self.currentMapIdx += 1

        self.levelTitle.setText(self.maps[self.currentMapIdx][0])
        self.levelTitle.setPosition(
            (
                self.screenRect.width / 2 - self.levelTitle.getSize()[0] / 2,
                self.currentLevelImageRect.y + self.currentLevelImageRect.height,
            )
        )

        self.selectLevelDraw()

    def selectLevel(self):
        self.currentLevelSize = (300, 300)
        self.mapPath = os.path.join(os.getcwd(), "assets", "map")
        self.maps = [
            [
                "Greenfield",
                pygame.transform.scale(
                    pygame.image.load(os.path.join(self.mapPath, "background.png")),
                    self.currentLevelSize,
                ),
            ],
            [
                "Desert",
                pygame.transform.scale(
                    pygame.image.load(os.path.join(self.mapPath, "map_desert.png")),
                    self.currentLevelSize,
                ),
            ],
            [
                "Cave",
                pygame.transform.scale(
                    pygame.image.load(os.path.join(self.mapPath, "map_cave.png")),
                    self.currentLevelSize,
                ),
            ],
        ]
        self.currentMapIdx = 0

        self.selectLevelText = TextModule.Text(
            self.selectLevelScreen, (0, 0), "SELECT LEVEL", size=67
        )
        self.selectTextCenterPos = (
            self.screenRect.width / 2 - self.selectLevelText.getSize()[0] / 2,
            10,
        )
        self.selectLevelText.setPosition(self.selectTextCenterPos)

        self.currentLevelImage = pygame.image.load(
            os.path.join(os.getcwd(), "assets", "map", "background.png")
        )
        self.currentLevelImageRect = pygame.Rect(
            self.screenRect.width / 2 - self.currentLevelSize[0] / 2,
            self.selectTextCenterPos[1] + self.selectLevelText.getSize()[1] + 20,
            self.currentLevelSize[0],
            self.currentLevelSize[1],
        )

        self.leftArrowButton = ButtonModule.Button(
            self.selectLevelScreen,
            (50, 50),
            (
                self.currentLevelImageRect.x - 50 - 10,
                self.currentLevelImageRect.y
                + (self.currentLevelImageRect.height / 2 - 50 / 2),
            ),
            color="gray",
            text="",
        )

        self.rightArrowButton = ButtonModule.Button(
            self.selectLevelScreen,
            (50, 50),
            (
                self.currentLevelImageRect.x + self.currentLevelImageRect.width + 10,
                self.currentLevelImageRect.y
                + (self.currentLevelImageRect.height / 2 - 50 / 2),
            ),
            color="gray",
            text="",
        )

        self.rightArrowButton.onClick(self.goToRightElement)
        self.leftArrowButton.onClick(self.goToLeftElement)

        self.levelTitle = TextModule.Text(
            self.selectLevelScreen, (0, 0), self.maps[self.currentMapIdx][0], 40
        )
        self.levelTitle.setPosition(
            (
                self.screenRect.width / 2 - self.levelTitle.getSize()[0] / 2,
                self.currentLevelImageRect.y + self.currentLevelImageRect.height,
            )
        )

        self.confirmButton = ButtonModule.Button(
            self.selectLevelScreen,
            (100, 50),
            (
                self.screenRect.width / 2 - 100 / 2,
                self.levelTitle.getPosition()[1] + self.levelTitle.getSize()[1] + 20,
            ),
            "Brown",
            "Confirm",
        )

        self.confirmButton.onClick(self.goToDiffSelection)
        print(self.levelTitle.getPosition())


    def selectLevelRun(self):
        while self.currentScreen == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.leftArrowButton.clicked(event)
                    self.rightArrowButton.clicked(event)

                    self.confirmButton.clicked(event)

            self.selectLevelDraw()
            pygame.display.update()

    def selectLevelDraw(self):
        self.selectLevelScreen.fill("#000000")
        self.selectLevelScreen.blit(
            self.maps[self.currentMapIdx][1], self.currentLevelImageRect
        )

        self.leftArrowButton.draw()
        self.rightArrowButton.draw()

        pygame.draw.polygon(
            self.selectLevelScreen,
            "white",
            (
                (
                    self.leftArrowButton.getRect().x
                    + self.leftArrowButton.getRect().width
                    - 10,
                    self.leftArrowButton.getRect().y + 10,
                ),
                (
                    self.leftArrowButton.getRect().x + 10,
                    self.leftArrowButton.getRect().y
                    + self.leftArrowButton.getRect().height / 2,
                ),
                (
                    self.leftArrowButton.getRect().x
                    + self.leftArrowButton.getRect().width
                    - 10,
                    self.leftArrowButton.getRect().y
                    + self.leftArrowButton.getRect().height
                    - 10,
                ),
            ),
        )

        pygame.draw.polygon(
            self.selectLevelScreen,
            "white",
            (
                (
                    self.rightArrowButton.getRect().x + 10,
                    self.rightArrowButton.getRect().y + 10,
                ),
                (
                    self.rightArrowButton.getRect().x
                    + self.rightArrowButton.getRect().width
                    - 10,
                    self.rightArrowButton.getRect().y
                    + self.rightArrowButton.getRect().height / 2,
                ),
                (
                    self.rightArrowButton.getRect().x + 10,
                    self.rightArrowButton.getRect().y
                    + self.rightArrowButton.getRect().height
                    - 10,
                ),
            ),
        )

        self.levelTitle.draw()
        self.confirmButton.draw()
        self.selectLevelText.draw()

        self.screen.blit(self.selectLevelScreen, (0, 0))

    def goToDiffSelection(self):
        self.currentScreen = 3

    def selectDifficulty(self):
        self.optionSize = [500, 100]

        self.header = TextModule.Text(
            self.selectDifficultyScreen, (0, 0), "SELECT DIFFICULTY", size=60
        )

        self.header.setPosition(
            (self.screenWidth / 2 - self.header.getSize()[0] / 2, 10)
        )

        self.easy = ButtonModule.difficultyButton(
            self.selectDifficultyScreen,
            (550, 140), 
            (0,0), 
            "pink",
            pygame.image.load(os.path.join(os.getcwd(), "creatures", "dragon.png")), 
            "EASY",
            "RELAKSUJACA   ZABAWA", 
            "100",
            "1000",
            "50"
        )

        self.medium = ButtonModule.difficultyButton(
            self.selectDifficultyScreen,
            (550, 140), 
            (0,0), 
            "blue",
            pygame.image.load(os.path.join(os.getcwd(), "creatures", "dragon.png")), 
            "CHALLENGING",
            "Zmierz   sie   z   losem", 
            "70",
            "750",
            "60"
        )

        self.hard = ButtonModule.difficultyButton(
            self.selectDifficultyScreen,
            (550, 140), 
            (0,0), 
            "red",
            pygame.image.load(os.path.join(os.getcwd(), "creatures", "dragon.png")), 
            "NIGHTMARE",
            "PIEKIELNIE   TRUDNA   ZABAWA", 
            "50",
            "500",
            "75"
        )

        self.easy.setPosition((self.screenWidth/2 - (self.easy.getSize()[0]/2), self.header.getPosition()[1] + self.header.getSize()[1] + 10))
        self.medium.setPosition((self.screenWidth/2 - (self.medium.getSize()[0]/2), self.easy.getPosition()[1] + self.easy.getSize()[1] + 10))
        self.hard.setPosition((self.screenWidth/2 - (self.hard.getSize()[0]/2), self.medium.getPosition()[1] + self.medium.getSize()[1] + 10))


        self.easy.onClick(self.startGame, "easy")
        self.medium.onClick(self.startGame, "challenging")
        self.hard.onClick(self.startGame, 'nightmare')



    def selectDifficultyRun(self):
        while self.currentScreen == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy.clicked(event)
                    self.medium.clicked(event)
                    self.hard.clicked(event)

            self.selectDifficultyDraw()
            pygame.display.update()

    def selectDifficultyDraw(self):
        self.selectDifficultyScreen.fill("black")

        self.header.draw()

        self.easy.draw()
        self.medium.draw()
        self.hard.draw()

        self.screen.blit(self.selectDifficultyScreen, (0, 0))
