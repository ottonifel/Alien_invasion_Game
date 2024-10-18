import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de teclado e mouse"""
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                 
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        # Move nave para direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
     """Atualiza as imagens na tela e alterna para a nova tela"""
     # Redesenha a tela a cada passagem pelo laco
     screen.fill(ai_settings.bg_color)
     ship.blitme() # desenha a nave
     
     for bullet in bullets.sprites(): # desenha cada projetil
         bullet.draw_bullet()

     # Deixa a tela mais recente vísivel
     pygame.display.flip()

def update_bullets(bullets):
    """Atualiza as posicoes dos projeteis e se livra de projeteis antigos"""
    # atualiza posicao das balas (chama o metodo update() da classe Bullet para cada instancia de Bullet dentro do Group)
    bullets.update()
    # apaga projeteis que desapareceram
    for bullet in bullets.copy(): # copy() evita problemas ao remover itens da coleção que estamos percorrendo.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projetil se o limite nao foi alcancado"""
    if len(bullets) < ai_settings.bullets_allowed: # se não atingiu o limite de projeteis na tela
        # cria um novo projetil e adiciona ao grupo de projéteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

 