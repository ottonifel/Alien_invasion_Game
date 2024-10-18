import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projeteis disparados pela nave"""

    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto para projetil na posicao atual da nave"""
        super().__init__()
        self.screen = screen
        # cria um retangulo para o projétil em (0,0) --> depois sera definido a posicao correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        # posicao em que o projetil ira emergir
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        """Move o projetil para cima na tela"""
        # atualiza a posicao decimal do projetil
        self.y -= self.speed_factor # decremento da coordenada y (para o projetil subir) no mesmo valor da velocidade do projetil
        # atualiza a posicao de rect
        self.rect.y = self.y 

    def draw_bullet(self):
        """Desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)