import pygame


class SidePanel:
    def __init__(self, screen, width, height, sf, width_size=150):
        self.width_size = width_size
        self.screen = screen
        self.width = width
        self.height = height
        self.sf = sf
        self.color = (30, 30, 30)  # Kolor panelu
        self.button_color = (70, 130, 180)  # Kolor przycisku
        self.button_hover_color = (100, 160, 210)
        self.button_pressed_color = (50, 90, 130)
        self.button_rect = pygame.Rect(self.width - 134 * sf, self.height - 100 * sf, 120 * sf, 50 * sf)
        self.button_text = "Start Wave"
        self.button_font = pygame.font.Font(None, int(24 * sf))
        self.button_pressed = False

        # Załadowanie obrazu do panelu
        self.panel_image = pygame.image.load("wood_texture.jpeg")
        self.panel_image = pygame.transform.scale(self.panel_image,
                                                  (self.width_size * self.sf, self.height))

    def draw(self):
        self.screen.blit(self.panel_image, (self.width - self.width_size * self.sf, 0))

        # Rysowanie przycisku
        button_color = self.button_color
        if self.button_pressed:
            button_color = self.button_pressed_color
        elif self.button_rect.collidepoint(pygame.mouse.get_pos()):
            button_color = self.button_hover_color

        pygame.draw.rect(self.screen, button_color, self.button_rect, border_radius=10)

        # Dodawanie tekstu na przycisk
        text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.button_pressed = True
                return True  # Przycisnięcie wykryte
        elif event.type == pygame.MOUSEBUTTONUP:
            self.button_pressed = False
        return False
