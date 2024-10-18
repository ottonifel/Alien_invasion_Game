import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    
    """Inicializa o jogo e cria um objeto para a tela"""
    pygame.init()

    # cria a tela do jogo
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # cria uma espaconave e sua posicao
    ship = Ship(ai_settings, screen)
 
    # cria um grupo no qual armazena projeteis
    bullets = Group()

    # Inicia o laço principal do jogo 
    while True:
        # Observa eventos de teclado e de mouse 
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # atualiza posicao da nave
        ship.update()

        # atualiza posicao das balas (chama o update() de cada instancia de Bullet dentro do Group)
        gf.update_bullets(bullets)
        
        # Redesenha a tela a cada passagem do laco
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

