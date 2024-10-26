class Settings():
    def __init__(self):
        # configuracoes de tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # configuracoes da nave
        self.ship_speed_factor = 1.5

        # configuracoes dos projeteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_speed_factor = 1
        self.bullets_allowed = 3

        # configuracoes alienigenas
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1 # 1 representa "direita", -1 representa "esquerda"