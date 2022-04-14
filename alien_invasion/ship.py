import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置飞船位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/chuying.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕正下方
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 存储小数
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''控制移动'''
        if self.moving_right and self.rect.right < self.screen_rect.right:  # 右移动
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:     # 左移动
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:  # 上移动
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:   # 下移动
            self.center_y += self.ai_settings.ship_speed_factor

        # centerx只能存储整数，通过上面的操作可以实现小数级别的移动
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def center_ship(self):
        '''把飞船放在中央'''
        # 将飞船放在屏幕正下方
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
