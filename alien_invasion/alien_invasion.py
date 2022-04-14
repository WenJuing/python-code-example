import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('外星葱入侵')

    # 创建一艘飞船、子弹的编组、外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建统计器
    stats = GameStats(ai_settings)

    # 创建按钮
    play_button = Button(ai_settings, screen, 'play')

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        ship.update()

        gf.update_bullet(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
