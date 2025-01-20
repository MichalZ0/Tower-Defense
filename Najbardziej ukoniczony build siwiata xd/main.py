import pygame

import Menu
import Settings

pygame.init()
pygame.mixer.init()


Settings.Settings.set('resolution', '800,600')
resolution = Settings.Settings.getSettings()['resolution']
# print(resolution[0])
scaleFactor = ((resolution[0] * 100) / 800)/100  # 800x600 is base resolution, every resolution change is made base on that initial value


screen = pygame.display.set_mode(resolution)
screen.fill('blue')
clock = pygame.time.Clock()
running = True
menu = Menu.mainMenu(screen, 'green', scaleFactor)

menu.run()

pygame.quit()  