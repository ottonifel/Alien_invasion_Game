import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa um unico alienigena da frota"""
    def __init__(self, ai_settings, screen):
        """Inicializa o alienigena e define sua posicao inicial"""
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # carrega imagem e rect do alienigena
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienigena em sua posicao atual"""
        self.screen.blit(self.image, self.rect)
        



        