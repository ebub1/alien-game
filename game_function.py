#!/usr/bin/env python3

import pygame
import sys
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint
#tracking keyboard and mouse movements
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key==pygame.K_RIGHT:
    #moving ship right
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
def fire_bullet(ai_settings, screen, ship, bullets):
    #Creating a new bullet and adding into bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship )
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Bullet position update and delete the old one"""
    #Bullet position update
    bullets.update()
    #Delete bullets when they out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings, screen,ship,aliens, bullets)    
        
def check_bullet_alien_collisions(ai_settings, screen,ship,aliens, bullets):       
    #Check if bullet collide alien
    #when collision is happened delete bullet
    collisions = pygame.sprite.groupcollide( aliens, bullets, True, True)
    if len(aliens) == 0:
        #Delete bullets and create new fleet
        bullet.empty()
        create_fleet(ai_settings, screen, ship, aliens)
    
def get_number_aliens_x(ai_settings, alien_width):
    # Calculate  amount of aliens in row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate amount of alien's rows"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) -ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Create first row of aliens
    alien = Alien(ai_settings, screen)
    alien_width =alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)
def create_fleet(ai_settings, screen,ship, aliens):
    """Create a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
def check_fleet_edges(ai_settings, ship, aliens):
    """React when alien reach edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        if pygame.sprite.spritecollideany(ship, aliens):
            print("Ship hit!!!")
def change_fleet_direction(ai_settings, aliens):
    """Down all fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1
def update_aliens(ai_settings, ship, aliens):
    """check if alien rech edge and update position all aliens in the fleet"""
    check_fleet_edges(ai_settings, ship, aliens)
    aliens.update()

def get_number_star_x(ai_settings, star_width):
    # Calculate  amount of star in row
    available_space_x = ai_settings.screen_width
    number_star_x = int(available_space_x / star_width)
    return number_star_x
def get_number_star_rows(ai_settings, star_height):
    """Calculate amount of star's rows"""
    available_space_y = ai_settings.screen_height
    number_star_rows = int(available_space_y / star_height)
    return number_star_rows
def create_star(ai_settings, screen, stars, star_number, star_row_number):
    #Create first row of star
    random_number = randint(-50, 50)
    star = Star(ai_settings, screen)
    star_width =star.rect.width
    star.x = star_width + 2 * star_width * star_number - random_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2*star.rect.height * star_row_number + random_number
    stars.add(star)
def create_sky(ai_settings, screen, stars):
    """Create a sky ful of stars"""
    star = Star(ai_settings, screen)
    number_star_x = get_number_star_x(ai_settings, star.rect.width)
    star_number_rows = get_number_star_rows(ai_settings, star.rect.height)
    for star_row_number in range(star_number_rows):
        for star_number in range(number_star_x):
            create_star(ai_settings, screen, stars, star_number, star_row_number)

def update_screen(ai_settings, screen, stars, ship, aliens, bullets):
    #The screen is redrawn on each iteration of the loop
    screen.fill(ai_settings.bg_colour)
    stars.draw(screen)
    #All the bullets draw behinde the ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip() 