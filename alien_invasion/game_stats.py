class GameStats():
    '''游戏数据统计'''
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏开始是处于非活动状态
        self.game_active = False

    def reset_stats(self):
        '''初始化游戏运行期间可能变化的信息'''
        self.ship_left = self.ai_settings.ship_limit
