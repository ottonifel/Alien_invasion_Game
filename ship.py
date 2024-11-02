import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """inicializa a nave e sua posicao inicial"""

        super().__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings

        # flags de movimento
        self.moving_right = False
        self.moving_left = False

        # carrega imagem da espaconave
        self.image = pygame.image.load('images/ship.bmp')

        # interpreta e guarda a espaconave como um "retangulo"
        self.rect = self.image.get_rect()
        # interpreta e guarda a tela como um "retangulo"
        self.screen_rect = screen.get_rect()

        # posiciona a nave na parte inferior central
        self.rect.centerx = self.screen_rect.centerx    #(coordenada do centro da nave tem que ser a mesma do centro da tela)
        self.rect.bottom = self.screen_rect.bottom      #(coordenada do fundo da nave tem que coincidir com a do fundo da tela)

        # Armazena um valor decimal para o centro da espaconave
        self.center = float(self.rect.centerx)
    
    def update(self):
        """Atualiza posicao da nave de acordo com tag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1 (esse so aceita int)
            self.center += self.ai_settings.ship_speed_factor  # esse aceita decimais

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center # rect.centerx so armazena a parte inteira ou seja a velocidade até incrementar no proximo inteiro muda

    def blitme(self):
        """Desenha a espaconave na posicao atual"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaconave na tela"""
        self.center = self.screen_rect.centerx