import pygame
from setting import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    
    """Inicializa o jogo e cria um objeto para a tela"""
    pygame.init()

    # cria a tela do jogo
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Cria botão Play
    play_button = Button(ai_settings, screen, "Play")

    # cria uma instancia para armazenar dados estatisticos do jogo
    stats = GameStats(ai_settings)
    # cria painel de pontuação
    sb = Scoreboard(ai_settings, screen, stats)
    
    # cria uma espaconave e sua posicao
    ship = Ship(ai_settings, screen)
 
    # cria um grupo no qual armazena projeteis e um para alienigenas
    bullets = Group()
    aliens = Group()

    # cria a frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo 
    while True:
        # Observa eventos de teclado e de mouse 
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            # atualiza posicao da nave
            ship.update()

            # atualiza posicao das balas (chama o update() de cada instancia de Bullet dentro do Group)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # atualiza posicao dos alienigenas
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            
        # Redesenha a tela a cada passagem do laco
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

