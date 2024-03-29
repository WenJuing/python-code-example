import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''单个外星人的类'''

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/cong.png')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储准确位置
        self.x = float(self.rect.x)

    def update(self):
        '''外星人移动'''
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''检查外星人是否在屏幕边缘，是返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)
