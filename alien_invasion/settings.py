class Settings():
    '''存储游戏的所有设置'''

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (4, 4, 25)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 18
        self.bullet_color = (127, 255, 212)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # 1代表右移，-1代表左移
