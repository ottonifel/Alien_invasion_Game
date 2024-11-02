class Settings():
    def __init__(self):
        # configuracoes de tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # configuracoes da nave
        self.ship_limit = 3

        # configuracoes dos projeteis
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # configuracoes alienigenas
        self.fleet_drop_speed = 10

        # taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        # taxa em que os pontos dos alienigenas aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo"""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1 # 1 representa "direita", -1 representa "esquerda"
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade e os pontos para cada alienigena"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)