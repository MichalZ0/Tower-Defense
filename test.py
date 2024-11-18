import pygame
background_colour = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((1024, 768))


pygame.font.init()  # Inicjalizowanie modułu czcionek
screen.fill('black')
font = pygame.font.Font(None, 70)  # None używa domyślnej czcionki, 36 to rozmiar czcionki

# Kolor tekstu (czarny)
text_color = (0, 0, 0)

# Tekst do narysowania
text = font.render('Hello, Pygame!', True, 'white')
screen.blit(text, (0,0))


pygame.display.set_caption('Tutorial 1')
pygame.display.flip()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN: 
        screen.blit(text, (0,0))
        print('true')

    # screen.blit(text, (0,0))

    pygame.display.update()
