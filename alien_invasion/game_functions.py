import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''按下按键'''
    # 控制飞船移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    # 创建子弹并添加到编组
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # 控制游戏结束
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    ''' 松开按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    '''玩家单击play时启动游戏'''
    button_checked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_checked and not stats.game_active:
        stats.game_active = True

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()

        # 清空外星人
        aliens.empty()

        # 创建新的外星人并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    '''更新屏幕'''
    screen.fill(ai_settings.bg_color)

    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)  # 自动绘制编组的每个元素（位置由它们的rect决定）

    # 如果游戏没有处于活动状态，则绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(ai_settings, screen, ship, aliens, bullets):
    '''更新子弹'''
    bullets.update()
    # 删除已消失的屏幕
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    '''碰撞检测'''
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    # 外星人消灭完了，则再生成新的外星人
    if len(aliens) == 0:
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_alines_x(ai_settings, alien_width):
    '''获取一行可容纳的外星人数量'''
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''获取屏幕可容纳多少行外星人'''
    avaliable_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''生成一个外星人'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''生成外星人群'''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alines_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''检查舰队是否到达屏幕边缘'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    ''' 将整群外星人下移，并改变它们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''更新外星人群的位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''外星人与飞船碰撞'''
    # 飞船生命减1
    stats.ship_left -= 1
    if stats.ship_left > 0:
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建新的外星人群并把飞船重新放在底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 短暂暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
