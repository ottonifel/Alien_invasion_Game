class GameStats():
    """Armazena dados estatisticos da Invasao Alienigena"""
    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # inicia o jogo em estado inativo
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 # sempre que um novo jogo comecar a pontuação deve reiniciar
        self.level = 1

        