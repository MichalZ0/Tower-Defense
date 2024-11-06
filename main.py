import pygame

import Menu

pygame.init()
screen = pygame.display.set_mode((1280,720))
screen.fill('blue')
clock = pygame.time.Clock()
running = True


menu = Menu.mainMenu(screen, 'green')

menu.run()

pygame.quit()



