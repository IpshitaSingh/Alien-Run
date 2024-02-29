import pygame

class GUI:
    @staticmethod
    def draw_text(surface, text, font_name, font_size, color, x, y):
        font = pygame.font.SysFont(font_name, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)

class Graphics:
    @staticmethod
    def load_image(image_path):
        return pygame.image.load(image_path).convert_alpha()
