import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responde a eventos de teclado e mouse"""
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                 
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando clicar em play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        # reinicia as configuracoes do jogo
        ai_settings.initialize_dynamic_settings()
        # reinicia os dados estáticos
        stats.reset_stats()
        stats.game_active = True
        # reinicia as imagens do painel de pontuaão
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # esvazia listas de alienigenas e projeteis
        aliens.empty()
        bullets.empty()
        # cria uma nova frota e centraliza a espaconave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        # Move nave para direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: # atalho para fechar o jogo
        sys.exit()

def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
     """Atualiza as imagens na tela e alterna para a nova tela"""
     # Redesenha a tela a cada passagem pelo laco
     screen.fill(ai_settings.bg_color)
     ship.blitme() # desenha a nave
     aliens.draw(screen)
     
     for bullet in bullets.sprites(): # desenha cada projetil
         bullet.draw_bullet()

     # Desenha a informação sobre a pontuação
     sb.show_score()
    
     # desenha o botao Play se o jogo estiver inativo
     if not stats.game_active:
         play_button.draw_button()
         
     # Deixa a tela mais recente vísivel
     pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Atualiza as posicoes dos projeteis e se livra de projeteis antigos"""
    # atualiza posicao das balas (chama o metodo update() da classe Bullet para cada instancia de Bullet dentro do Group)
    bullets.update()
    # apaga projeteis que desapareceram
    for bullet in bullets.copy(): # copy() evita problemas ao remover itens da coleção que estamos percorrendo.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Verifica se algum projetil atingiu um alienigena e apaga ambos se sim
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projetil se o limite nao foi alcancado"""
    if len(bullets) < ai_settings.bullets_allowed: # se não atingiu o limite de projeteis na tela
        # cria um novo projetil e adiciona ao grupo de projéteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Atualiza as posicoes de todos ps alienigenas da frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Verifica colisoes entre alienigenas e espaconave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
        # print("Ship hit!!!")
    # Verifica se algum alienigena atingiu o fundo da tela
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienigenas"""
    # cria um alienigena e calcula o numero de alienigenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # cria a primeira linha de alienigenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # cria um alienigena e posiciona na linha
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """Determina o numero de alienigenas que cabem em uma linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width # para deixar uma margem do tamanho do alien nas bordas verticais da tela
    number_aliens_x = int(available_space_x / (2 * alien_width)) # quantos alienigenas cabem sendo que um alienigena ocupa o espaço de dois aliens por conta do espaçamento entre os aliens
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Cria um alienigena e o posiciona na linha"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number # onde eu vou inserir ele horizontalmente considerando margem e espaçamento entre naves
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number # onde vou inserir ele verticalmente considerando margem e espaçamento entre linhas
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o numero de linhas com alienigenas que cabem na tela"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height ) # 
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    """Responde se algum alienigena alcançou a borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda sua direcao"""
    
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 #inverte a direcao atual

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisões entre projéteis e alienigenas"""
    # Verifica se algum projetil atingiu um alienigena e apaga ambos se sim
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # modifica a pontuação
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
    sb.prep_score()
    check_high_score(stats, sb)
    # verifica se precisa de uma nova frota
    if len(aliens) == 0:
        # incrementa o nível:
        stats.level += 1
        sb.prep_level()
        # apaga os projeteis da tela, aumenta a velocidade/nivel e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Responde ao fato da espaconave ter sido atingida por um alienigena"""
    if stats.ships_left > 0:
        # Decrementa ship_left e atualiza o painel de pontuacao
        stats.ships_left -= 1
        sb.prep_ships()

        # Esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        bullets.empty()

        #Cria uma nova frota e centraliza a espaconave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Verifica se algum alienigena alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação máxima"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()