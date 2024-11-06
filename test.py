import pygame
background_colour = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((1024, 768))

testBG = pygame.Surface((1024, 768))
testBG.fill('blue')

rect = pygame.draw.rect(testBG, 'red', (1024-100, 768-100, 100, 100))

currentScreen = testBG




pygame.display.set_caption('Tutorial 1')
pygame.display.flip()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        previousSize = [screen.get_width(), screen.get_height()]

        screen = pygame.display.set_mode((800, 600))
        testBG = pygame.transform.scale(testBG, (800,600))

        currentScreen = testBG

        changeRatio = (currentScreen.get_width() * 100 / previousSize[0] ) / 100
        print('before', rect)
        rect = pygame.Rect(rect.x * changeRatio, rect.y * changeRatio, rect.width * changeRatio, rect.height * changeRatio)
        print('after', rect)

        if (rect.collidepoint(event.pos)):
            print('clicked')
  screen.blit(currentScreen, (0,0))
  pygame.display.update()
